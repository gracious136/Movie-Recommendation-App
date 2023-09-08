import streamlit as st
import pandas as pd
import requests
import pickle
import sklearn
from sklearn.metrics.pairwise import cosine_similarity

#settings for the webpage
st.set_page_config(page_title='SMG Movies', page_icon ="🎬", layout="wide", initial_sidebar_state="collapsed")



#readin my movie data
movies = pd.read_csv('https://raw.githubusercontent.com/gracious136/Movie-Recommendation-App/main/data/movies.csv')
ratings = pd.read_csv('https://raw.githubusercontent.com/gracious136/Movie-Recommendation-App/main/data/ratings.csv')
tags = pd.read_csv('https://raw.githubusercontent.com/gracious136/Movie-Recommendation-App/main/data/tags.csv')
links = pd.read_csv('https://raw.githubusercontent.com/gracious136/Movie-Recommendation-App/main/data/links.csv')
df = pd.read_csv('https://raw.githubusercontent.com/gracious136/Movie-Recommendation-App/main/data/MovieGenre.csv', encoding="ISO-8859-1", usecols=["imdbId", "Title", "Genre", "Poster"])
df['title']= df['Title']
df.drop('Title', axis =1, inplace=True)

# Define the URL of the model file
model_url = 'https://github.com/gracious136/Movie-Recommendation-App/raw/main/data/movie_model.sav'

# Use requests to fetch the model from the URL
response = requests.get(model_url)

# Check if the request was successful
if response.status_code == 200:
    # Create a binary stream from the response content
    model_stream = response.content
    
    # Use pickle to load the model from the binary stream
    movie_model = pickle.loads(model_stream)

    # Now, you can use 'movie_model' as your loaded model
else:
    # Handle the case where the request to fetch the model was unsuccessful
    st.error("Failed to fetch the model")

#movie_model =pickle.load(open('https://github.com/gracious136/Movie-Recommendation-App/blob/main/data/movie_model.sav', 'rb'))

movie_ratings = movies.merge(ratings, how = 'inner', on = 'movieId')


# model = joblib.load('your_model.pkl')


def top_rated_movies():
    movie_ratings = movies.merge(ratings, how = 'inner', on = 'movieId')
    average_ratings = movie_ratings.groupby('title').agg({'movieId':'count', 'rating' : 'mean'})\
                              .rename(columns = {'movieId': 'number_of_ratings', 'rating' : 'average_rating'})\
                              .sort_values(by = ['average_rating', 'number_of_ratings'], ascending = [False, False]).reset_index()
    
    average_ratings['popularity_score'] = (average_ratings['average_rating']*0.4 + average_ratings['number_of_ratings']*0.6) / (average_ratings['average_rating'] + average_ratings['number_of_ratings'])
    
    result = average_ratings.sort_values(by = 'popularity_score', ascending = False).loc[average_ratings['average_rating']>=4.5][['title', 'average_rating']].head(35).merge(df, how = 'inner', on = 'title')
    result['average_rating'] = round(result['average_rating'], 1)
    return result[['title', 'average_rating', 'Poster']].head(10)


def top_popular_movies():
    movie_ratings = movies.merge(ratings, how = 'inner', on = 'movieId')
    average_ratings = movie_ratings.groupby('title').agg({'movieId':'count', 'rating' : 'mean'})\
                              .rename(columns = {'movieId': 'number_of_ratings', 'rating' : 'average_rating'})\
                              .sort_values(by = 'number_of_ratings', ascending = False).reset_index()  #, 'average_rating']
    
    # average_ratings['popularity_score'] = (average_ratings['average_rating']*0.4 + average_ratings['number_of_ratings']*0.6) / (average_ratings['average_rating'] + average_ratings['number_of_ratings'])
    
    result = average_ratings.loc[average_ratings['average_rating']>=4][['title', 'average_rating']].head(25).merge(df, how = 'inner', on = 'title')
    result['average_rating'] = round(result['average_rating'], 1)
    return result[['title', 'average_rating', 'Poster']].head(5)


# user-collaborative filtering
def related_movies(title):
    
    movie_ratings = movies.merge(ratings, how = 'inner', on = 'movieId')
    movie = str(title)
    movie_id = movies.loc[movies['title']==movie].iloc[0,0]
    movie_matrix = pd.pivot_table(movie_ratings,
                            columns='movieId',
                            index = 'userId',
                            values = 'rating',
                            aggfunc='mean',
                            fill_value=0)
    
    movie_cosine =pd.DataFrame(cosine_similarity(movie_matrix.T),
                              columns=movie_matrix.columns,
                              index = movie_matrix.columns)
    movie_df = pd.DataFrame(movie_cosine[movie_id]).rename(columns={movie_id : 'cosine_similarity'})
    movie_df = movie_df[movie_df.index != movie_id].sort_values(by = 'cosine_similarity', ascending=False)

    no_of_rating_for_both_movies = [sum((movie_matrix[movie_id] > 0) & (movie_matrix[movie_id])) for movie_ids in movie_df.index]
    movie_df['common_movie_raters'] = no_of_rating_for_both_movies 
    results = movie_df[movie_df['common_movie_raters']>=5].reset_index()\
                .merge(movie_ratings, how='inner', on ='movieId')\
                .groupby(['movieId','title']).agg({'rating':'mean', 'common_movie_raters' : 'mean'}).reset_index()\
                .sort_values('rating', ascending=False).head(25).merge(df, how = 'inner', on = 'title')

    results['rating'] = round(results['rating'], 1)
    return results[['title','rating', 'Poster']].head(5)

# Recommendation for users based ont heir user id

def get_recommendation(model, user_id, movie_ids, n=7):
    
    user_recommendations = []
    
    for movie_id in movie_ids:
        
        _, _, _, est, _ = model.predict(user_id, movie_id)
        
        user_recommendations.append((movie_id, est))
        
    recommendations = sorted(user_recommendations, key = lambda x : x[1], reverse = True)
    
    top_recommendations = pd.DataFrame(recommendations[:n], columns= ['movieId', 'est_rating'])
    
    reduced_rating_df = movie_ratings.drop_duplicates(subset='movieId').copy()
    
    top_recommendations = top_recommendations.merge(reduced_rating_df, on = 'movieId', how = 'inner')
    
    return top_recommendations[['movieId', 'title']].merge(df, how='inner', on='title').head(5)
        
        






def app_interaction():
    st.title('Welcome to SMG Movies')

    with st.expander('Search details'):
        user = st.number_input('Please enter your membership number', value =1)

        option = st.selectbox(
        'Please choose a movie that you like',
            movie_ratings['title'].sort_values().unique())
    st.text('')
    
    
    # Call your top_rated_movies function
    top_movies = top_rated_movies().head(5)

    
    unrated_movies = movie_ratings[~movie_ratings['movieId'].isin(movie_ratings[movie_ratings['userId']==user])]['movieId'].unique()
    
    unwatched_movies = get_recommendation(movie_model, user, unrated_movies, 10)
    
            
    st.subheader(f"Because you liked {option}, you might also like...")
    
    if option:
        
        movie_rec = related_movies(option)
        
        if not movie_rec.empty:

            columns = st.columns(len(movie_rec))
            for index, row in movie_rec.iterrows():
                
                with columns[index]:
                    st.image(row['Poster'], caption=row['title'], width=None, use_column_width='auto')

        else:
            st.warning(f"No related movies found for {option}.")

    st.subheader("Top Movies today")
    if not top_movies.empty:
      
        columns = st.columns(len(top_movies)) #st.columns(len(top_movies))
        
        for index, row in top_movies.iterrows():
            with columns[index]:
                st.image(row['Poster'], caption=row['title'], width=None, use_column_width='auto') #row['title']

    else:
        st.warning("No top-rated movies found.")
        
    st.subheader(f"Top Picks for User{user}")
    if not unwatched_movies.empty:
        columns = st.columns(len(unwatched_movies))
        for index, row in unwatched_movies.iterrows():
            with columns[index]:
                st.image(row['Poster'], caption=row['title'], width=None, use_column_width='auto')
    else:
        st.warning('Select a movie to enjoy from the trending movies')
        
    
        
    

st.text("")
#st.write('You selected:', option)




if __name__ == "__main__":
   
    app_interaction()


# Add a footer to your app
st.markdown('------')
st.write("Built with Streamlit by Sebastian, Mirella and Grace")

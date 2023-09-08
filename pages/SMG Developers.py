import streamlit as st
st.set_page_config(page_title='SMG Movies', page_icon ="🎬", layout="wide", initial_sidebar_state="collapsed")
st.title('Meet the Creators of SGM Movies')



col1, col2, col3 = st.columns(3)

with col1:
   st.header("Sebastian")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/raw/main/data/seba.png", format ='image/png')
   st.write('''
   Sebastian is a valuable member of the team who contributes greatly to work culture. He is positive and brings this to every project and meeting. His journey into the world of data science is a unique one, having embarked on this path later in life after a successful career running businesses. This background has given Sebastian an all-round business acumen, allowing him to possess an in-depth  understanding of how businesses operate from the ground up.
His ability to bridge different departments and manage collaborations with contractors is a testament to his exceptional leadership and teamwork skills. He seamlessly integrates the data science domain with various aspects of business operations, ensuring that projects align with overarching business goals.
Sebastian strength lies with his knack for visualising and presenting data. Transforming complex datasets into clear, insightful visual representations. Whether it's through graphs, charts, or interactive dashboards, He is comfortable conveying the story hidden within the data and most importantly making it accessible and actionable for all stakeholders. The art of communication and interpretation of data is paramount and Sebastian excels in this skill which takes second place to code and other technical skills.''') 


with col2:
   st.header("Mirella")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/raw/main/data/mire.png", format ='image/png')

with col3:
   st.header("Grace")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/raw/main/data/grace.png", format ='image/png')

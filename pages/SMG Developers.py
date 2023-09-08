import streamlit as st
st.set_page_config(page_title='SMG Movies', page_icon ="🎬", layout="wide", initial_sidebar_state="collapsed")
st.title('Meet the Creators of SGM Movies')



col1, col2, col3 = st.columns(3)

with col1:
   st.header("Sebastian")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/blob/main/data/seba.png")#, output_format ='png')
   st.write('''
   Sebastian is a Junior Data Analyst and a valuable member of the team who contributes greatly to work culture. He is positive and brings this to every project and meeting. His journey into the world of data science is a unique one, having embarked on this path later in life after a successful career running businesses. This background has given Sebastian an all-round business acumen, allowing him to possess an in-depth  understanding of how businesses operate from the ground up.
His ability to bridge different departments and manage collaborations with contractors is a testament to his exceptional leadership and teamwork skills. He seamlessly integrates the data science domain with various aspects of business operations, ensuring that projects align with overarching business goals.
Sebastian strength lies with his knack for visualising and presenting data. Transforming complex datasets into clear, insightful visual representations. Whether it's through graphs, charts, or interactive dashboards, He is comfortable conveying the story hidden within the data and most importantly making it accessible and actionable for all stakeholders. The art of communication and interpretation of data is paramount and Sebastian excels in this skill which takes second place to code and other technical skills.''') 


with col2:
   st.header("Mirella")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/blob/main/data/mire.png")#, format ='image/png')
   st.write('''
   Mirella is our junior Data Analyst who started her career as an Executive Personal Assistant. She worked in tandem with some of the best CEOs in Germany. It was in this world she harnessed her remarkable organisational & analytical skills. This grounding has made her excellent in spotting and uncovering valuable insights in data sets. Her attention to detail allowed her to see anomalies and discrepancies within the data that go unnoticed by others.
Mirella's critical thinking enables her to delve deeper into the data, constantly asking probing questions to understand the underlying trends and correlations. Using her research skills she effortlessly gathers additional domain context from the ever complex and comprehensive ‘internet of things’. In her role, Mirella's passion for seeking answers and her unwavering dedication to precision makes her an invaluable asset. She also brings and gentleness and kindness in the way she interacts with others, that creates a calming atmosphere even in the most stressful times.''')


with col3:
   st.header("Grace")
   st.image("https://github.com/gracious136/Movie-Recommendation-App/blob/main/data/grace.png")#, format ='image/png')
   st.write('''
   Grace, our Senior Data Scientist is a true expert all aspects of the field. Her coding speed is nothing short of astonishing. When faced with new challenges, she exhibited a remarkable ability to not just pick them up quickly but also grapple with them in a way that left others inspired. Grace thrived in the dynamic world of data, her mind agile and adaptable, always ready to embrace the next big puzzle.
What really set Grace apart is her selflessness and willingness to bring the whole team along with her. This is innate ability and the motivation for which, is not the success of the project alone Whenever someone in the team needed assistance, she would step in with unwavering patience and a genuine desire to ensure they understood. Grace had a unique talent for explaining complex concepts thoroughly and repeatedly, using different angles and analogies until those concepts became crystal clear for her peers.
Grace's impact importantly extended beyond her technical expertise. She is the team's motivator always keeping everyone on track. Late nights at the office were routine, as she tirelessly pursued perfection in her work. In the world of data science, Grace is not just a Senior Data Scientist; she is a guiding star at the heart of the team's success.''')

   

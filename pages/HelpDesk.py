import openai
import streamlit as st
st.set_page_config(page_title='SMG Movies', page_icon ="🎬", layout="centered", initial_sidebar_state="collapsed")

st.title("SMG HelpDesk")

openai.api_key = "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"
st.chat_message("user", avatar = "😎").markdown("Welcome to SMG Movies, I am SeGreLa. How can i help you today?")

responses = {
    "What is your name?": "I am SeGreLa, your movie recommendation assistant.",
    "hi": "Hi, i am SeGreLa, your movie recommendation assistant.",
    "hey": "Hi, i am SeGreLa, your movie recommendation assistant.",
    "hello": "Hi, i am SeGreLa, your movie recommendation assistant.",
    "what is your name?": "I am SeGreLa, your movie recommendation assistant.",
    "what is your name": "I am SeGreLa, your movie recommendation assistant.",
    "How does the recommendation work?": "I use a sophisticated algorithm to analyze your preferences and suggest movies that you might like. All you need to do i select a movie that you liked from our list and we will recommend movies that we think you will enjoy.",
    "How do i get a membership number" : "When you sign up with SMG, you will be assigned a memebership number that will be used to tailor personalized recommendations just for you"
}

if "messages" not in st.session_state:
    st.session_state.messages = []

    
# Display chat messages from the chat history when the app is re-run
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# React to user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


    # Check if there is a saved response for the user input
    if prompt in responses:
        response = responses[prompt]
    else:
        # If no saved response, generate a default response
        response = "I'm sorry, I don't have a specific response for that."

    # Display assistant response in chat message container
    with st.chat_message("user", avatar="😎"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat history
if st.button("Clear Chat"):
    st.session_state.messages = []
    
    
    

 

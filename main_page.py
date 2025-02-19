import streamlit as st
import brain
import random

def main():
    st.set_page_config(page_title="AyurBot", layout="wide")
    
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if st.session_state.page == "home":
        display_home()
    elif st.session_state.page == "chat":
        ayurbot()

def display_home():
    page_bg = """
    <style>
    .body {
        background-image : url("https://wallpaperaccess.com/full/432582.jpg");
        background-size : cover;
        background-repeat: no-repeat;
        color : white;
        height : 100vh;
        text-align: center;
    }
    h1 { font-size : 100px; font-family : "Comic Sans MS"; }
    .getStartedButton {
        background-color : transparent;
        color : white;
        border-color :rgb(0, 158, 0);
        margin-top : 20px;
        border-width : 2px;
        border-radius : 20px;
    }
    .getStartedButton:hover {
        background-color : rgb(0, 158, 0);
        color : white;
    }
    </style>
    """
    
    st.markdown(page_bg, unsafe_allow_html=True)
    st.markdown("""<h1>AyurBot</h1><p>Discover your Prakriti using an AI-based chatbot.</p>""", unsafe_allow_html=True)
    if st.button("Get Started", key="start_chat", help="Click to start the chat"):
        st.session_state.page = "chat"
        st.experimental_rerun()

def ayurbot():
    st.markdown("""<h2 style='text-align: center;'>AyurBot Chat</h2>""", unsafe_allow_html=True)
    st.write("Hi there! Let's determine your Prakriti. Answer these questions as accurately as possible.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Send a message"):
        st.session_state.messages.append({"role": "USER", "content": prompt})
        with st.chat_message("USER"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = get_bot_response(prompt.lower())
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(response)

def get_bot_response(user_input):
    if user_input in brain.c_hi:
        return "Please answer the following questions honestly and accurately."
    elif user_input in brain.c_yes:
        return random.choice(brain.questions)
    else:
        return "I didn't quite get that. Could you please answer the question?"

if __name__ == "__main__":
    main()

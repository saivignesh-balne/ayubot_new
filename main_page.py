import streamlit as st
import brain
import random

home = False
count=0

def ayurbot():
    global count
    questions =False
    a=0
    b=0
    c=0
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: ;
    background-size: cover;
    }        
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style="text-align: center; color: #FFFFF7; font-family: 'Times New Roman';">AYURBOT</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    st.markdown(
        """
        <h5 style="color: #FFFFF7;">Hi there! I am Chatbot specific to determine the Prakriti of an individual. So now lets determine your Prakriti!</h5>
        """,
        unsafe_allow_html=True
    )
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Send a message"):
        st.session_state.messages.append({"role":"USER","content": prompt})
        with st.chat_message("USER"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            bot_response=""
            prompt = prompt.lower()

            if count==0:
               bot_response = random.choice(brain.questions)
            if count ==1:
               bot_response = brain.questions[1]
            if prompt in brain.c_hi:
                bot_response = "Please answer the following questions honestly and accurately."    
            if prompt in brain.c_yes:
                questions = True
            count+=1

            logic(prompt,a,b,c)
        
            message_placeholder.markdown(bot_response)
        st.session_state.messages.append({"role": "assistant","content": bot_response})
        

def result(a,b,c):
    if a>b and a>c:
        bot_response = "Congratulations your prakriti is VATA"
    if b>c and b>a:
        bot_response = "Congratulations your prakriti is PiTTA"
    if c>a and c>b:
        bot_response = "Congratulations your prakriti is KAPHA"

def logic(user,x,y,z):
    if user in brain.ans_1:
        x+=1
    elif user in brain.ans_2:
        y+=2
    else:
        z+=3
    return user,x,y,z
def main():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url(https://images.pexels.com/photos/66997/pexels-photo-66997.jpeg?cs=srgb&dl=pexels-no-name-66997.jpg&fm=jpg);
    height = 50%;
    background-position: center;
    background-size: cover;
    }
    </style>
    """
    st.markdown(
        page_bg,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 style="text-align: center; color: black; font-family: 'Times New Roman', sans-serif;">PRAKRITI</h1>
        """,
        unsafe_allow_html=True
    )
    st.subheader('', divider='rainbow')
    st.markdown(
        """
        <h5 style="color: black;">It is a term used in traditional Indian philosophy, particularly in Ayurveda, to describe the inherent constitution or nature of an individual.</h5>
        <h5 style="color: black;">In Ayurveda, it is believed that every person has a unique combination of three fundamental energies or doshas known as VATA, PITTA and KAPHA, which make up their Prakriti.</h5>
        <h5 style="color: black;">These doshas represent different combinationof five elements (Earth, Water, Fire, Air and Ether) and play physical and physcological characteristics as well as their susceptibility to certain health issues.</h5>
        
        """,
        unsafe_allow_html=True
    )
   
col1,col2,col3 = st.columns([1,1,5])
with col1:
    if st.button("HOME"):
        st.session_state.page = 'home'
with col2:
    if st.button("AYURBOT"):
        st.session_state.page = 'ayurbot'
    
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    main()

if st.session_state.page == 'ayurbot':
    home = True
    ayurbot()

"""
# features---
    1. A sidebar with new_chat button and buttons to view older chats
    2. A chatbot

"""

import streamlit as st  
# provide UI
from langchain_core.prompts import ChatPromptTemplate
# to prepare prompt from user input
from langchain_core.output_parsers import StrOutputParser
# present the output from llm to user
from langchain_community.llms import Ollama
# load the model
import os

st.set_page_config(initial_sidebar_state="expanded")

# This ensures it runs on any machine (Windows, Mac, Linux) without FileNotFoundError
database_path = os.path.join("nlp", "elevance_skills", "chats_database")
os.makedirs(database_path, exist_ok=True)

if "show_chat_status" not in st.session_state:
    st.session_state.show_chat_status = False

if "new_chat_status" not in st.session_state:
    # to ensure that operations are only done after we have created a new chat
    st.session_state.new_chat_status = False

if "active_file_path" not in st.session_state:
    st.session_state.active_file_path = ""


def new_chat_function(chat_name = "new_chat"):
    """ To define the functionalities for new chat creation"""

    file_path = os.path.join(database_path, chat_name)
    st.session_state.active_file_path = file_path
        # to keep track of current active file

    if not os.path.exists(file_path):
        with open(file_path,'w',encoding="utf-8") as chat_file:
            chat_file.write("")
        st.session_state.new_chat_status = True
    else:
        st.error("Sorry, already a file with same name exists!!!!!!!")

    load_chat(st.session_state.active_file_path)



def load_chat(chat_path):
    """ to load data from old chats"""
    st.session_state.new_chat_status = True
    st.session_state.active_file_path = chat_path
    # so that further operations are inside this chat only
    st.session_state.chat = {}

    with open(st.session_state.active_file_path,'r',encoding="utf-8") as chat:
        messsages = chat.read().split(" end_of_message")
        # bcs after splitting with end_of_message, we get an empty string too and this slicing is done to remove that empty string
    if len(messsages) > 1 :
        for message in messsages: 
            # 3. SAFETY CHECK: Ensure the split actually yields exactly two items before unpacking
            if " query_answer_joint " in message:
                query,response = message.split(" query_answer_joint ")

                # bcs the message will be in format--- "query query_answer_joint response"
                st.session_state.chat[query] = response

def show_chat():
    """ to display the chat """
    for query,response in st.session_state.chat.items():
        with st.chat_message("human",avatar="👶"):
            st.write(query)

        with st.chat_message("assistant",avatar="🌐"):
            st.write(response)



#------------------------- UI creation-----------------------
st.title("Local Memory Chatbot")
st.subheader("How may I help you ?")
# Dynamic Subheader
# if st.session_state.active_file_path:
#     # Extracts just the file name from the long path
#     active_chat_name = os.path.basename(st.session_state.active_file_path)
#     st.subheader(f"Currently chatting in: {active_chat_name}")

with st.sidebar:

    with st.popover(label="New Chat"):
        # Store the input in a standard variable
        chat_name_input = st.text_input(label="chat name", placeholder="please enter chat name")
        
        # Add a button to act as a gatekeeper. 
        # It will only evaluate to True at the exact moment it is clicked.
        if st.button("Create Chat"):
            if chat_name_input:
                new_chat_function(chat_name_input)


    if os.path.exists(database_path):
        older_chats = os.listdir(database_path)
        st.write("---------------------------")
        st.write("Older chats")
        st.write("---------------------------")
        for chat in older_chats:
            # Highlight logic for the active chat button
            is_active = False
            if st.session_state.active_file_path:
                is_active = st.session_state.active_file_path.endswith(chat)
            
            # Use Streamlit's "primary" color for active, "secondary" for inactive
            btn_type = "primary" if is_active else "secondary"
            
            # use_container_width makes the buttons stretch nicely across the sidebar
            if st.button(chat, type=btn_type, use_container_width=True):
                chat_path = os.path.join(database_path, chat)
                load_chat(chat_path)
                st.session_state.show_chat_status = True
                st.rerun()


if st.session_state.show_chat_status == True:
    show_chat()    
    # defined the condition here so that the chat is on the main screen, not on the sidebar   


#--------------------- collect user input--------------------------------
if st.session_state.new_chat_status:
    # execute only if we have entered into a chat
    query = st.chat_input("What's on your Mind ? ")
    if query:
        with st.chat_message("human",avatar="👶"):
            st.write(query)
        prompt = ChatPromptTemplate( ("user","question:{query}" ) )


        # loading model and generating replies
        output_parser = StrOutputParser()
        llm = Ollama(model='llama3')
        chain = prompt | llm | output_parser
        output = chain.invoke({"query": query})
        
        # we need to use session to manage the history bcs everytime user hits enter, the whole scrit runs from top to bottom

        if "chat" in st.session_state:
            st.session_state.chat[query] = output
        else:
            st.session_state.chat = {}
            st.session_state.chat[query] = output

        with st.chat_message("AI",avatar="🌐"):
            st.write(output)  

        
        # 2. Save the chat to whichever file is currently active
        if st.session_state.active_file_path:
            with open(st.session_state.active_file_path,'a',encoding="utf-8") as file:
                # I added 'end_of_turn_pair' so you can actually separate the turns when reading the file later!
                file.write(f"{query} query_answer_joint {output} end_of_message")



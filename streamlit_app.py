import streamlit as st
from utils_solution import ChatAgent
import time



# This is a simple application of streamlit that shows how to use the Aleph Alpha API to create a conversational AI that answers questions.

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "agent" not in st.session_state:
    st.session_state.agent = ChatAgent(user_name="user", agent_name="assistant")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = st.session_state.agent.chat(prompt)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="AI Agent Demo", page_icon="🤖")
st.title("AI Agent Chat")

# Backend API URL
API_URL = "http://localhost:8011/chat"

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Send request to FastAPI backend
        response = requests.post(API_URL, json={"message": prompt})
        response.raise_for_status()

        # Extract the agent's response from the JSON
        # Assuming the backend returns {"response": "..."}
        data = response.json()
        full_response = data.get("response", "I'm sorry, I couldn't process that request.")

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(full_response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend. Please ensure the FastAPI server is running at http://localhost:8010")
    except requests.exceptions.HTTPError as e:
        st.error(f"API Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

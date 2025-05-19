import streamlit as st
from gpt_client import chat_with_gpt
from conversation import ConversationManager
from conversation_storage import ConversationStorage
from config import DEFAULT_MODEL, get_available_models
import uuid

# Set page config must be the first Streamlit command
st.set_page_config(page_title="ChatGPT Wrapper", layout="wide")

# Initialize storage
storage = ConversationStorage()

# Initialize session state
if "manager" not in st.session_state:
    st.session_state.manager = ConversationManager()
if "available_models" not in st.session_state:
    st.session_state.available_models = get_available_models()
if "selected_model" not in st.session_state:
    st.session_state.selected_model = DEFAULT_MODEL
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Sidebar for conversation management
with st.sidebar:
    st.title("Conversations")
    
    # Search box
    search_query = st.text_input("Search conversations", key="search_query")
    
    # List conversations
    conversations = storage.list_conversations()
    if search_query:
        conversations = [c for c in conversations if search_query.lower() in c["title"].lower()]
    
    # New conversation button
    if st.button("New Conversation"):
        st.session_state.manager.reset()
        st.rerun()
    
    # Display conversation list
    for conv in conversations:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(conv["title"], key=f"conv_{conv['id']}"):
                loaded_conv = storage.load_conversation(conv["id"])
                st.session_state.manager = ConversationManager(conv["id"])
                st.session_state.manager.messages = loaded_conv["messages"]
                st.session_state.manager.title = loaded_conv["title"]
                st.rerun()
        with col2:
            if st.button("🗑️", key=f"del_{conv['id']}"):
                storage.delete_conversation(conv["id"])
                st.rerun()

# Main chat interface
st.title("ChatGPT Streamlit Chatbot")

# Model selection
selected_model = st.selectbox(
    "Select Model",
    st.session_state.available_models,
    index=st.session_state.available_models.index(DEFAULT_MODEL) if DEFAULT_MODEL in st.session_state.available_models else 0
)

# Display model capabilities
st.caption(f"Selected model: {selected_model}")

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    try:
        st.session_state.manager.add_user_message(user_input)
        assistant_reply = chat_with_gpt(
            st.session_state.manager.get_conversation(),
            model=selected_model
        )
        st.session_state.manager.add_assistant_message(assistant_reply)
        
        # Save conversation after each exchange
        storage.save_conversation(
            st.session_state.manager.conversation_id,
            st.session_state.manager.messages,
            st.session_state.manager.title
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display conversation
for msg in st.session_state.manager.get_conversation()[1:]:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")

if st.button("Reset Conversation"):
    st.session_state.manager.reset()
    st.rerun()

# Add a refresh models button
if st.button("Refresh Available Models"):
    st.session_state.available_models = get_available_models()
    st.rerun()

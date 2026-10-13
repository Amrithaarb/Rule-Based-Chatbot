
import streamlit as st

from chatbot import get_response
from chat_storage import (
    init_db,
    create_conversation,
    list_conversations,
    get_messages,
    save_message,
    update_title,
    clear_messages,
)

st.set_page_config(
    page_title=" Rule-Based Chatbot",
    page_icon="💬",
    layout="wide",
)

init_db()


# -------------------- SESSION STATE --------------------

if "active_conversation_id" not in st.session_state:
    conversations = list_conversations()

    if conversations:
        st.session_state.active_conversation_id = conversations[0]["id"]
    else:
        st.session_state.active_conversation_id = create_conversation()

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


def queue_question(category, question):
    """Remember the selected question and keep its category expanded."""
    st.session_state.selected_category = category
    st.session_state.pending_prompt = question


# -------------------- SUGGESTED QUESTIONS --------------------

categories = {
    "Everyday Life": [
        "How can I save water?",
        "How can I save electricity?",
        "How can I stay organized?",
        "What should I eat for breakfast?",
        "Why is sleep important?",
        "How can I reduce stress?",
        "How can I improve my English?",
        "How can I manage my time?",
        "What should I carry when travelling?",
        "How can I save money?",
        "What should I do when I feel bored?",
        "How can I stay healthy?",
        "How can I be more productive?",
        "How can I protect my phone?",
    ],
    "Education & Technology": [
        "What is Python?",
        "What is artificial intelligence?",
        "What is machine learning?",
        "What is deep learning?",
        "What is data science?",
        "What is cybersecurity?",
        "What is SQL?",
        "What is cloud computing?",
        "What is an algorithm?",
        "What is a database?",
        "What is the internet?",
    ],
    "General Knowledge": [
        "What is gravity?",
        "What is photosynthesis?",
        "What is the solar system?",
        "What is the largest planet?",
        "Why is the sky blue?",
        "What is renewable energy?",
        "How many planets are in the solar system?",
        "What direction does the sun rise?",
        "How many months are there in a year?",
        "What day is it today?",
    ],
    "Entertainment": [
        "What are some best genres in movies?",
        "What is the best cartoon to improve English?",
        "Which music is best for relaxation?",
        "What is a good movie for family?",
        "What music is good for studying?",
    ],
    "Programming": [
        "What is Java?",
        "What is SQL?",
        "What is HTML?",
        "What is a computer network?",
        "What is an operating system?",
    ],
    "Basic Mathematics": [
        "What is 25 + 37?",
        "What is 50 - 18?",
        "What is 12 * 8?",
        "What is 100 / 4?",
    ],
}


# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.title("💬Rule-Based Chatbot")

    if st.button("➕ New conversation", use_container_width=True):
        st.session_state.active_conversation_id = create_conversation()
        st.session_state.selected_category = None
        st.session_state.pending_prompt = None
        st.rerun()

    st.divider()
    st.subheader("📚 Try asking")

    for category, questions in categories.items():
        with st.expander(
            category,
            expanded=(st.session_state.selected_category == category),
        ):
            for index, question in enumerate(questions):
                st.button(
                    question,
                    key=f"question_{category}_{index}",
                    use_container_width=True,
                    on_click=queue_question,
                    args=(category, question),
                )

    st.divider()
    st.subheader("🕘 Conversation history")

    conversations = list_conversations()

    if conversations:
        conversation_ids = [c["id"] for c in conversations]
        conversation_titles = {
            c["id"]: c["title"] for c in conversations
        }

        active_id = st.session_state.active_conversation_id

        if active_id not in conversation_ids:
            active_id = conversation_ids[0]
            st.session_state.active_conversation_id = active_id

        selected_id = st.selectbox(
            "Choose a conversation",
            options=conversation_ids,
            index=conversation_ids.index(active_id),
            format_func=lambda cid: conversation_titles.get(
                cid, "New conversation"
            ),
            label_visibility="collapsed",
        )

        st.session_state.active_conversation_id = selected_id

        if st.button("🗑️ Clear current conversation", use_container_width=True):
            clear_messages(selected_id)
            st.session_state.pending_prompt = None
            st.rerun()


# -------------------- PROCESS USER INPUT --------------------

conversation_id = st.session_state.active_conversation_id

typed_prompt = st.chat_input("Type your message here...")

# Suggested questions take priority when clicked.
prompt = st.session_state.pending_prompt
st.session_state.pending_prompt = None

if not prompt:
    prompt = typed_prompt

if prompt:
    # Give a new conversation a title based on its first message.
    if not get_messages(conversation_id):
        update_title(conversation_id, prompt)

    save_message(conversation_id, "user", prompt)

    response = get_response(prompt)
    save_message(conversation_id, "assistant", response)


# -------------------- MAIN CHAT WINDOW --------------------

st.title("💬 Rule-Based Chatbot")
st.caption("Your simple assistant for everyday questions, technology, and more.")

messages = get_messages(conversation_id)

if not messages:
    st.info(
        "Hello! 👋 Choose a suggested question from the sidebar "
        "or type your own question below to get started."
    )

for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

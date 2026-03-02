import streamlit as st
import time

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------------- Custom Styling ----------------
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a, #1e293b);
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: white;
            margin-bottom: 10px;
        }
        .sub-text {
            text-align: center;
            color: #cbd5e1;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 Smart AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Responsive • Modern • Clean UI</div>', unsafe_allow_html=True)

# ---------------- Session Memory ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Display Chat History ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Bot Logic ----------------
def generate_response(prompt):
    prompt = prompt.lower()
    
    if "hello" in prompt:
        return "Hey Adhil 👋 How can I help you today?"
    elif "project" in prompt:
        return "Are you working on ML deployment or your potato leaf disease project? 🌱"
    elif "streamlit" in prompt:
        return "Streamlit is great for ML app deployment 🚀"
    else:
        return f"I understand you said: **{prompt}**"

# ---------------- Chat Input ----------------
if user_input := st.chat_input("Type your message..."):

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Simulate typing effect
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)
            response = generate_response(user_input)
            st.markdown(response)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
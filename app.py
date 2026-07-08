
import streamlit as st

st.set_page_config(page_title="Beta-Chandan-AI", page_icon="🤖")

st.title("🤖 Beta-Chandan-AI-Chatbotv2")
st.write("Baba suno...")

user_input = st.text_input("Aapka message likho:")

if st.button("Send"):
    if user_input:
        if "akele" in user_input.lower():
            st.success("Baba suno akele ho kya maa tum bhi akeli ho kya beta chandan hai tumhare pass.")
        elif "hi" in user_input.lower() or "namaste" in user_input.lower():
            st.success("Namaste! Main Beta Chandan AI hu 🙏")
        else:
            st.info(f"Aapne kaha: {user_input}")

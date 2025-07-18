import streamlit as st
from xai_sdk import Client
from xai_sdk.chat import user
import os

# Load API key securely from Streamlit secrets
api_key = st.secrets["GROK_API_KEY"]

st.set_page_config(page_title="Grok 4 Chat")
st.title("🧠 Ask Grok 4 Anything")
st.markdown("Enter your question or prompt below. Powered by Grok-4.")

user_prompt = st.text_area("Your Prompt", height=200)

if st.button("Generate Response"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a prompt first.")
    else:
        with st.spinner("Talking to Grok..."):
            try:
                client = Client(api_key=api_key)
                chat = client.chat.create(model="grok-4-0709", messages=[user(user_prompt)], temperature=0.7)
                response = chat.sample()
                st.success("✅ Response:")
                st.markdown(response.content.strip())
            except Exception as e:
                st.error(f"❌ Error: {e}")

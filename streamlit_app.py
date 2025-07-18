import streamlit as st
from xai_sdk import Client
from xai_sdk.chat import user

st.title("🔮 Grok 4 Chatbot")
st.markdown("Ask anything, powered by **Grok 4**")

prompt = st.text_area("Your prompt", height=200)
submit = st.button("Ask")

if submit and prompt.strip():
    with st.spinner("Thinking..."):
        client = Client(api_key=st.secrets["GROK_API_KEY"])
        chat = client.chat.create(
            model="grok-4-0709",
            messages=[user(prompt)],
            temperature=0.7,
        )
        response = chat.sample().content
        st.markdown("### Response:")
        st.markdown(response)

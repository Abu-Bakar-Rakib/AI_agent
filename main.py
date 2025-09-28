import streamlit as st
from langchain_groq import ChatGroq

# Set up the Streamlit app
st.set_page_config(page_title="AI Agent", page_icon="🤖")
st.title("🤖 AI Agent - Powered by LLaMA 3.1 (Groq)")

# Ask for API key (better security than hardcoding)
api_key = st.text_input("Enter your Groq API Key:", type="password")

if api_key:
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)

    # Chat input from user
    user_input = st.text_area("💬 Ask me anything:")

    if st.button("Generate Response"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                response = llm.invoke(user_input)
                st.success(response.content)
        else:
            st.warning("Please enter a question.")
else:
    st.info("🔑 Please enter your Groq API key to continue.")


# llm = ChatOpenAI(model = "gpt-4o-mini",api_key="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")
# # llm2 = ChatAnthropic(model= "claude-3-5-sonnet-20241022")
# response = llm.invoke("what is the meaning of life?")
# print(response)
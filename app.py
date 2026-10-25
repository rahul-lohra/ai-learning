import streamlit as st

st.set_page_config(page_title="AI Learning Lab", page_icon="🧠")

st.title("🧠 My AI Learning Lab")
st.write("Experimenting with RAG, embeddings and LLMs")

question = st.text_input("Ask a question")
if st.button("Search"):
    if question.strip():
        st.success(f"Your question: {question}")
    else:
        st.info("Enter a question to search.")

st.caption("Demo: this echoes your question. Connect a RAG chain to search documents.")

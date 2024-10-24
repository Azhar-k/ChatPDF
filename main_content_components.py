import streamlit as st
from langchain.schema import Document
from vector_store_utils import get_relevant_context
from chain_utils import create_chain

def display_file_info():
    if st.session_state.displayed_file_name:
        st.write(f"Processed file: {st.session_state.displayed_file_name}")

def handle_user_question():
    chain = create_chain()

    # Use a unique key for the text input
    input_key = f"question_input_{st.session_state.get('question_count', 0)}"
    
    user_question = st.text_input("Ask a question about the PDF:", key=input_key)
    
    if user_question:
        relevant_context = get_relevant_context(st.session_state.vector_store, user_question)
        doc = Document(page_content=relevant_context, metadata={})

        response = chain.invoke({
            "input_documents": [doc],
            "question": user_question
        })

        st.session_state.user_question = user_question
        st.session_state.answer = response["output_text"]
        
        # Increment the question count to generate a new key for the next input
        st.session_state.question_count = st.session_state.get('question_count', 0) + 1
        
        # Rerun the app to display the answer and clear the input
        st.rerun()

def display_answer():
    if st.session_state.user_question and st.session_state.answer:
        st.write("Your question:", st.session_state.user_question)
        st.write("Answer:", st.session_state.answer)

def main_content():
    if st.session_state.file_processed:
        display_file_info()
        handle_user_question()
        display_answer()

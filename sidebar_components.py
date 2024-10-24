import streamlit as st
from pdf_utils import read_pdf, split_text
from vector_store_utils import save_to_vector_store
from state_management import clear_app_state

def handle_file_upload():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", 
                                     key=f"uploader_{st.session_state.uploader_key}",
                                     disabled=st.session_state.uploader_disabled)

    if uploaded_file is not None and not st.session_state.file_processed:
        st.session_state.uploaded_file = uploaded_file
        st.session_state.displayed_file_name = uploaded_file.name
        
        text = read_pdf(uploaded_file)
        chunks = split_text(text)

        if not chunks:
            st.error("Failed to extract text from the PDF. Please try another file.")
        else:
            st.session_state.vector_store = save_to_vector_store(chunks)

            if st.session_state.vector_store is None:
                st.error("Failed to create vector store. Please try again or use a different PDF.")
            else:
                st.session_state.file_processed = True
                st.session_state.show_success_message = True
                st.session_state.uploader_disabled = True
                st.rerun()  # Rerun to show the success message and disable the uploader

def show_success_message():
    if st.session_state.show_success_message:
        st.success("PDF Processed successfully!")
        st.session_state.show_success_message = False  # Reset the flag

def handle_clear_button():
    if st.session_state.file_processed:
        if st.button("Clear and Upload New File"):
            clear_app_state()
            st.success("App state cleared. You can now upload a new file.")
            st.rerun()

def sidebar_content():
    st.title("PDF Upload")
    handle_file_upload()
    show_success_message()
    handle_clear_button()

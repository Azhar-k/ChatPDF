import streamlit as st
import os
import shutil

def initialize_app_state():
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None
    if 'file_processed' not in st.session_state:
        st.session_state.file_processed = False
    if 'user_question' not in st.session_state:
        st.session_state.user_question = ""
    if 'answer' not in st.session_state:
        st.session_state.answer = ""
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'displayed_file_name' not in st.session_state:
        st.session_state.displayed_file_name = None
    if 'uploader_key' not in st.session_state:
        st.session_state.uploader_key = 0
    if 'show_success_message' not in st.session_state:
        st.session_state.show_success_message = False
    if 'uploader_disabled' not in st.session_state:
        st.session_state.uploader_disabled = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    if 'question_count' not in st.session_state:
        st.session_state.question_count = 0

def clear_app_state():
    if os.path.exists("faiss_index"):
        shutil.rmtree("faiss_index")
    st.session_state.vector_store = None
    st.session_state.file_processed = False
    st.session_state.user_question = ""
    st.session_state.answer = ""
    st.session_state.uploaded_file = None
    st.session_state.displayed_file_name = None
    st.session_state.uploader_key += 1
    st.session_state.show_success_message = False
    st.session_state.uploader_disabled = False
    st.session_state.current_question = ""
    st.session_state.question_count = 0

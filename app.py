import streamlit as st
import os
from dotenv import load_dotenv
import logging
from state_management import initialize_app_state, clear_app_state
from sidebar_components import sidebar_content
from main_content_components import main_content

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    st.title("PDF Question & Answer Bot")
    google_api_key = st.secrets["general"]["GOOGLE_API_KEY"]
    os.environ["GOOGLE_API_KEY"] = google_api_key
    
    with st.sidebar:
        sidebar_content()
    
    main_content()

if __name__ == "__main__":
    initialize_app_state()
    main()

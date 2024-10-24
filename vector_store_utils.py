from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import logging

def save_to_vector_store(text_chunks):
    """
    Convert text chunks to embeddings, create a FAISS vector store,
    and save the text chunks to it.
    """
    if not text_chunks:
        logging.error("No text chunks to process")
        return None

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    try:
        vector_store = FAISS.from_texts(text_chunks, embeddings)
        
        # Save the vector store to disk
        vector_store.save_local("faiss_index")
        
        # Log the number of chunks processed
        logging.info(f"Processed {len(text_chunks)} chunks into the vector store")
        
        return vector_store
    except Exception as e:
        logging.error(f"Error creating vector store: {str(e)}")
        return None

def get_relevant_context(vector_store, question, k=5):
    """
    Retrieve relevant context from the vector store for a given question.
    """
    if not question.strip():
        # If the question is empty, return the first k documents
        docs = list(vector_store.docstore._dict.values())[:k]
    else:
        docs = vector_store.similarity_search(question, k=k)
    
    return "\n".join([doc.page_content for doc in docs])

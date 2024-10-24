from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

def create_chain():
    """
    Create and return a question-answering chain using ChatGoogleGenerativeAI and a custom prompt.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an AI assistant tasked with answering questions about a PDF document. 
        The following text is the relevant content extracted from the PDF:

        {context}

        Using the above context, please answer the following question. If the question asks for a summary, 
        provide a comprehensive summary of the main points in the document. If you can't find the answer 
        in the context, simply state that you don't have enough information to answer the question.

        Question: {question}

        Answer:"""
    )
    
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    return chain


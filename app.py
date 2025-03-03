import os
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("🚆 Indian Railways ChatBot")

# Initialize LLM (Groq's Gemma Model)
llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

# Define the prompt
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only. 
    Provide the most accurate response based on the question. Explain if necessary. 
    <context>
    {context}
    <context>
    Question: {input}
    """
)

# Function to load and embed documents
def vector_embedding():
    if "vectors" not in st.session_state:
        with st.spinner("Loading and embedding documents..."):
            # Load embeddings model
            st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            
            # Load PDFs from "./data" folder
            st.session_state.loader = PyPDFDirectoryLoader("./data")
            st.session_state.docs = st.session_state.loader.load()

            # Split documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            final_documents = text_splitter.split_documents(st.session_state.docs)

            # Convert documents into vector embeddings using FAISS
            st.session_state.vectors = FAISS.from_documents(final_documents, st.session_state.embeddings)

            st.success("Document processing completed! Ready to answer queries.")

# Input field for user question
query = st.text_input("❓ Ask a question related to Indian Railways:")

if st.button("Submit"):
    if query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        # Ensure embeddings are initialized
        vector_embedding()

        # Setup retriever
        retriever = st.session_state.vectors.as_retriever()

        # ✅ Step 1: Create document chain
        document_chain = create_stuff_documents_chain(llm, prompt)

        # ✅ Step 2: Create retrieval chain
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        with st.spinner("Thinking..."):
            start_time = time.process_time()
            response = retrieval_chain.invoke({'input': query})
            elapsed_time = time.process_time() - start_time

        # Display answer
        st.subheader("🤖 Answer:")
        st.write(response.get('answer', "Sorry, I couldn't find an answer."))

        # Display time taken
        st.write(f"⏳ Response generated in {elapsed_time:.2f} seconds.")

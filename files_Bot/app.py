import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import pymongo
import os

load_dotenv()

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["conversations"]
collection = db["chatfiles"]

def save_conversation(conversation, filename):
    conversation_data = {
        "filename": filename,
        "conversation": conversation
    }
    collection.update_one({"filename": filename}, {"$set": conversation_data}, upsert=True)

def load_conversation(filename):
    result = collection.find_one({"filename": filename})
    if result:
        return result["conversation"]
    return []

def reset_session_state():
    if "messages" in st.session_state:
        del st.session_state.messages

def main():
    st.title('Chat with your PDF files💬👩‍💻')
    pdf = None
    selected_file = None

    with st.sidebar:
        pdf = st.file_uploader("Upload pdf:", type='pdf')

    if pdf is None:
        st.warning("Upload your pdf file to start a new conversation.", icon="🚨")
        reset_session_state()

    if pdf is not None:
        store_name = pdf.name[:-4]
        conversation_filename = f"{store_name}_conversation.pkl"

        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        query = st.chat_input("Ask questions about your PDF file:")

        if query is not None:
            with st.chat_message("user", avatar="👩‍💻"):
                st.markdown(query)
            st.session_state.messages.append({"role": "👩‍💻", "content": query})

        if query:
            docs = VectorStore.similarity_search(query=query, k=3)

            llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(response)
            st.session_state.messages.append({"role": "🤖", "content": response})

        save_conversation(st.session_state.messages, conversation_filename)
        
    with st.sidebar.expander("Saved Conversations"):
        conversation_files = collection.find({}, {"filename": 1})
        conversation_files = [f.get("filename", "No filename") for f in conversation_files]
        selected_file = st.selectbox("Select a file:", ["Choose Conversation"] + conversation_files)
    selected_conversation = []
    if selected_file and selected_file != "Choose Conversation":
        selected_conversation = load_conversation(selected_file)
    for message in selected_conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if __name__ == '__main__':
    main()

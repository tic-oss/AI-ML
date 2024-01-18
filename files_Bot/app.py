import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

load_dotenv()

def main():
    st.title('Chat With Your PDF files💬 ')
    pdf=None

    pdf = st.sidebar.file_uploader("Upload your PDF", type='pdf')
    if pdf is None:
        st.warning("Please upload your pdf to start conversation",icon="🚨")
 
    if pdf is not None:
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

        store_name = pdf.name[:-4]
 
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        if "messages" not in st.session_state:
            st.session_state.messages=[]
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        query = st.chat_input("Ask questions about your PDF file:")
        if query is not None:
            with st.chat_message("user",avatar="🧑‍💻"):
                st.markdown(query)
            st.session_state.messages.append({"role":"🧑‍💻","content":query})
 
        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
 
            llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            with st.chat_message("assistant",avatar="🤖"):
                st.markdown(response)
            st.session_state.messages.append({"role":"🤖","content":response})

        conversation_data = {
            "file_name": store_name,
            "conversation": st.session_state.messages.copy(),
        }
 
if __name__ == '__main__':
    main()

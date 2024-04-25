import streamlit as st
import os
import time
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader
import threading
import openai

# Set Streamlit page configuration
st.set_page_config(
    page_title="Documentation Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

# Set OpenAI API key
openai.api_key = st.secrets.openai_key

# Initialize chat header and warning
st.header("Chat with the CanvasToCode docs💬")
st.subheader("Talk to our canvas")
st.warning("Get Back To site 👉 [CanvasTocode](https://tic.comakeit.com/)", icon="🌐")

# Initialize chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "🤖", "content": "Ask me a question on how to get started with CanvasToCode!"}
    ]

# Function to track file updates
def track_file_updates(directory, session_state):
    existing_files = set(os.listdir(directory))
    print(f"Initial files in directory: {existing_files}")
    while True:
        current_files = set(os.listdir(directory))
        new_files = current_files - existing_files
        if new_files:
            print(f"New files detected: {new_files}")
            for file in new_files:
                if file.endswith(".md"):
                    existing_file = file.replace("_v1", "")
                    if existing_file in existing_files:  
                        st.write(f"New file '{file}' with updated data has been added.")
        existing_files = current_files
        time.sleep(10)

# Function to load data
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./docs", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are a assistant for documentation provided. Answer only when user gives a prompt, do not get queries of your own and donot give imaginary answers give only facts."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

# Initialize chat engine
if "chat_engine" not in st.session_state.keys():
    st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

prompt = st.chat_input("Your question")
if prompt:
    st.session_state.messages.append({"role": "🧑🏻‍💻", "content": prompt})

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("🤖"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "🤖", "content": response.response}
            st.session_state.messages.append(message)  # Add response to message history

# Run file tracking in a separate thread
file_tracking_thread = threading.Thread(target=track_file_updates, args=("./docs", st.session_state))
file_tracking_thread.start()

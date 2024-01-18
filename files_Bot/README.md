# ChainLang
 simple chatbot based on LangChain and OpenAI API that can be trained with PDF files.

This chatbot is trained with PDF files which the user uploads.
--------------------------------

### Prerequisites:

* python3
* pip3
* OpenAI API Key
  
--------------------------------

### Get started by following the below steps:

Install required packages:

``` pip3 install -r requirements.txt```

Set OpenAI API Key as an environment variable:

```export OPENAI_API_KEY="--replace--with--api--key--"```

or Add yout Api Token in .env file.

Run the chatbot:
```streamlit run app.py```

Open the url logged on the terminal and upload your file and start asking the questions.

### Saving previous conversations

We can save our previous conversations into the MongoDB. make sure you have MongoDB instance and replace these with your data.
```
client = pymongo.MongoClient("your_mongodb_uri")
db = client["your_database_name"]
collection = db["your_collection_name"]

```


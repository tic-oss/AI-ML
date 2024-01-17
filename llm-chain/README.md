# Llama2 LLM Chain

A simple LLM chain, built using langchain & Llama2 model running locally.

## Setup

Download ollama, a tool for running LLMs locally.
https://github.com/jmorganca/ollama?tab=readme-ov-file

Start Llama2 ``` ollama run llama2 ```

Use the below commands to setup langchain and jupyter notebook

```
pip install langchain

pip install langchain-community

pip install notebook
```

Start notebook locally ``` jupyter notebook ```

Refer to [Sample notebook](notebook.ipynb) for getting started.

## Notes

If you face any errors, try upgrading the required libraries

```
pip install --upgrade langchain

pip install --upgrade notebook
```

## References

https://python.langchain.com/docs/get_started/quickstart

https://github.com/jmorganca/ollama?tab=readme-ov-file

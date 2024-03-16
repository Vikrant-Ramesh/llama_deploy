import os

def get_hf_key():
    return os.environ["HUGGINGFACEHUB_API_TOKEN"]

def get_cohere_key():
    return os.environ["COHERE_API_KEY"]

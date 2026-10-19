from langchain_huggingface import HuggingFaceEmbeddings

embegging = HuggingFaceEmbeddings (model_name="sentence-transformers/all-MiniLM-L12-v2")

text="Delhi is the capital of India"

vector = embegging.embed_query(text)

print(str(vector))
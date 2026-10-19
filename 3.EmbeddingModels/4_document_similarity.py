from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrix.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeding = OpenAIEmbeddings(model="text-embedding-3-large", dimension=300)

documents=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query="Tell me about Virat Kholi"

doc_embeddings = embeding.embed_documents(documents)
query_embedding = embeding.embed_query(query)

print(cosine_similarity([query_embedding], doc_embeddings))

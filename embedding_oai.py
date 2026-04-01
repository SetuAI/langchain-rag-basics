from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)
import os

api_key = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions=100, # output is going to be a 32D vector
    api_key=api_key
)

result = embedding.embed_query("Oracle Corporation is an American multinational computer technology company headquartered in Austin, Texas.")

print(str(result))
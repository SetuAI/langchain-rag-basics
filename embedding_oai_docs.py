from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)
import os

api_key = os.getenv("OPENAI_API_KEY")

embedding = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions=50, # output is going to be a 32D vector
    api_key=api_key
)


result = embedding.embed_documents([
    "Oracle Corporation is an American multinational computer technology company headquartered in Austin, Texas.",
    "Oracle Corporation was founded in 1977 by Larry Ellison, Bob Miner, and Ed Oates.",
    "Oracle Corporation is known for its database software and technology, cloud engineered systems, and enterprise software products.",
    "Oracle Corporation has a strong presence in the enterprise software market."

])

print(str(result))
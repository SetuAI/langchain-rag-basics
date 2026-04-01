'''
chat model : gpt-4o 
establishing a connection between openai api and our code using langchain

'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)
import os

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
    model="gpt-4o",
    max_completion_tokens=None, # max tokens  - setting limit on the output tokens generated
    openai_api_key = api_key
    
)

result = model.invoke("Can you tell me something about Oracle Corporation? ")

print(result.content)
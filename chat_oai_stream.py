from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)
import os

api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(
        model = "gpt-4o",
        max_tokens = None, # None means no upper limit on tokens
        openai_api_key = api_key ,
        streaming = True, # Enable streaming mode
        
    )


print("=" * 40)
# stream tokens as they arrive
for result in model.stream("Can you tell me something about HCL tech  ? "):
    print(result.content,end = "", flush=True)
    
print("=" * 40)
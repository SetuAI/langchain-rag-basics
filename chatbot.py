from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv(override=True)
import os 

'''
langchain : 3 types of messages
System message : system level message you send to AI at the start of conversation 
ex : you are helpful assitant

Human Message : user prompt : human sends to the AI system

AI Message : message that AI replies to human message
'''

model = ChatOpenAI(model="gpt-4o")

# chat history : list of messages exchanged between human and AI
# each time a user inputs a message : it is appended to the chat history
chat_history = [SystemMessage(content="You are a helpful assistant. \
    You ask the most relevant questions and provide them with the information they need")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)
    
print("Chat history .....\n")
print(chat_history)
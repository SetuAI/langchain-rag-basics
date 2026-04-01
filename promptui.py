from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv(override=True)
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# defining the model
model = ChatOpenAI()

# defining the streamlit UI 
st.header("Research Tool")
# which paper does the user want
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
                                                           "BERT: Pre-training of Deep Bidirectional Transformers", 
                                                           "GPT-3: Language Models are Few-Shot Learners", 
                                                           "Diffusion Models Beat GANs on Image Synthesis"] )

# what should be the level of explanation
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", 
                                                         "Technical",
                                                         "Code-Oriented", 
                                                         "Mathematical"] ) 

# what should be the length of explanation
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", 
                                                           "Medium (3-5 paragraphs)",
                                                           "Long (detailed explanation)"] )

# designing the prompt 

template = PromptTemplate(
    template= """
    Please summarize the research paper titled {paper_input} with the following specs: 
    Explanation style : {style_input}
    Explanation_length : {length_input}
    1 : Mathematical details:
    - Include relevant math questions if present in the paper
    - Explain the math concepts using simple, code snippets 
    - Use relatable analogies to simplify complex ideas
    If certain information is not available in the paper, respond with : Insufficient information
    Ensure the summary is clear, accurate and aligned with provided style and length
    """,
    input_variables=['paper_input','style_input','length_input']
)

prompt = template.invoke({
    "paper_input" : paper_input,
    "style_input" : style_input,
    "length_input" : length_input
})

# ui part
if st.button("summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
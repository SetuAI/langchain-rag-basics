

from langchain_core.prompts import PromptTemplate

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

template.save("template.json")
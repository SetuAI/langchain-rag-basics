'''
Document readers : readers/parsers for diff formats
job : read a file and return a list[document]

pypdfloader -> reads pdf
textloader -> read text 
csv loader -> reads csv rows

at this stage, no splitting, no chunking - just raw extraction
a 50 page pdf -> becomes 50 document objects - one per page
page text --> page_content

page_content is what gets vectorized

why chunking is needed? 
embed models have a token limit - text-ada-002 : 512 tokens
you want semantically focussed vectors for precise retrieval

text splitters = chunking tool
will take a list[document objects] and split each document's page_content into 
a smaller list[document objects] chunks

'''
# pip install langchain-text-splitters
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# create a loader object
loader= PyPDFLoader('AI_TrainingPLan.pdf')

# this will create out a set of document objects
docs = loader.load()

# first chunk extracted will be of 100 tokens
# second chunk extracted : 20 tokens from the 1st chunk and 80 new tokens from the 2nd chunk = 100 tokens
# chunk overlap between chunks to preserve context
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)

print("Length of chunks..\n",len(chunks))
print("===================")
# print(chunks)
print(chunks[150].page_content)
print("===================")
print(chunks[0].metadata)
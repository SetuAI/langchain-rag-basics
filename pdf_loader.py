from langchain_community.document_loaders import PyPDFLoader

# create a loader object
loader= PyPDFLoader('AI_TrainingPLan.pdf')

# this will create out a set of document objects
docs = loader.load()

print("list of doc objects....\n", docs)
print("=========================")
print("# of docs created", len(docs))
print("=========================")
print("Extracting the page content from the first document only..",docs[0].page_content)
print("=========================")
print("Extracting the Metadata from the first document only..",docs[0].metadata)
# pip install pypdf

'''
raw file : pdf/txt/csv

loader --> list[document]

text splitter --> chunking

embeddings --> vectors are stored with metadata

'''
#breaks the pdf into pages ke size ka list item--- use when we have text and we want to load this text

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs[0].page_content)
print(docs[1].metadata)
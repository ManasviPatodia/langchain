#length-based text splitting is the easiest but the least used cause the text can be broken in between words, in between meanings, so the embedding generated wouldnt be accurate

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs= loader.load()

text= """hey my name is manasvi im here to see whether this works or not, it is not working working currently but i do hope that this eventually works,because i would like to see it work in front of me"""

splitter= CharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)
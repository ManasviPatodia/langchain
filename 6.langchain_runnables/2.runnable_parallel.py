#ek sath do chiz jayega do chains banega, this is runnable parallel



from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate me a twitter post on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate me a linkedin post on {topic}",
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template="Combine these together for me twitter-> {twitter}, linkedin-> {linkedin}",
    input_variables=['twitter','linkedin']
)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
parser = StrOutputParser()

parallel_chain= RunnableParallel({
    'twitter':prompt1|model|parser,
    'linkedin':prompt2|model|parser
})

merge_chain=prompt3|model|parser

chain=parallel_chain|merge_chain

result= chain.invoke({'topic':'AI'})

print(result['twitter'])
print(result['linkedin'])
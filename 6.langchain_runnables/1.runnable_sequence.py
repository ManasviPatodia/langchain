#ek ke baad dosra chiz jayega, this is runnable sequence


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Now, tell me a funny story about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-pro")

parser = StrOutputParser()

chain= RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'dogs'}))
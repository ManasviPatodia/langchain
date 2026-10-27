#it will just pass, and give the same output as the input

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser= StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain= RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'AI'}))
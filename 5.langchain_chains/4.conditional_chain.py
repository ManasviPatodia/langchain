from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative'] = Field(description='Sentiment of the feedback')

parser2= PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the feedback into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback} \n ",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback} \n ",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='postive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Invalid sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'The product is really good and I am satisfied with the purchase'}))

chain.get_graph().print_ascii()
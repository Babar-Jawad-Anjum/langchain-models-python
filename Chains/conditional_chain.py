from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

text_output_parser = StrOutputParser()

class FeedbackClassification(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

feedback_parser = PydanticOutputParser(pydantic_object=FeedbackClassification)

sentiment_classification_prompt = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction': feedback_parser.get_format_instructions()}
)

positive_feedback_prompt = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

negative_feedback_prompt = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)

sentiment_classifier_chain = sentiment_classification_prompt | llm | feedback_parser

feedback_response_branch = RunnableBranch(
    (lambda x:x.sentiment == 'positive', positive_feedback_prompt | llm | text_output_parser),
    (lambda x:x.sentiment == 'negative', negative_feedback_prompt | llm | text_output_parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

feedback_processing_chain = sentiment_classifier_chain | feedback_response_branch

result = feedback_processing_chain.invoke({'feedback': 'This is good phone'})

print(result)

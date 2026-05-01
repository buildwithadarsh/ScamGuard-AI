from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.schemas.spam_schema import SpamDetectionOutput

from app.utils.files_loader import load_system_prompt

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
llm_model = os.getenv("LLM_MODEL")

# 1. get your LLM
def get_openai_llm() -> ChatOpenAI:
    llm = ChatOpenAI(model = llm_model, api_key=openai_key)
    llm = llm.with_structured_output(SpamDetectionOutput)
    return llm

def get_chat_prompt(email_text) -> ChatPromptTemplate:
    sys_prompt = load_system_prompt()
    chat_prompt= ChatPromptTemplate.from_messages([
                ("system", sys_prompt),
                ("human", "{email_text}")
            ])
    return chat_prompt

def get_chat_prompt2() -> ChatPromptTemplate:
    sys_prompt = load_system_prompt()
    chat_prompt= ChatPromptTemplate.from_messages([
                ("system", sys_prompt),
                ("human", "{email_text}")
            ])
    return chat_prompt




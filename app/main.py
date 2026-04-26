from app.utils.clean_data import pre_process, pre_process_2, post_process
from app.services.llm_service import get_openai_llm, get_chat_prompt, get_chat_prompt2

from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser


email = """Email:
        Congratulation! you have won $5,000,000 in an international lottery.
        Click this link immediately to claim your prize.
        The prize is valid only for next 15 minutes.
    """

# 1. Without Chain 
# cleaned_email = pre_process_2(email)
# chat_prompt = get_chat_prompt2()

# # print(f"system prompt: {chat_prompt}")
# print("Expected variables:", chat_prompt.input_variables)
# formatted_prompt = chat_prompt.format_messages(
#     email_text=cleaned_email
# )
# print("Expected variables:", chat_prompt.input_variables)
# response = get_openai_llm().invoke(formatted_prompt)
# print(f"llm_response: {response}")



# 2. Create the chain
# chat_prompt = get_chat_prompt(cleaned_email)

# chain = RunnableLambda(pre_process)|RunnableLambda(get_chat_prompt)|get_openai_llm()|StrOutputParser()
# print(chain.invoke(email))


# 3. we have introduced the pydantic class to restrict the output format form LLM
chain = RunnableLambda(pre_process)|RunnableLambda(get_chat_prompt)|get_openai_llm()|RunnableLambda(post_process)
print(chain.invoke(email))


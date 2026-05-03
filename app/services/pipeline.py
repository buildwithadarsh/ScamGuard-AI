from langchain_core.runnables import RunnableLambda
from app.utils.clean_data import pre_process
from app.services.llm_service import get_chat_prompt2, get_chat_prompt, get_openai_llm
from app.utils.clean_data import post_process


# scamguard_chain = (
#     RunnableLambda(pre_process)
#     | get_chat_prompt2()
#     | get_openai_llm()
#     | RunnableLambda(post_process)
# )

scamguard_chain = (
    RunnableLambda(pre_process)
    | RunnableLambda(get_chat_prompt)
    | get_openai_llm()
    | RunnableLambda(post_process)
    )

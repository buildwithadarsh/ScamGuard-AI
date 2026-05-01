from spam_schema import SpamDetectionOutput

def llm_with_schema(llm):
    llm_with_schema = llm.with_structured_output(SpamDetectionOutput)
    return llm_with_schema
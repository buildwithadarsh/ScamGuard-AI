# To Remove whitespaces from email
def pre_process(email: str) -> str:
    return {"email_text": email.strip()}

def pre_process_2(email) -> str:
    return email.strip()

def post_process(output):
    return output.model_dump()
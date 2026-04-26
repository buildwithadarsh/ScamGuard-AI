from pathlib import Path


def load_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# system_prompt = load_file("prompts/system_prompt.txt")

# system_prompt_path = "prompts/system_prompt.txt"

BASE_DIR = Path(__file__).resolve().parent.parent  # goes to app/
PROMPT_PATH = BASE_DIR / "prompts" / "system_prompt.txt"

def load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")

# def load_system_prompt(system_prompt_path) -> str:
#     return load_file(system_prompt_path)
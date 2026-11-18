from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
    print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def load_notes():

    with open("curriculum/unit_0/notes.txt", "r", encoding="utf-8") as file:
        return file.read()

#Notes for AI
def ask_ai(question: str):

    notes = load_notes()

    response = client.responses.create(
        model="gpt-5",
        input=f"""
You are an expert math tutor for Accelerated Math 2/3 Honors.

The following notes describe the actual curriculum and teacher expectations.
Use this information when answering.

Course Notes:
{notes}

Rules:
- Explain step-by-step.
- Show reasoning clearly.
- Be encouraging but concise.
- If the student is wrong, explain why.
- Use examples when helpful.

Student Question:
{question}
"""
    )

    return response.output_text
# Connecting to Endpoint

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

print("MAIN.PY LOADED")

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Welcome to AI Math Tutor"}


@app.post("/ask")
def ask_question(data: Question):

    answer = ask_ai(data.question)

    return {
        "answer": answer
    }
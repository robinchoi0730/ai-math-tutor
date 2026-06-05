from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

#Instructing AI 
def ask_ai(question: str):
    response = client.responses.create(
        model="gpt-5",
        input=f"""
You are an expert math tutor.

Rules:
- Explain step-by-step.
- Show reasoning clearly.
- Be encouraging but concise.
- If the student is wrong, explain why.
- Use examples when helpful.

Student question:
{question}
"""
    )

    return response.output_text

# Connecting to Endpoint

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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
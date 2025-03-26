import json
import csv
import os
from fastapi import FastAPI, Form
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Load FAQ data
with open("faq_data.json", "r") as f:
    faq_data = json.load(f)["faqs"]

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/faq")
def get_answer(question: str):
    for faq in faq_data:
        if question.lower() in faq["question"].lower():
            return {"answer": faq["answer"]}

    # AI-generated response if no match is found
    response = client.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Answer this question based on IT consulting: {question}",
        max_tokens=50
    )
    return {"answer": response["choices"][0]["text"].strip()}

@app.post("/collect_info/")
def collect_info(name: str = Form(...), email: str = Form(...)):
    with open("visitors.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email])

    return {"message": "Information saved successfully!"}

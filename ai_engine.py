
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_business_plan(
    business_idea,
    category,
    budget,
    target,
    question
):

    prompt = f"""
You are an AI Business Plan Assistant.

Business Idea: {business_idea}
Category: {category}
Investment Budget: ₹{budget}
Target Customers: {target}
User Question: {question}

Generate a complete business plan with:

1. Business Overview
2. Business Objectives
3. Products and Services
4. Target Customers
5. Marketing Strategy
6. Investment Requirements
7. Monthly Expenses
8. Revenue Estimation
9. Profit Estimation
10. Risks and Solutions
11. Future Development

Use simple English.
Give a clear and useful answer.
Financial values must be treated as estimates.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text

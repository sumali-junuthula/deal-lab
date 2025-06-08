from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_strategy(buyer: str, target: str):
  try:
    prompt = f"""
    You are an investment banker preparing a pitch deck for a potential M&A deal.
    Write a strategic rationale for why {buyer} should acquire {target}.
    """

    response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[{"role": "user", "content": prompt}],
      temperature=0.6,
      max_tokens=400,
    )

    return {"strategy_summary": response.choices[0].message.content}

  except Exception as e:
    return {"error": str(e)}

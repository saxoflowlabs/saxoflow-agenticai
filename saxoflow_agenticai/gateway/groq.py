# saxoflow_agenticai/gateway/groq.py

import os
import requests
from dotenv import load_dotenv
from saxoflow_agenticai.gateway.base import ModelGateway

load_dotenv()

class GroqGateway(ModelGateway):
    def __init__(self, model_name):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model_name
        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def query(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 512
        }

        response = requests.post(self.url, headers=headers, json=payload)
        if response.status_code != 200:
            print("❌ Request failed with status", response.status_code)
            print("📨 Response:", response.text)
            response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"].strip()

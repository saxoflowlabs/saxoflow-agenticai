import os
import requests
from dotenv import load_dotenv
from saxoflow_agenticai.gateway.base import ModelGateway

load_dotenv()

class FireworksGateway(ModelGateway):
    def __init__(self, model_name):
        self.api_key = os.getenv("FIREWORKS_API_KEY")
        self.model = model_name
        self.url = "https://api.fireworks.ai/inference/v1/chat/completions"
        if not self.api_key:
            raise ValueError("FIREWORKS_API_KEY not set in environment.")

    def query(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        body = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 4096,
        }
        response = requests.post(self.url, headers=headers, json=body)
        if response.status_code != 200:
            print("❌ Fireworks API call failed:", response.status_code)
            print("📨", response.text)
            response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

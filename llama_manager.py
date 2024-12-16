import requests
import json

url = "http://localhost:11434/api/chat"

class LlamaManager:
    def query(self, prompt):
        data = {
            "model": "llama3",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()["message"]["content"]
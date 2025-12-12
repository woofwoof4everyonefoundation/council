import os
import openai
from .base import ModelProvider

class OpenAIProvider(ModelProvider):
    def __init__(self, model_name: str, api_key: str | None = None):
        self.model_name = model_name
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def call(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return response["choices"][0]["message"]["content"]

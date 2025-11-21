import os
from gpt4all import GPT4All

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_FILE = "qwen2.5-0.5b-instruct-q4_k_m.gguf"
MODEL_PATH = os.path.join(BASE_DIR, "models")

class LLMWrapper:
    def __init__(self):
        print("Loading Qwen2.5 0.5B Instruct (GGUF)...")
        self.model = GPT4All(
            model_name=MODEL_FILE,
            model_path=MODEL_PATH,
            allow_download=False
        )

    def generate(self, prompt: str, max_tokens: int = 150):
        raw = self.model.generate(
            prompt=prompt,
            max_tokens=max_tokens,
            temp=0.85,
            top_p=0.9,
            repeat_penalty=1.2
        )

        text = (
            raw.replace("<|im_start|>", "")
               .replace("<|im_end|>", "")
               .strip()
        )
        return text

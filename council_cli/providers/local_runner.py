import subprocess
from .base import ModelProvider

class LocalRunner(ModelProvider):
    """Very simple local runner calling an external command-line model."""

    def __init__(self, command: str, model_path: str | None = None):
        self.command = command
        self.model_path = model_path

    def call(self, prompt: str) -> str:
        cmd = [self.command]
        if self.model_path:
            cmd += ["--model", self.model_path]
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, _ = proc.communicate(prompt)
        return stdout

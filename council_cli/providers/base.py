class ModelProvider:
    """Abstract model interface for Council CLI."""

    def call(self, prompt: str) -> str:
        raise NotImplementedError

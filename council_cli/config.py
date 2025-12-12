import yaml
from council.registry import Registry
from .providers.openai_api import OpenAIProvider
from .providers.local_runner import LocalRunner

class CouncilConfig:
    """Loads Council configuration for CLI usage."""

    def __init__(self, path: str = "council.yaml"):
        with open(path, "r") as f:
            self.raw = yaml.safe_load(f)

        self.registry = Registry()
        self.registry.load_tasks(self.raw["tasks"])
        self.registry.load_profiles(self.raw["profiles"])

        provider_cfg = self.raw.get("provider", {})
        ptype = provider_cfg.get("type")

        if ptype == "openai":
            self.provider = OpenAIProvider(
                model_name=provider_cfg["model"],
                api_key=provider_cfg.get("api_key"),
            )
        elif ptype == "local":
            self.provider = LocalRunner(
                command=provider_cfg["command"],
                model_path=provider_cfg.get("model"),
            )
        else:
            self.provider = None  # Not required unless self-assessment is used

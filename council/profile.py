from dataclasses import dataclass, field
from typing import Dict, Any
import datetime

@dataclass
class Profile:
    """Describes observed behavioral traits of a model."""
    model_name: str
    version: str = "unknown"
    observed_by: str = "anonymous"
    date: str = field(default_factory=lambda: datetime.date.today().isoformat())
    traits: Dict[str, str] = field(default_factory=dict)
    notes: Dict[str, Any] = field(default_factory=dict)

    def has_trait(self, trait: str) -> str:
        return self.traits.get(trait)

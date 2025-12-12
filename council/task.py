from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Task:
    """Represents a category of cognitive work, not a single prompt."""
    id: str
    description: str
    traits_required: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def requires(self, trait: str) -> str:
        return self.traits_required.get(trait)

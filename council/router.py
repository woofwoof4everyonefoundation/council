from typing import List, Optional
from .task import Task
from .profile import Profile

ORDINAL = {
    "cannot_do": -999,
    "very_low": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
    "excellent": 4,
    "perfect": 5,
}

class Router:
    """Simple trait-based task-to-model router."""

    def __init__(self, weighting: Optional[dict] = None):
        self.weighting = weighting or {}

    def score(self, task: Task, profile: Profile) -> float:
        score = 0.0
        for trait, required in task.traits_required.items():
            model_level = profile.has_trait(trait) or "very_low"
            diff = ORDINAL.get(model_level, 0) - ORDINAL.get(required, 0)
            weight = self.weighting.get(trait, 1.0)
            score += diff * weight
        return score

    def select(self, task: Task, profiles: List[Profile]) -> Profile:
        scored = [(self.score(task, p), p) for p in profiles]
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1]

    def explain(self, task: Task, profile: Profile) -> str:
        lines = [f"Selected model: {profile.model_name}", ""]
        lines.append("Reasons:")
        for trait, required in task.traits_required.items():
            model_val = profile.has_trait(trait) or "n/a"
            lines.append(f" - {trait}: required {required}, model {model_val}")
        return "\n".join(lines)

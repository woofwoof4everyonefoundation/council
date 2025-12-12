import yaml
from .task import Task
from .profile import Profile

class Registry:
    """In-memory registry for tasks and profiles backed by YAML files."""

    def __init__(self):
        self.tasks = {}
        self.profiles = {}

    def load_tasks(self, path: str):
        with open(path, "r") as f:
            raw = yaml.safe_load(f) or []
        for item in raw:
            t = Task(
                id=item["id"],
                description=item["description"],
                traits_required=item.get("traits_required", {}),
                metadata=item.get("metadata", {}),
            )
            self.tasks[t.id] = t

    def load_profiles(self, path: str):
        with open(path, "r") as f:
            raw = yaml.safe_load(f) or []
        for item in raw:
            p = Profile(
                model_name=item["model_name"],
                version=item.get("version", "unknown"),
                observed_by=item.get("observed_by", "anonymous"),
                traits=item.get("traits", {}),
                notes=item.get("notes", {}),
            )
            self.profiles[p.model_name] = p

    def get_task(self, id: str) -> Task:
        return self.tasks[id]

    def get_profiles(self):
        return list(self.profiles.values())

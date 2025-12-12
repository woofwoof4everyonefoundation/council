from council.registry import Registry
from council.router import Router

if __name__ == "__main__":
    reg = Registry()
    reg.load_tasks("tasks.yaml")
    reg.load_profiles("profiles.yaml")

    task = reg.get_task("investigative_summarization")
    profiles = reg.get_profiles()

    router = Router()
    winner = router.select(task, profiles)

    print(router.explain(task, winner))

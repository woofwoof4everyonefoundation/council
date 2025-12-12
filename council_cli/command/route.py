from council_cli.config import CouncilConfig
from council.router import Router

def run_route(args):
    cfg = CouncilConfig()
    task = cfg.registry.get_task(args.task_id)
    profiles = cfg.registry.get_profiles()

    router = Router()
    winner = router.select(task, profiles)

    print(router.explain(task, winner))

def register(subparsers):
    p = subparsers.add_parser("route", help="Route a task to the best model")
    p.add_argument("task_id")
    p.set_defaults(func=run_route)

from council_cli.config import CouncilConfig

def run_list(args):
    cfg = CouncilConfig()
    for t in cfg.registry.tasks.values():
        print(f"{t.id}: {t.description}")

def run_info(args):
    cfg = CouncilConfig()
    t = cfg.registry.get_task(args.task_id)
    print(t)

def register(subparsers):
    p = subparsers.add_parser("tasks", help="List all tasks")
    p.set_defaults(func=run_list)

    p_info = subparsers.add_parser("task-info", help="Show details for a task")
    p_info.add_argument("task_id")
    p_info.set_defaults(func=run_info)

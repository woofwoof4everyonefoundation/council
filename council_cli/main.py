import argparse
from council_cli.commands import route, tasks, profiles, self_assess, compare, drift, reconcile

def cli():
    parser = argparse.ArgumentParser(prog="council", description="Council Framework CLI")
    subparsers = parser.add_subparsers(dest="command")

    tasks.register(subparsers)
    profiles.register(subparsers)
    route.register(subparsers)
    self_assess.register(subparsers)
    compare.register(subparsers)
    drift.register(subparsers)
    reconcile.register(subparsers)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    args.func(args)

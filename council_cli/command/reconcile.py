import yaml

def run_reconcile(args):
    with open(args.self_profile, "r") as f:
        s = yaml.safe_load(f)
    with open(args.human_profile, "r") as f:
        h = yaml.safe_load(f)

    print("Comparing model self-assessment with human profile:\n")
    for trait, model_val in s.get("traits", {}).items():
        human_val = h.get("traits", {}).get(trait)
        if human_val != model_val:
            print(f"{trait}: model={model_val} | human={human_val}")

def register(subparsers):
    p = subparsers.add_parser("reconcile", help="Show differences between self-assessed and human profile")
    p.add_argument("self_profile")
    p.add_argument("human_profile")
    p.set_defaults(func=run_reconcile)

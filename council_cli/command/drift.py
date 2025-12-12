import glob
import yaml

def run_drift(args):
    pattern = f"profiles/{args.model_name}*.yaml"
    files = sorted(glob.glob(pattern))
    if len(files) < 2:
        print("Not enough profile versions to check drift.")
        return

    prev = yaml.safe_load(open(files[-2]))
    curr = yaml.safe_load(open(files[-1]))

    print(f"Drift for {args.model_name}:")
    for trait, old in prev.get("traits", {}).items():
        new = curr.get("traits", {}).get(trait)
        if new != old:
            print(f" - {trait}: {old} -> {new}")

def register(subparsers):
    p = subparsers.add_parser("drift", help="Show trait drift for a model over versions")
    p.add_argument("model_name")
    p.set_defaults(func=run_drift)

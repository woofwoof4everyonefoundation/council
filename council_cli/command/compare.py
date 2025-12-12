from council_cli.config import CouncilConfig

def run_compare(args):
    cfg = CouncilConfig()
    a = cfg.registry.profiles[args.model_a]
    b = cfg.registry.profiles[args.model_b]

    print(f"Comparing {a.model_name} vs {b.model_name}:\n")
    for trait in sorted(set(list(a.traits.keys()) + list(b.traits.keys()))):
        av = a.traits.get(trait)
        bv = b.traits.get(trait)
        if av != bv:
            print(f"{trait}: {av} vs {bv}")

def register(subparsers):
    p = subparsers.add_parser("compare", help="Compare two model profiles")
    p.add_argument("model_a")
    p.add_argument("model_b")
    p.set_defaults(func=run_compare)

import json
from council_cli.config import CouncilConfig
from council.self_assess import model_self_assess

def run_self_assess(args):
    cfg = CouncilConfig()
    if cfg.provider is None:
        raise RuntimeError("No provider configured in council.yaml")

    def api_call(prompt: str) -> str:
        return cfg.provider.call(prompt)

    result = model_self_assess(api_call)
    print(json.dumps(result, indent=2))

    if args.save:
        with open(args.save, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Saved to {args.save}")

def register(subparsers):
    p = subparsers.add_parser("self-assess", help="Ask a model to self-assess its traits")
    p.add_argument("--save", help="Save JSON result to file")
    p.set_defaults(func=run_self_assess)

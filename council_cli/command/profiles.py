from council_cli.config import CouncilConfig

def run_profiles(args):
    cfg = CouncilConfig()
    for p in cfg.registry.profiles.values():
        print(p.model_name)

def run_info(args):
    cfg = CouncilConfig()
    p = cfg.registry.profiles[args.model_name]
    print(p)

def register(subparsers):
    p = subparsers.add_parser("profiles", help="List all profiles")
    p.set_defaults(func=run_profiles)

    p_info = subparsers.add_parser("profile-info", help="Show details for a profile")
    p_info.add_argument("model_name")
    p_info.set_defaults(func=run_info)

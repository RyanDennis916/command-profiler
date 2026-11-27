import argparse

def parse_args(argv: list[str]) -> list[str]:
    parser = argparse.ArgumentParser(
            prog="profiler.py"
            description="Profiling a program's wall clcok time, ram, and exit status",
    )
    parser.add_argument(
            "command",
            nargs=argparse.REMAINDER,
            help="Command and args to run (pass -- before cmds starting with -)",
    )

    args=parser.parse_args(argv)
    cmd = args.command
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        parser.error("provide a cmd to run")
    return cmd




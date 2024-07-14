"""Install requirements for a given integration."""

import argparse
from pathlib import Path
import subprocess
import sys

from .gen_requirements_all import gather_recursive_requirements
from .util import valid_integration
from security import safe_command


def get_arguments() -> argparse.Namespace:
    """Get parsed passed in arguments."""
    parser = argparse.ArgumentParser(
        description="Install requirements for a given integration"
    )
    parser.add_argument(
        "integration", type=valid_integration, help="Integration to target."
    )

    arguments = parser.parse_args()

    return arguments


def main() -> int | None:
    """Install requirements for a given integration."""
    if not Path("requirements_all.txt").is_file():
        print("Run from project root")
        return 1

    args = get_arguments()

    requirements = gather_recursive_requirements(args.integration)

    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-c",
        "homeassistant/package_constraints.txt",
        "-U",
        *requirements,
    ]
    print(" ".join(cmd))
    safe_command.run(subprocess.run, cmd,
        check=True,
    )


if __name__ == "__main__":
    sys.exit(main())

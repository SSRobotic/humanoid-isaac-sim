"""Launch a pinned Isaac Lab humanoid task after installing its GPU runtime.

--dry-run inspects local source paths without importing Isaac or launching a GPU.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "projects" / "IsaacLab"
SCRIPTS = {"random": "scripts/environments/random_agent.py",
           "train": "scripts/reinforcement_learning/rsl_rl/train.py",
           "play": "scripts/reinforcement_learning/rsl_rl/play.py"}


def build_command(action, task="Isaac-Humanoid-v0", num_envs=16, headless=False,
                  checkpoint=None, platform=None):
    if action not in SCRIPTS or num_envs < 1:
        raise ValueError("action and num_envs must be valid")
    if task != "Isaac-Humanoid-v0":
        raise ValueError("this starter supports the pinned Isaac-Humanoid-v0 task")
    script = LAB / SCRIPTS[action]
    windows = (platform or os.name) == "nt"
    launcher = LAB / ("isaaclab.bat" if windows else "isaaclab.sh")
    for path in (script, launcher):
        if not path.is_file():
            raise FileNotFoundError(path)
    command = (["cmd.exe", "/c", str(launcher)] if windows else ["bash", str(launcher)])
    command += ["-p", str(script), "--task", task, "--num_envs", str(num_envs)]
    if headless:
        command.append("--headless")
    if checkpoint:
        checkpoint = Path(checkpoint).resolve()
        if not checkpoint.is_file():
            raise FileNotFoundError(checkpoint)
        if action != "play":
            raise ValueError("checkpoint is only supported for play")
        command += ["--checkpoint", str(checkpoint)]
    elif action == "play":
        raise ValueError("play requires --checkpoint from a trained policy")
    return command


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=SCRIPTS)
    parser.add_argument("--task", default="Isaac-Humanoid-v0")
    parser.add_argument("--num-envs", type=int, default=16)
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--checkpoint")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    command = build_command(args.action, args.task, args.num_envs, args.headless, args.checkpoint)
    if args.dry_run:
        print(json.dumps({"cwd": str(LAB), "command": command,
                          "validation": "source paths only; GPU/runtime not tested"}, indent=2))
        return 0
    return subprocess.call(command, cwd=LAB)


if __name__ == "__main__":
    raise SystemExit(main())

import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1]/"examples"/"launch_humanoid.py"
spec = importlib.util.spec_from_file_location("launcher", path)
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class LauncherTests(unittest.TestCase):
    def test_windows_and_linux_source_paths(self):
        for platform in ("nt", "posix"):
            for action in ("random", "train"):
                command = launcher.build_command(action, num_envs=8, headless=True, platform=platform)
                self.assertIn("Isaac-Humanoid-v0", command)
                self.assertEqual(command[-1], "--headless")
                script = Path(command[command.index("-p")+1])
                self.assertTrue(script.is_file())

    def test_missing_checkpoint_is_rejected(self):
        with self.assertRaises(ValueError):
            launcher.build_command("play")
        with self.assertRaises(FileNotFoundError):
            launcher.build_command("play", checkpoint="missing-policy.pt")

    def test_invalid_environment_count_and_task(self):
        with self.assertRaises(ValueError):
            launcher.build_command("random", num_envs=0)
        with self.assertRaises(ValueError):
            launcher.build_command("random", task="made-up-task")


if __name__ == "__main__":
    unittest.main()

<p align="center"><img src="assets/ssrobotics-logo.jpg" alt="SSRobotics — original logo by SSRobotic" width="240"></p>

<h1 align="center">🟢 Isaac Sim & Isaac Lab</h1>
<p align="center"><b>SSRobotics · Source Code Collection</b></p>

<p align="center">
  <a href="https://ssrobotic.github.io/humanoid-robot-hub/"><img src="https://img.shields.io/badge/Resources-8-f28c28?style=flat-square" alt="8 curated resources"></a>
  <a href="https://ssrobotic.github.io/humanoid-robot-hub/"><img src="https://img.shields.io/badge/Language-TH_%2F_EN-555555?style=flat-square" alt="Thai and English"></a>
  <a href="https://github.com/SSRobotic/humanoid-robot-hub/blob/main/CREDITS.md"><img src="https://img.shields.io/badge/Original_sources-Credited-555555?style=flat-square" alt="Original authors credited"></a>
</p>


**Part of [Humanoid Robot Hub](https://github.com/SSRobotic/humanoid-robot-hub)** · [🔎 Search all resources](https://ssrobotic.github.io/humanoid-robot-hub/)

Isaac Sim scenes, Isaac Lab training, ROS integration and policy evaluation resources.

ฉาก Isaac Sim, การฝึกบน Isaac Lab, เชื่อม ROS และการประเมิน Policy

Curated by **SSRobotic — Robotics Engineer & Open-source Curator**. This repository contains actual source files and models in `projects/`, alongside a resource catalog and engineering guide. The imported implementations are unchanged snapshots credited to their original creators.

## 📦 Code & models in this repository

**11,522 tracked upstream files** — เปิดโฟลเดอร์ด้านล่างเพื่อดูโค้ดจริง โมเดล และตัวอย่างต้นฉบับ

| Project files | Files | Pinned source | License / notices |
| --- | ---: | --- | --- |
| [isaac-sim/IsaacLab](projects/IsaacLab) | 1,993 | [`b0542fe2d45b`](https://github.com/isaac-sim/IsaacLab/tree/b0542fe2d45bf91c4e1d9ef6952b9c709c80b4e8) | [LICENSE](projects/IsaacLab/LICENSE) · [LICENSE-mimic](projects/IsaacLab/LICENSE-mimic) |
| [isaac-sim/IsaacSim](projects/IsaacSim) | 9,529 | [`2469084bc328`](https://github.com/isaac-sim/IsaacSim/tree/2469084bc328710207c6bc4ede32209082a9286c) | [LICENSE](projects/IsaacSim/LICENSE) · [THIRD_PARTY_NOTICE.md](projects/IsaacSim/THIRD_PARTY_NOTICE.md) |

**Contents:** 10,375 files contain their complete tracked contents; 1,147 files are Git LFS pointers to large upstream assets. These pointers are listed in the source manifests. Their binary objects are not hosted in SSRobotics LFS storage. Fetch needed assets from the original pinned project checkout under its own licenses.

[Source manifest](source-manifest.json) records commits, file counts, Git LFS pointers and external submodules. [Per-file manifests](source-manifests/) record original Git blob hashes. `projects/` keeps upstream code, README files, licenses and notices; SSRobotics supplies the organization and guides.

```bash
# Skip LFS smudging: large asset objects remain upstream
git -c filter.lfs.smudge= -c filter.lfs.process= -c filter.lfs.required=false clone --depth 1 https://github.com/SSRobotic/humanoid-isaac-sim.git
cd humanoid-isaac-sim
```

### ▶️ Inspect and launch a humanoid task

[Isaac Lab humanoid environment](projects/IsaacLab/source/isaaclab_tasks/isaaclab_tasks/manager_based/classic/humanoid/) · [Training entry point](projects/IsaacLab/scripts/reinforcement_learning/rsl_rl/train.py) · [SSRobotics launcher](examples/launch_humanoid.py)

```bash
# Source-path check; works without Isaac or a GPU
python examples/launch_humanoid.py random --num-envs 16 --dry-run
python -m unittest discover -s tests -v

# After completing the pinned Isaac Lab installation instructions
python examples/launch_humanoid.py random --num-envs 16
python examples/launch_humanoid.py train --num-envs 128 --headless
python examples/launch_humanoid.py play --checkpoint /path/to/model.pt
```

The retained Isaac Lab version is **2.3.2** (`main`, pinned above); its [compatibility table](projects/IsaacLab/README.md#isaac-sim-version-dependency) lists Isaac Sim 4.5 / 5.0 / 5.1. The separate Isaac Sim source snapshot is an upstream `develop` snapshot and is **not** a prebuilt compatible runtime for that Lab version. Follow [Isaac Lab installation](https://isaac-sim.github.io/IsaacLab/v2.3.2/source/setup/installation/index.html) and the pinned README when choosing the runtime.

This collection includes open-source code, not the NVIDIA runtime, hosted USD assets or a trained policy. Those are acquired through the upstream installation and access procedures under their own terms. We checked the launcher’s source paths; GPU simulation and policy training have not been run in this workspace.

## 🚀 Start here

Start with the [task selection and engineering guide](GUIDE.md): simulator setup, robot assets, ROS integration and policy evaluation.

## 🗂️ Resource directory

| Resource | What it provides | Keywords | Original source |
| --- | --- | --- | --- |
| [Unitree RL Gym](https://github.com/unitreerobotics/unitree_rl_gym) | Reinforcement learning training examples for Unitree locomotion. Use the documented simulator and task versions. | Unitree, RL, Isaac Gym | [unitreerobotics](https://github.com/unitreerobotics/unitree_rl_gym) |
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | Framework for robot learning built on Isaac Sim, with environments and training integrations. | RL, Simulation, Isaac Sim | [isaac-sim](https://github.com/isaac-sim/IsaacLab) |
| [TienKung Lab](https://github.com/Open-X-Humanoid/TienKung-Lab) | Isaac Lab workflows for legged-robot learning, including TienKung. | TienKung, RL, Isaac Lab | [Open-X-Humanoid](https://github.com/Open-X-Humanoid/TienKung-Lab) |
| [X-Humanoid VLA Benchmark](https://github.com/Open-X-Humanoid/x-humanoid-vla-simulation-benchmark) | Isaac Sim resources for evaluating vision-language-action policies. | VLA, Benchmark, Isaac Sim | [Open-X-Humanoid](https://github.com/Open-X-Humanoid/x-humanoid-vla-simulation-benchmark) |
| [Isaac Sim](https://github.com/isaac-sim/IsaacSim) | Robot simulation on NVIDIA Omniverse, with physics, sensor simulation and robot integration. | Isaac Sim, USD, RTX | [isaac-sim](https://github.com/isaac-sim/IsaacSim) |
| [Isaac Lab Arena](https://github.com/isaac-sim/IsaacLab-Arena) | Composable simulation tasks and policy evaluation built around Isaac Lab. | Isaac Lab, Policy evaluation, Benchmarks | [isaac-sim](https://github.com/isaac-sim/IsaacLab-Arena) |
| [Isaac Sim ROS Workspaces](https://github.com/isaac-sim/IsaacSim-ros_workspaces) | ROS workspace packages for Isaac Sim integration; check the supported ROS distribution upstream. | Isaac Sim, ROS 2, Integration | [isaac-sim](https://github.com/isaac-sim/IsaacSim-ros_workspaces) |
| [Isaac Automator](https://github.com/isaac-sim/IsaacAutomator) | Infrastructure tooling for Isaac cloud workstations; review provider setup and costs before deployment. | Isaac Sim, Cloud, Infrastructure | [isaac-sim](https://github.com/isaac-sim/IsaacAutomator) |

**Legacy reference:** Unitree RL Gym uses its documented Isaac Gym workflow. Isaac Gym, Isaac Sim and Isaac Lab are distinct projects; check compatibility before adapting examples.

[resources.json](resources.json) contains the structured entries. [GUIDE.md](GUIDE.md) connects tools to tasks and records the information needed to reproduce an experiment.

## 🔗 Explore the ecosystem

<details>
<summary>🌐 Browse all 14 categories</summary>

[🦾 Models & URDF](https://github.com/SSRobotic/humanoid-models) · [🌐 Simulation](https://github.com/SSRobotic/humanoid-simulation) · [🧠 Robot Learning](https://github.com/SSRobotic/humanoid-robot-learning) · [⚙️ Whole-body Control](https://github.com/SSRobotic/humanoid-whole-body-control) · [👁️ Vision & 3D Perception](https://github.com/SSRobotic/humanoid-vision) · [🤏 Manipulation & Planning](https://github.com/SSRobotic/humanoid-manipulation) · [🎮 Teleoperation](https://github.com/SSRobotic/humanoid-teleoperation) · [💾 Datasets & Demonstrations](https://github.com/SSRobotic/humanoid-datasets) · [💬 Vision-Language-Action](https://github.com/SSRobotic/humanoid-vla) · [🔌 Hardware & SDKs](https://github.com/SSRobotic/humanoid-hardware-sdks) · [📡 ROS & Integration](https://github.com/SSRobotic/humanoid-ros2) · [📚 Research & Benchmarks](https://github.com/SSRobotic/humanoid-research) · [🟢 Isaac Sim & Isaac Lab](https://github.com/SSRobotic/humanoid-isaac-sim) · [🧮 Robotics Algorithms](https://github.com/SSRobotic/humanoid-algorithms)

</details>

[🏠 Main Hub](https://github.com/SSRobotic/humanoid-robot-hub) · [🤖 Profile](https://github.com/SSRobotic)

## 🙌 Help this collection grow

⭐ [Star the Hub](https://github.com/SSRobotic/humanoid-robot-hub) · 👤 [Follow SSRobotic](https://github.com/SSRobotic) · 💡 [Suggest a resource](https://github.com/SSRobotic/humanoid-robot-hub/issues/new/choose)

Suggestions and corrections follow the [Hub contribution guide](https://github.com/SSRobotic/humanoid-robot-hub/blob/main/CONTRIBUTING.md). Linked software, assets and documentation keep their original licenses. The original SSRobotics logo is supplied by its creator; the root MIT license covers our original descriptions, guides and SSRobotics example code only. Imported `projects/` files retain their own licenses.

# 🟢 Isaac Sim / Isaac Lab engineering guide

[🏠 Main Hub](https://github.com/SSRobotic/humanoid-robot-hub) · [↩️ Directory](README.md)

## 🎯 Choose the layer that matches your task

| Goal | Start with | What you prepare |
| --- | --- | --- |
| Import a robot, inspect joints and add camera / depth streams | [Isaac Sim](https://github.com/isaac-sim/IsaacSim) | Robot assets, scene, sensor settings and controller interface |
| Train a locomotion or manipulation policy | [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | Supported embodiment, observations, actions, rewards and training backend |
| Assemble tasks and compare policies | [Isaac Lab Arena](https://github.com/isaac-sim/IsaacLab-Arena) | Task definitions, objects, evaluation conditions and policy interface |
| Connect simulation with ROS | [ROS workspaces](https://github.com/isaac-sim/IsaacSim-ros_workspaces) | ROS distribution, bridge configuration, message types and frame names |
| Study TienKung workflows | [TienKung Lab](https://github.com/Open-X-Humanoid/TienKung-Lab) | Its robot assets, environment and dependency versions |
| Inspect VLA evaluation in simulation | [X-Humanoid benchmark](https://github.com/Open-X-Humanoid/x-humanoid-vla-simulation-benchmark) | Its supported embodiments, tasks and evaluation instructions |

Isaac Sim provides the simulator. Isaac Lab organizes robot-learning environments and training integrations. Their versions must match the selected workflow; a repository name alone does not establish compatibility.

## 🚀 A practical route from model to policy

1. **Check the environment.** Read the [Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html) and [Isaac Lab installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html). Record the simulator / Lab release, OS, GPU, driver and Python environment supported by that release.
2. **Inspect the robot.** Use the source project's supported URDF / MJCF / USD path. Confirm joint names and order, joint axes, units, inertias, limits, actuator settings and collision geometry. Save an untouched copy of the source assets and their notices.
3. **Run one documented scene.** Inspect articulation state and the initial pose. Check gravity, time step and sensor / control rates before adding a complex task.
4. **Use a documented environment.** For learning, reproduce the upstream example first. Record observation normalization, action scaling, reward terms, resets, randomization and the policy checkpoint.
5. **Evaluate separately.** Use explicit task conditions and multiple episodes. Record falls, task success, tracking error and episode length as relevant to the task. Keep training conditions distinct from evaluation conditions.
6. **Integrate ROS when needed.** Confirm bridge instructions, ROS distribution, `/clock`, timestamps, topic names and TF conventions. Inspect simulated states before connecting a controller.

## 📝 Reproducibility record

| Item | Record |
| --- | --- |
| Software | Isaac Sim / Isaac Lab release, source commits, OS and dependencies |
| Hardware | GPU, driver and memory required by the chosen workload |
| Robot | Asset source, model revision, joint order and actuator configuration |
| Timing | Physics step, control step and sensor update rates |
| Policy | Framework, checkpoint, observations, actions and normalization |
| Evaluation | Task, seeds, episode count, metrics and scene conditions |

## 🔗 Next steps

- [🧮 Robotics Algorithms](https://github.com/SSRobotic/humanoid-algorithms): choose IK, MPC, whole-body control or motion planning.
- [🧠 Robot Learning](https://github.com/SSRobotic/humanoid-robot-learning): compare learning frameworks.
- [🦾 Models](https://github.com/SSRobotic/humanoid-models): inspect descriptions and meshes.
- [📡 ROS](https://github.com/SSRobotic/humanoid-ros2): middleware and controller integration.

These are original curation notes from SSRobotics. Follow each linked project's installation instructions and license; no combined installation or humanoid policy is claimed to have been tested here.

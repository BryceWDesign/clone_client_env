# clone_client_env

An experimental sandbox for simulating and evaluating control agents in a Clone Robotics-compatible environment.

## Overview

This environment provides a modular interface for testing AI control agents outside of real-world hardware. It allows for simulation-to-real (sim2real) development by defining consistent APIs and providing utilities for seamless agent evaluation.

## Features

- 🎮 Unified interface for running agent policies in a simulated environment.
- ⚙️ Synchronization tools to emulate Clone Robotics’ control loop and interface expectations.
- 🧱 Extensible framework to swap out environments, agents, and sensors with minimal changes.
- 📊 SimulationRunner class to facilitate continuous episode execution and reward tracking.
- 📦 Plug-and-play abstractions to test learned policies before deploying to physical hardware.

## Goals

- Close the realism gap between simulation and physical systems.
- Improve modularity for easier experimentation with different control strategies.
- Provide a clean and minimal baseline to rapidly test new agents.

## Usage

```python
from clone_client_env import Environment, Agent, SimulationRunner

env = Environment()
agent = Agent()
runner = SimulationRunner(env, agent)

reward = runner.run()
print(f"Total reward: {reward}")
- Python 3.9+
- numpy

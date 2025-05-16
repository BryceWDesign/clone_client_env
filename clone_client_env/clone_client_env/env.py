import gym
from gym import spaces
import numpy as np

class CloneClientEnv(gym.Env):
    """
    Custom Gym environment for controlling Clone Robotics' simulated or physical hand.
    """

    metadata = {'render.modes': ['human']}

    def __init__(self, config=None):
        super(CloneClientEnv, self).__init__()
        
        self.config = config or {}
        self.time_step = 0

        # Define a simple 20 DOF hand model, values from -1.0 to 1.0 normalized control space
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(20,), dtype=np.float32)

        # Observation includes joint angles and optionally force sensors or touch feedback
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(40,), dtype=np.float32)

        self.state = np.zeros(self.observation_space.shape, dtype=np.float32)

    def step(self, action):
        action = np.clip(action, self.action_space.low, self.action_space.high)
        # Update the internal state (placeholder logic)
        self.state[:20] = action
        self.state[20:] = np.random.randn(20).astype(np.float32)  # Mock sensor feedback

        self.time_step += 1
        done = self.time_step >= 200  # End episode after 200 steps
        reward = self._compute_reward()
        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.time_step = 0
        self.state = np.zeros(self.observation_space.shape, dtype=np.float32)
        return self.state

    def render(self, mode='human'):
        print(f"[Step {self.time_step}] Action: {self.state[:20]}")

    def close(self):
        pass

    def _compute_reward(self):
        # Placeholder: negative reward for joint deviation
        return -np.sum(np.square(self.state[:20]))

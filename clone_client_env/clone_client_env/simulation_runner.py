import time

class SimulationRunner:
    def __init__(self, env, agent, max_steps=1000, render=False):
        self.env = env
        self.agent = agent
        self.max_steps = max_steps
        self.render = render

    def run(self):
        observation = self.env.reset()
        self.agent.reset()
        total_reward = 0

        for step in range(self.max_steps):
            if self.render:
                self.env.render()

            action = self.agent.act(observation)
            observation, reward, done, _ = self.env.step(action)
            self.agent.update(reward, done)
            total_reward += reward

            if done:
                break

            time.sleep(0.01)  # Optional delay for visualization

        return total_reward

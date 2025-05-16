class AgentInterface:
    def __init__(self, action_space, observation_space):
        self.action_space = action_space
        self.observation_space = observation_space

    def reset(self):
        """
        Reset the agent state at the beginning of an episode.
        """
        raise NotImplementedError

    def act(self, observation):
        """
        Return an action in response to an observation.
        """
        raise NotImplementedError

    def update(self, reward, done):
        """
        Update internal state or learning algorithm (if applicable).
        """
        pass

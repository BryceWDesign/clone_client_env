from clone_client_env import CloneEnv
import numpy

clone_robot_env = CloneEnv()

clone_robot_env.connect()

clone_robot_env.reset(numpy.zeros(clone_robot_env.no_actions))
for _ in range(int(1e4)):
    rand_actions = numpy.random.uniform(low=-1, high=1, size=(clone_robot_env.no_actions,))
    clone_robot_env.step(rand_actions)
    obs = clone_robot_env.get_obs()

clone_robot_env.close()

# clone_client_env/constants.py

# Constants used across the environment
MAX_JOINT_ANGLE = 3.14  # Radians
MIN_JOINT_ANGLE = -3.14
MAX_FORCE = 100.0  # Newtons
MIN_FORCE = 0.0

# Actuator limits
ACTUATOR_SPEED_LIMIT = 1.0  # rad/s

# Simulation constants
SIMULATION_TIMESTEP = 0.02  # seconds
GRAVITY = -9.81  # m/s^2

# Environment configuration
DEFAULT_EPISODE_LENGTH = 1000  # steps

# Logging settings
ENABLE_LOGGING = True
LOGGING_INTERVAL = 10  # steps

# Placeholder for extensibility
MODULAR_EXTENSIONS = []

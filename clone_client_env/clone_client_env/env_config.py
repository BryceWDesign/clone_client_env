from dataclasses import dataclass

@dataclass
class EnvConfig:
    use_gui: bool = False
    use_real_robot: bool = False
    max_timesteps: int = 1000
    action_repeat: int = 1
    seed: int = 42
    camera_resolution: tuple = (640, 480)
    log_data: bool = True

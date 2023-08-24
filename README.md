# Clone Client Env

This package is wrapper around logic of `clone_client` package. It has a gym-like API however **it's not** gym compatible. Use it to extend any proper gym environment.

Clone Client API package is accessible here:
https://github.com/clonerobotics/clone_client

Please get familiar with README there before using this package.

## Installation

Unfortunately, we do not provide PyPI releases just yet, but you can use this repository as an installation candidate using pip:

https://pip.pypa.io/en/stable/cli/pip_install/#examples

## Quick overview

```python
from clone_client_env import CloneEnv

robot = CloneEnv(hostname="clonepiext", timeout=0.0045, log_level = logging.ERROR)
```

`hostname` - name of the robot to connect to. The dafult should be up-to-date. Although you can change it to your own robot name.

`timeout` - how long to wait for a response. Default is `0.0045` (4.5ms). Making it smaller can affect the overall frequency due to too much dropped frames.

For detailed specification please contact us.

`log_level` - level of logs to show in the console. Default is `logging.ERROR`. Changing this might be useful for debugging.

```python
# Connect
robot.connect()

# Step
robot.step([...])

# Obs
obs = robot.get_obs()

# Reset
robot.reset([...])

# Close
robot.close()

```

Working example can be found in [example.py](/clone_client_env/example.py)

Please use it as reference.

Mind that calling `get_obs` right after `step` **can't** guarantee that the actions have been performed fully. Consider adding a pause between.

## Contributing

We are open for any suggestions and bug reports using issue system, however we do not accept pull requests at the moment.

In case of any problem please contact us at https://clonerobotics.com/contact.

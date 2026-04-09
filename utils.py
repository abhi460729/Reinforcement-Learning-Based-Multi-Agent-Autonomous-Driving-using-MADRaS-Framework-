import numpy as np

def add_sensor_noise(obs):
    obs["speedX"] += np.random.normal(0, 0.5)
    obs["angle"] += np.random.normal(0, 0.01)
    return obs

def add_action_noise(action):
    return action + np.random.normal(0, 0.02, size=action.shape)

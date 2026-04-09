from madras.envs.gym_madras import MadrasEnv
from reward import compute_reward
from utils import add_sensor_noise

class CustomMadrasEnv(MadrasEnv):
    def __init__(self, use_noise=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_noise = use_noise

    def step(self, action):
        obs, reward, done, info = super().step(action)

        if self.use_noise:
            obs = add_sensor_noise(obs)

        reward = compute_reward(obs)
        return obs, reward, done, info

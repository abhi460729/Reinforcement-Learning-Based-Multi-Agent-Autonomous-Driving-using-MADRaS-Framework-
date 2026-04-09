from stable_baselines3 import PPO
from env import CustomMadrasEnv

env = CustomMadrasEnv(vision=False, throttle=True, gear_change=False)

model = PPO.load("models/madras_ppo")

obs = env.reset()

while True:
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()

    if done:
        obs = env.reset()

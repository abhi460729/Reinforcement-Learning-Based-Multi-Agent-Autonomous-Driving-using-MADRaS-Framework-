from stable_baselines3 import PPO
from env import CustomMadrasEnv
import time

env = CustomMadrasEnv(vision=False, throttle=True, gear_change=False)

model = PPO.load("models/madras_ppo")

obs = env.reset()

total_reward = 0

while True:
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()

    total_reward += reward

    if done:
        print(f"Episode Reward: {total_reward}")
        total_reward = 0
        obs = env.reset()

    time.sleep(0.01)

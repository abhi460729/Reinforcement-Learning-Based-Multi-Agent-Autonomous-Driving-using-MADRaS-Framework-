from stable_baselines3 import PPO
from env import CustomMadrasEnv
import time

env = CustomMadrasEnv(vision=False, throttle=True, gear_change=False)

model = PPO.load("models/madras_ppo")

obs = env.reset()

total_reward = 0
step_count = 0
collision_count = 0

print("🚦 Running HEAVY TRAFFIC scenario...")

while True:
    action, _ = model.predict(obs)

    obs, reward, done, info = env.step(action)
    env.render()

    total_reward += reward
    step_count += 1

    if obs.get("damage", 0) > 0:
        collision_count += 1

    if step_count % 100 == 0:
        print(f"Steps: {step_count} | Reward: {total_reward:.2f} | Collisions: {collision_count}")

    time.sleep(0.01)

    if done:
        print("\n🏁 Episode Finished")
        print(f"Total Steps: {step_count}")
        print(f"Total Reward: {total_reward:.2f}")
        print(f"Total Collisions: {collision_count}")

        obs = env.reset()
        total_reward = 0
        step_count = 0
        collision_count = 0

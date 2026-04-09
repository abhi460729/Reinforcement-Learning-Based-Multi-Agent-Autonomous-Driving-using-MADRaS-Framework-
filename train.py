from stable_baselines3 import PPO
from env import CustomMadrasEnv
from config import ENV_CONFIG, TRAINING_CONFIG

env = CustomMadrasEnv(
    vision=ENV_CONFIG["vision"],
    throttle=ENV_CONFIG["throttle"],
    gear_change=ENV_CONFIG["gear_change"]
)

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=TRAINING_CONFIG["learning_rate"],
    gamma=TRAINING_CONFIG["gamma"]
)

model.learn(total_timesteps=TRAINING_CONFIG["timesteps"])

model.save("models/madras_ppo")
print("✅ Training Complete")

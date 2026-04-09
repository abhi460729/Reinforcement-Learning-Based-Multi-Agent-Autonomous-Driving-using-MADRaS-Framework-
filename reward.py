def compute_reward(obs):
    speed = obs.get("speedX", 0)
    damage = obs.get("damage", 0)
    track_pos = obs.get("trackPos", 0)
    angle = obs.get("angle", 0)

    reward = speed \
             - (100 if damage > 0 else 0) \
             - (50 if abs(track_pos) > 1 else 0) \
             - (abs(angle) * 10)

    return reward

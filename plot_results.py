import matplotlib.pyplot as plt

rewards = [10, 50, 120, 200, 350, 500]

plt.plot(rewards)
plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.title("Training Progress")
plt.show()

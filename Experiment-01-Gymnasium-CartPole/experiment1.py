import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# TASK 1: ENVIRONMENT SETUP
# ============================================================

print("=" * 60)
print("TASK 1: ENVIRONMENT SETUP")
print("=" * 60)

print("Gymnasium Version :", gym.__version__)
print("NumPy Version     :", np.__version__)
print("Matplotlib Version:", plt.matplotlib.__version__)


# ============================================================
# TASK 2: CREATE AND INITIALIZE RL ENVIRONMENT
# ============================================================

print("\n" + "=" * 60)
print("TASK 2: CREATE AND INITIALIZE RL ENVIRONMENT")
print("=" * 60)

# Create the CartPole-v1 environment
env = gym.make("CartPole-v1")

# Reset the environment
observation, info = env.reset()

print("Initial Observation:")
print(observation)

print("\nEnvironment Information:")
print(info)


# ============================================================
# TASK 3: EXPLORE OBSERVATION AND ACTION SPACES
# ============================================================

print("\n" + "=" * 60)
print("TASK 3: EXPLORE OBSERVATION AND ACTION SPACES")
print("=" * 60)

print("Observation Space:")
print(env.observation_space)

print("\nAction Space:")
print(env.action_space)

print("\nType of Observation Space:")
print(type(env.observation_space))

print("\nNumber of Possible Actions:")
print(env.action_space.n)


# ============================================================
# TASK 4: EXECUTE A RANDOM AGENT
# ============================================================

print("\n" + "=" * 60)
print("TASK 4: EXECUTE A RANDOM AGENT")
print("=" * 60)

# Reset the environment before starting the episode
observation, info = env.reset()

total_reward = 0
step_count = 0

terminated = False
truncated = False

while not (terminated or truncated):

    # Select a random action
    action = env.action_space.sample()

    # Execute the action
    observation, reward, terminated, truncated, info = env.step(action)

    # Update step count and cumulative reward
    step_count += 1
    total_reward += reward

    # Display step information
    print(
        f"Step: {step_count} | "
        f"Action: {action} | "
        f"Observation: {observation} | "
        f"Reward: {reward} | "
        f"Terminated: {terminated} | "
        f"Truncated: {truncated}"
    )


# ============================================================
# FINAL RESULTS
# ============================================================

print("\n" + "=" * 60)
print("EPISODE COMPLETED")
print("=" * 60)

print("Total Number of Steps :", step_count)
print("Cumulative Reward     :", total_reward)

# Close the environment
env.close()

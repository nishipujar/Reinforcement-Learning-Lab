import numpy as np
import random


# ============================================================
# GRIDWORLD CONFIGURATION
# ============================================================

states = ["S1", "S2", "S3", "S4", "S5"]

start_state = 0
terminal_state = 4

gamma = 0.9
theta = 0.0001
max_steps = 20


# ============================================================
# ENVIRONMENT FUNCTION
# ============================================================

def take_action(state, action):
    """
    action:
        -1 = Left
         1 = Right
    """

    # If the state is terminal, no further movement is possible
    if state == terminal_state:
        return state, 0

    next_state = state + action

    # Keep the agent inside the GridWorld
    if next_state < 0:
        next_state = 0

    if next_state > terminal_state:
        next_state = terminal_state

    # Reward structure
    if next_state == terminal_state:
        reward = 10
    else:
        reward = -1

    return next_state, reward


# ============================================================
# TASK 1: FORMULATE GRIDWORLD
# ============================================================

print("=" * 70)
print("TASK 1: GRIDWORLD FORMULATION")
print("=" * 70)

print("States:", states)
print("Start State:", states[start_state])
print("Terminal State:", states[terminal_state])
print("Actions: Left, Right")
print("Normal Movement Reward: -1")
print("Goal Reward: +10")
print("Discount Factor:", gamma)


# ============================================================
# TASK 2: POLICY EVALUATION
# ============================================================

print("\n" + "=" * 70)
print("TASK 2: POLICY EVALUATION")
print("=" * 70)

# Fixed policy:
# S1 -> Right
# S2 -> Right
# S3 -> Left
# S4 -> Right
policy = {
    0: 1,
    1: 1,
    2: -1,
    3: 1
}

# Initial value function
V = np.zeros(len(states))

iteration = 0

print("\nPolicy:")
print("S1 -> Right")
print("S2 -> Right")
print("S3 -> Left")
print("S4 -> Right")
print("S5 -> Terminal")

print("\nIteration | Maximum Change (Delta) | Convergence")

while True:

    iteration += 1

    new_V = V.copy()

    for state in range(len(states) - 1):

        action = policy[state]

        next_state, reward = take_action(state, action)

        new_V[state] = reward + gamma * V[next_state]

    # Terminal state remains zero
    new_V[terminal_state] = 0

    delta = np.max(np.abs(new_V - V))

    convergence = "Converged" if delta < theta else "Not Converged"

    print(
        f"{iteration:9d} | "
        f"{delta:22.6f} | "
        f"{convergence}"
    )

    V = new_V

    if delta < theta:
        break


print("\nFinal Policy Evaluation Values:")

for i, state in enumerate(states):
    print(f"{state}: {V[i]:.4f}")


# ============================================================
# TASK 3: VALUE ITERATION
# ============================================================

print("\n" + "=" * 70)
print("TASK 3: VALUE ITERATION")
print("=" * 70)

V_optimal = np.zeros(len(states))

actions = [-1, 1]

iteration = 0

while True:

    iteration += 1

    new_V = V_optimal.copy()

    for state in range(len(states) - 1):

        action_values = []

        for action in actions:

            next_state, reward = take_action(state, action)

            value = reward + gamma * V_optimal[next_state]

            action_values.append(value)

        new_V[state] = max(action_values)

    new_V[terminal_state] = 0

    delta = np.max(np.abs(new_V - V_optimal))

    V_optimal = new_V

    if delta < theta:
        break


# Determine optimal policy
optimal_policy = {}

for state in range(len(states) - 1):

    action_values = {}

    for action in actions:

        next_state, reward = take_action(state, action)

        action_values[action] = (
            reward + gamma * V_optimal[next_state]
        )

    best_action = max(
        action_values,
        key=action_values.get
    )

    optimal_policy[state] = best_action


print("Value Iteration Converged")
print("Number of Iterations:", iteration)

print("\nOptimal Policy:")

for state in range(len(states) - 1):

    action_name = (
        "Left"
        if optimal_policy[state] == -1
        else "Right"
    )

    print(
        f"{states[state]} -> "
        f"{action_name} | "
        f"Value = {V_optimal[state]:.4f}"
    )

print("S5 -> Terminal | Value = 0.0000")


# ============================================================
# TASK 4: PATH ANALYSIS
# ============================================================

def run_policy(policy_type, selected_policy=None, seed=None):

    if seed is not None:
        random.seed(seed)

    state = start_state

    path = [states[state]]

    total_reward = 0

    for step in range(max_steps):

        # Random policy
        if policy_type == "Random":

            action = random.choice(actions)

        else:

            action = selected_policy[state]

        next_state, reward = take_action(
            state,
            action
        )

        total_reward += reward

        state = next_state

        path.append(states[state])

        if state == terminal_state:

            return (
                path,
                len(path) - 1,
                total_reward,
                "Yes"
            )

    return (
        path,
        max_steps,
        total_reward,
        "No"
    )


# Random policy
random_path, random_length, random_reward, random_goal = run_policy(
    "Random",
    seed=42
)


# Evaluated policy
evaluated_path, evaluated_length, evaluated_reward, evaluated_goal = run_policy(
    "Evaluated",
    policy
)


# Optimal policy
optimal_path, optimal_length, optimal_reward, optimal_goal = run_policy(
    "Optimal",
    optimal_policy
)


# ============================================================
# DISPLAY PATH RESULTS
# ============================================================

print("\n" + "=" * 70)
print("TASK 4: OPTIMAL PATH ANALYSIS")
print("=" * 70)

print("\nRandom Policy:")
print("Path:", " -> ".join(random_path))
print("Path Length:", random_length)
print("Total Reward:", random_reward)
print("Goal Reached:", random_goal)

print("\nEvaluated Policy:")
print("Path:", " -> ".join(evaluated_path))
print("Path Length:", evaluated_length)
print("Total Reward:", evaluated_reward)
print("Goal Reached:", evaluated_goal)

print("\nOptimal Policy:")
print("Path:", " -> ".join(optimal_path))
print("Path Length:", optimal_length)
print("Total Reward:", optimal_reward)
print("Goal Reached:", optimal_goal)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print("Optimal Policy:")

for state in range(len(states) - 1):

    action_name = (
        "Left"
        if optimal_policy[state] == -1
        else "Right"
    )

    print(
        f"{states[state]} -> {action_name}"
    )

print("S5 -> Terminal")

print("\nOptimal Path:")
print(" -> ".join(optimal_path))

print("\nOptimal Path Length:", optimal_length)
print("Optimal Total Reward:", optimal_reward)
print("Goal Reached:", optimal_goal)
# Experiment 3: GridWorld – Policy Evaluation and Value Iteration

## Course

Reinforcement Learning Laboratory

## Course Outcomes

CO2, CO3, CO4

## Objective

To formulate a GridWorld environment as a Reinforcement Learning problem, implement Policy Evaluation and Value Iteration, determine an optimal policy, and compare random, evaluated, and optimal policies.

## GridWorld Environment

A five-state linear GridWorld is used:

S1 → S2 → S3 → S4 → S5

S1 is the starting state and S5 is the terminal goal state.

## Environment Parameters

| Parameter | Value |
|---|---|
| States | S1, S2, S3, S4, S5 |
| Start State | S1 |
| Terminal State | S5 |
| Actions | Left, Right |
| Normal Movement Reward | -1 |
| Goal Reward | +10 |
| Discount Factor | 0.9 |

## Task 1: GridWorld Formulation

The states represent the current location of the agent. The agent can move left or right. A normal movement produces a reward of -1, while reaching the goal state produces a reward of +10.

## Task 2: Policy Evaluation

A fixed policy is evaluated using the Bellman expectation equation.

The policy used is:

- S1 → Right
- S2 → Right
- S3 → Left
- S4 → Right
- S5 → Terminal

The value function is iteratively updated until the maximum change falls below the convergence threshold.

## Task 3: Value Iteration

Value Iteration uses the Bellman Optimality Equation to determine the best action for every state.

The resulting optimal policy is:

- S1 → Right
- S2 → Right
- S3 → Right
- S4 → Right
- S5 → Terminal

The optimal state values are:

| State | Optimal Action | State Value |
|---|---|---:|
| S1 | Right | 4.58 |
| S2 | Right | 6.20 |
| S3 | Right | 8.00 |
| S4 | Right | 10.00 |
| S5 | Terminal | 0.00 |

## Task 4: Path Analysis

The optimal path is:

S1 → S2 → S3 → S4 → S5

The path requires four actions and produces a total reward of 7.

## Bellman Optimality Equation

V*(s) = max_a [R(s,a) + γV*(s')]

## Conclusion

The experiment demonstrated the formulation of a GridWorld environment and the application of Policy Evaluation and Value Iteration. Policy Evaluation estimated the value of states under a fixed policy, while Value Iteration determined the optimal state values and corresponding actions. The optimal policy consistently moved the agent toward the goal and reached it in the minimum number of steps. Random and non-optimal policies could produce inefficient paths or fail to reach the goal. The experiment demonstrates how Bellman equations support policy evaluation and optimal decision-making in Reinforcement Learning.

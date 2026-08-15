# Experiment 1: Exploring Reinforcement Learning Environments using Gymnasium

## Course

Reinforcement Learning Laboratory

## Course Outcome

CO1

## Experiment Objective

To explore and interact with a standard Reinforcement Learning environment using Gymnasium and understand observation spaces, action spaces, rewards, and episode termination.

## Environment Used

CartPole-v1

## Tasks Performed

### Task 1: Environment Setup

- Installed Gymnasium.
- Installed NumPy.
- Installed Matplotlib.
- Imported the required libraries.
- Displayed the Gymnasium version.

### Task 2: Create and Initialize an RL Environment

- Created the CartPole-v1 environment.
- Reset the environment.
- Displayed the initial observation.
- Displayed environment information.

### Task 3: Explore Observation and Action Spaces

- Displayed the observation space.
- Displayed the action space.
- Displayed the type of observation space.
- Displayed the number of possible actions.

### Task 4: Execute a Random Agent

- Selected a random action at every time step.
- Executed one complete episode.
- Displayed the step number.
- Displayed the selected action.
- Displayed the observation.
- Displayed the reward.
- Displayed the termination status.
- Calculated the total number of steps.
- Calculated the cumulative reward.

## Observation Space

CartPole-v1 provides four observation values:

1. Cart Position
2. Cart Velocity
3. Pole Angle
4. Pole Angular Velocity

The observation space is a continuous `Box` space.

## Action Space

CartPole-v1 has two possible actions:

- `0` - Push the cart to the left
- `1` - Push the cart to the right

The action space is `Discrete(2)`.

## Random Agent

The random agent selects an action using:

```python
env.action_space.sample()

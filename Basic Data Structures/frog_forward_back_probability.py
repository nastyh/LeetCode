"""
 If there is a frog which can go one step forward with probability 3/4 
 and one step backward with 1/4. What is expectancy to reach 7 steps forward.

 Func below generalizes the solution
 First returns path
 Second returns steps
 Third return prob of reaching the n-th position

 X = + 1 with prob 3/4
 X = -1 with prob 1/4
 E[X] = 1 * (3/4) + (-1) * (1/4) = 3/4 - 1/4 = 1/2
 T is the number of steps to reach a net displacement of 7
 E[S_t] = E[X] * E[T]
 S_t = 7, E[X] = 1/2
 7 = 1/2 * E[T] --> E[T] = 14
 14 steps are expected 
"""

import random
import matplotlib.pyplot as plt

def simulate_random_walk(n, p_forward=0.75, step_forward=1, step_backward=-1):
    """
    Simulates a random walk for n steps.
    
    Parameters:
    - n: Number of steps to simulate.
    - p_forward: Probability of taking a forward step.
    - step_forward: The increment when stepping forward.
    - step_backward: The increment when stepping backward.
    
    Returns:
    - path: A list containing the cumulative displacement after each step.
    """
    position = 0
    path = [position]
    
    for _ in range(n):
        if random.random() < p_forward:
            position += step_forward
        else:
            position += step_backward
        path.append(position)
    
    return path

def simulate_until_target(target, p_forward=0.75, max_steps=1000):
    """
    Simulates one random walk until the frog reaches the target position or max_steps is reached.
    
    Parameters:
    - target: The target position (positive integer).
    - p_forward: Probability of taking a forward step.
    - max_steps: Maximum number of steps to simulate.
    
    Returns:
    - reached: True if the frog reached the target within max_steps, else False.
    - steps: Number of steps taken (up to max_steps).
    """
    position = 0
    for step in range(1, max_steps+1):
        if random.random() < p_forward:
            position += 1
        else:
            position -= 1
        if position >= target:
            return True, step
    return False, max_steps

def estimate_reach_probability(target, p_forward=0.75, max_steps=1000, trials=10000):
    """
    Estimates the probability of eventually reaching the target position within max_steps.
    
    Parameters:
    - target: The target position (positive integer).
    - p_forward: Probability of taking a forward step.
    - max_steps: Maximum number of steps allowed for each trial.
    - trials: Number of simulation trials.
    
    Returns:
    - probability: The estimated probability of reaching the target.
    - average_steps: Average number of steps taken to reach the target in successful trials.
    """
    successes = 0
    steps_list = []
    for _ in range(trials):
        reached, steps = simulate_until_target(target, p_forward, max_steps)
        if reached:
            successes += 1
            steps_list.append(steps)
    probability = successes / trials
    average_steps = sum(steps_list) / len(steps_list) if steps_list else None
    return probability, average_steps

if __name__ == "__main__":
    # Part 1: Simulate a random walk for a given number of steps and plot the path.
    n_steps = int(input("Enter the number of steps for the path simulation: "))
    p_forward = float(input("Enter the forward probability (e.g., 0.75): "))
    
    path = simulate_random_walk(n_steps, p_forward)
    print("Final displacement after", n_steps, "steps:", path[-1])
    print("Path:", path)
    
    plt.figure(figsize=(10, 5))
    plt.plot(path, marker='o', linestyle='-')
    plt.title("Random Walk Simulation")
    plt.xlabel("Step")
    plt.ylabel("Displacement")
    plt.grid(True)
    plt.show()
    
    # Part 2: Estimate the probability of eventually reaching the target position.
    target_position = int(input("Enter the target position to reach (n): "))
    max_sim_steps = int(input("Enter the maximum steps allowed per trial for reaching the target: "))
    trials = int(input("Enter the number of trials for estimation: "))
    
    probability, avg_steps = estimate_reach_probability(target_position, p_forward, max_sim_steps, trials)
    print(f"Estimated probability of reaching position {target_position} within {max_sim_steps} steps: {probability}")
    if avg_steps is not None:
        print(f"Average steps taken (for successful trials): {avg_steps}")
    else:
        print("No successful trials within the maximum step limit.")

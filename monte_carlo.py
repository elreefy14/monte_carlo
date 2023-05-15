import random

def toss_coin(prob_head=0.5):
    return 'H' if random.random() < prob_head else 'T'

def simulate_tosses(num_tosses=10, prob_head=0.5):
    return [toss_coin(prob_head) for _ in range(num_tosses)]

def monte_carlo_simulation(num_simulations=1000, num_tosses=10, prob_head=0.5):
    head_counts = [0] * (num_tosses + 1)

    for _ in range(num_simulations):
        toss_results = simulate_tosses(num_tosses, prob_head)
        num_heads = toss_results.count('H')
        head_counts[num_heads] += 1

    probabilities = [count / num_simulations for count in head_counts]
    average_heads = sum(num_heads * count for num_heads, count in enumerate(head_counts)) / num_simulations

    return probabilities, average_heads

# Set the parameters
num_simulations = 10000
num_tosses = 10
prob_head = 0.5

# Run the Monte Carlo simulation
probabilities, average_heads = monte_carlo_simulation(num_simulations, num_tosses, prob_head)

# Print the results
print(f"Estimated probabilities of n heads: {probabilities}")
print(f"Estimated average number of heads: {average_heads}")

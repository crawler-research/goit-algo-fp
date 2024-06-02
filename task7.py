import random
import pandas as pd
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_throws):
    counts = [0 for i in range(11)]
    for i in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        counts[dice1 + dice2 - 2] += 1
    probabilities = [count / num_throws for count in counts]
    return probabilities

# Test
num_throws = 100000
probabilities = monte_carlo_dice_simulation(num_throws)

data = {'Сума': range(2, 13), 'Ймовірність': probabilities}
df = pd.DataFrame(data)
print(df)

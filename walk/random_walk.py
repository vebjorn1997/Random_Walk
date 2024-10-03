"""
Project: Random walk
Author: Vebjørn Øglend
Date: 28 September 2024
"""

import matplotlib.pyplot as plt
import random


###### DO NOT change this function #####
# Function to plot the random walk for each animal
def plot_walk(animal):
    xs, ys = zip(*animal["positions"])

    plt.figure(figsize=(10, 10))
    plt.scatter(
        xs,
        ys,
        color=animal["color"],
        edgecolor="k",
        alpha=0.7,
        s=100,
        marker=animal["marker"],
    )
    plt.plot(xs, ys, lw=1.5, ls="--", color=animal["color"])
    plt.grid(True)
    plt.title(f'Path of Random Walk for {animal["name"]}')
    plt.xlabel("East-West")
    plt.ylabel("North-South")

    # Save the plot to a file
    plt.savefig(f'{animal["name"]}_random_walk.png', dpi=300)
    plt.close()  # Close the figure


# You need to create the animal dictionary inside the main function where each animal has
# direction, probabilities, positions, marker and color attributes
# animal = {}


def random_walk(animal):
    last_position = animal["positions"][-1]

    options = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    direction = random.choices(options, weights=animal["probabilities"])
    animal["direction"] = direction
    animal["positions"].append(
        (last_position[0] + direction[0][0], last_position[1] + direction[0][1])
    )


def main():
    chuck_the_chicken = {
        "name": "Chucky",
        "direction": 0,
        "probabilities": [0.25, 0.25, 0.25, 0.25],
        "positions": [(0, 0)],
        "marker": "o",
        "color": "blue",
    }

    daisy_the_dog = {
        "name": "Daisy",
        "direction": 0,
        "probabilities": [0.50, 0.167, 0.167, 0.167],
        "positions": [(0, 0)],
        "marker": "s",
        "color": "red",
    }

    chester_the_cat = {
        "name": "Chester",
        "direction": 0,
        "probabilities": [0.0, 0.0, 0.50, 0.50],
        "positions": [(0, 0)],
        "marker": "<",
        "color": "green",
    }

    for _ in range(1000):
        random_walk(chuck_the_chicken)
        random_walk(daisy_the_dog)
        random_walk(chester_the_cat)
    plot_walk(chuck_the_chicken)
    plot_walk(daisy_the_dog)
    plot_walk(chester_the_cat)


if __name__ == "__main__":
    main()

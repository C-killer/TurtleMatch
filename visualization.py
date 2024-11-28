from collections import Counter
from config import config

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_scatter(results: list[int], title: str = "Scatter Plot of Results") -> None:
    """
    Plots a scatter plot where the x-axis is the total number of turtles obtained,
    and the y-axis is the number of simulations that achieved that total.

    :param results: List of results from simulations.
    :param title: Title for the scatter plot.
    """
    count = Counter(results)
    x = list(count.keys())   # Total number of turtles
    y = list(count.values()) # Number of simulations with that total

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', alpha=0.7, label="Simulation Results")
    plt.title(title, fontsize=16)
    plt.xlabel("Total Number of Turtles Obtained", fontsize=14)
    plt.ylabel(f"Number of Simulations = {config.init_turtles}", fontsize=14)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()


def plot_distribution(results: list[int], title: str = "Distribution of Simulation Results") -> None:
    """
    Plots the distribution of simulation results as a histogram with a density curve.

    :param results: List of results from simulations.
    :param title: Title for the histogram plot.
    """
    mean = float(np.mean(results))  # 转换为标准的 Python float

    plt.figure(figsize=(10, 6))
    sns.histplot(results, kde=True, bins=30, color="blue", alpha=0.7, edgecolor="black")
    plt.axvline(mean, color="red", linestyle="--", label=f"Mean: {mean:.2f}")
    plt.title(title, fontsize=16)
    plt.xlabel(f"Number of Turtles = {config.init_turtles}", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()



def plot_cumulative(results: list[int], title: str = "Cumulative Distribution of Results") -> None:
    """
    Plots the cumulative distribution of simulation results.

    :param results: List of results from simulations.
    :param title: Title for the cumulative distribution plot.
    """
    sorted_results = np.sort(results)
    cumulative = np.cumsum(sorted_results) / np.sum(sorted_results)

    plt.figure(figsize=(10, 6))
    plt.plot(sorted_results, cumulative, marker="o", linestyle="--", color="blue", alpha=0.7)
    plt.title(title, fontsize=16)
    plt.xlabel(f"Total Number of Turtles = {config.init_turtles}", fontsize=14)
    plt.ylabel("Cumulative Probability", fontsize=14)
    plt.grid(alpha=0.3)
    plt.show()


def plot_line(results: list[int], title: str = "Line Chart of Simulation Results") -> None:
    """
    Plots a line chart of simulation results.

    :param results: List of results from simulations.
    :param title: Title for the line chart.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(results)), results, linestyle="-", marker="o", color="green", alpha=0.7)
    plt.title(title, fontsize=16)
    plt.xlabel("Simulation Index", fontsize=14)
    plt.ylabel(f"Total Number of Turtles = {config.init_turtles}", fontsize=14)
    plt.grid(alpha=0.3)
    plt.show()

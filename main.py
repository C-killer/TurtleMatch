from config import config
from simulation import simulate_many
from visualization import plot_scatter, plot_distribution, plot_cumulative, plot_line

# 模拟参数
init_turtles = config.init_turtles
num_simulations = config.num_simulations

# 获取模拟结果
results_data = simulate_many(init_turtles, num_simulations)
results = results_data

# 点云图
plot_scatter(results, title="Scatter Plot of Total Turtles Obtained")

# 直方图
plot_distribution(results, title="Histogram of Total Turtles Obtained")

# 累积分布图
plot_cumulative(results, title="Cumulative Distribution of Total Turtles Obtained")

# 曲线图
plot_line(results, title="Line Chart of Simulation Results")

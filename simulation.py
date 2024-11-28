from collections import Counter
from config import config
import random
random.seed(1234)

def simulate(init_turtles) -> int :
    """
    Simulates the process of unpacking turtles based on their colors, aiming to
    maximize the number of turtles obtained. The process involves unpacking
    turtles and handling them based on whether they match a desired color or
    can be paired off. This method operates until there are no more available
    turtles left to unpack.

    :param init_turtles:
        The initial number of turtle packages available for unpacking.
    :type init_turtles: int

    :return:
        The total number of turtles obtained after completing the unpacking
        process.
    :rtype: int
    """
    nb_total = 0    # 获得的海龟总数
    color_range = list(config.colors)  # 获取颜色范围
    color_wanted = random.choice(color_range).value  # 动态选择颜色
    waiting_list = init_turtles     # 等待拆包的海龟
    table = Counter()      # 桌面上的海龟
    while waiting_list > 0 :
        x = random.choice(color_range).value  # 动态选择颜色
        if x == color_wanted:       # 若为期望颜色，则加拆一包
            waiting_list += 1
        else :
            if table[x] > 0:              # 若能对对碰，加拆一包并移走放入口袋
                waiting_list += 1
                table[x] -= 1
                nb_total += 2
            else :
                table[x] += 1
        waiting_list -= 1
    nb_total += len(table)          # 将桌上剩余海龟收入囊中
    return nb_total

def simulate_many(init_turtles, nb_simulations) -> list:
    """
    Simulates multiple iterations of a turtle coloring simulation. This function
    executes the simulation a specified number of times, using the initial turtle
    setup and the desired color as parameters. The result is a list of outcomes
    from each simulation run.

    :param init_turtles: Initial setup of turtles for the simulation.
    :type init_turtles: int
    :param nb_simulations: The number of times the simulation should be run.
    :type nb_simulations: int
    :return: A list of results from each of the simulations.
    :rtype: list
    """
    return [ simulate(init_turtles) for _ in range(nb_simulations) ]




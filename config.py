from enum import Enum

class TurtleColor(Enum):
    """
    Represents a set of predefined turtle colors as an enumeration.

    The `TurtleColor` enumeration provides a collection of constants
    representing colors commonly used to colorize representations of
    turtles. Each color is associated with a unique integer value.

    This enumeration can be used in applications where these color
    identifiers are needed to manage or refer to specific colors
    in a standardized way, ensuring consistent color usage across
    different parts of a program.

    :ivar RED: Represents the color red.
    :ivar BLUE: Represents the color blue.
    :ivar GREEN: Represents the color green.
    :ivar YELLOW: Represents the color yellow.
    :ivar PURPLE: Represents the color purple.
    :ivar ORANGE: Represents the color orange.
    :ivar BLACK: Represents the color black.
    :ivar WHITE: Represents the color white.
    :ivar GRAY: Represents the color gray.
    :ivar BROWN: Represents the color brown.
    """
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4
    ORANGE = 5
    BLACK = 6
    WHITE = 7
    GRAY = 8
    BROWN = 9

class Config:
    """
    Configuration class for setting simulation parameters.

    This class defines the configuration settings used for running a
    simulation, including the number of simulations to execute, the initial
    number of turtles, and color configuration for turtles. The provided
    attributes allow customization of the simulation environment, enabling
    researchers to adjust scenarios and observe different outcomes based
    on initial conditions.

    :ivar num_simulations: The number of simulation trials to execute.
    :type num_simulations: int
    :ivar init_turtles: The initial quantity of turtles at the start of the simulation.
    :type init_turtles: int
    :ivar colors: The configuration for turtle colors used in the simulation.
    :type colors: TurtleColor
    """
    def __init__(self):
        self.num_simulations = 100000     # 模拟试验次数
        self.init_turtles = 50          # 初始的海龟数量
        self.colors = TurtleColor

config = Config()

from dataclasses import dataclass
from typing import Tuple
from random import randrange
from agents import Agent


@dataclass
class Tile:
    coord: Tuple


@dataclass
class Grid:
    x_size: int
    y_size: int

    def __post_init__(self):
        self.grid = [
            [Tile((x, y)) for x in range(self.x_size)] for y in range(self.y_size)
        ]


@dataclass
class World:
    n_agents: int
    _x_size: int = 128
    _y_size: int = 128
    life_time: int = 100
    time_step: int = 0

    def __post_init__(self):
        self.grid = Grid(self.x_size, self.y_size)
        self.agents = [
            Agent([randrange(self.x_size), randrange(self.y_size)])
            for _ in range(self.n_agents)
        ]

    @property
    def x_size(self) -> int:
        return self._x_size

    @x_size.setter
    def x_size(self, v: int) -> None:
        self._x_size = v

    @property
    def y_size(self) -> int:
        return self._y_size

    @y_size.setter
    def y_size(self, v: int) -> None:
        self._y_size = v

    def get_state(self) -> list:
        return self.agents

    def reset_agent_location(self, agent):
        x = randrange(self.x_size)
        y = randrange(self.y_size)
        agent.set_coordinates(x, y)

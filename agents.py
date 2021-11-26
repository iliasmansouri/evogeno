from dataclasses import dataclass
from typing import Tuple
from genes import Genome
from brain import Brain


@dataclass
class AgentState:
    coord: Tuple


@dataclass
class Agent:
    coord: Tuple
    mutation_proability: float = 0.001

    def __post_init__(self):
        self.genome = Genome()
        self.brain = Brain(self.genome)

    def execute(self):
        decisions = self.brain.execute(self.state())
        self.update_state(decisions)

    def update_state(self, decisions):
        x, y = self.coord
        if decisions:
            for k, v in decisions.items():
                if v > 0.5:
                    if str(k) == "move_left":
                        x = x - 1 if x > 0 else x
                    elif str(k) == "move_right":
                        x = x + 1 if x < 128 else x
                    elif str(k) == "move_back":
                        y = y + 1 if y < 128 else y
                    elif str(k) == "move_forward":
                        y = y - 1 if y > 0 else y
            self.coord = (x, y)

    def state(self):
        return {"coord": self.coord}

    def mutate(self):
        for gene in self.genome.genes:
            gene.mutate(self.mutation_proability)

    def die(self):
        pass

    def duplicate(self):
        self.mutate()

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    @property
    def coord(self):
        return self.__coord

    @coord.setter
    def coord(self, val):
        x, y = val
        x = 0 if x < 0 else x
        y = 0 if y < 0 else y
        self.__coord = (x, y)

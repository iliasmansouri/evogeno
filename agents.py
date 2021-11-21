from dataclasses import dataclass
from typing import Tuple
from genes import Genome
from brain import Brain

@dataclass
class Actions:
    pass


@dataclass
class Agent:
    coord: Tuple
    mutation_proability:float = 0.001

    def __post_init__(self):
        self.genome = Genome()
        self.brain = Brain(self.genome)

    def execute(self):
        self.coord = self.brain.execute(self.state())

    def state(self):
        return {"coord": self.coord}

    def mutate(self):
        for gene in self.genome.genes:
            gene.mutate(self.mutation_proability)

    def die(self):
        pass

    def duplicate(self):
        self.mutate()

    def set_coordinates(self,x,y):
        self.coord = (x,y)
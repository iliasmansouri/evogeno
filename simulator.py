from dataclasses import dataclass
from world import World
from visualize import Visualizer


@dataclass
class Sim:
    n_agents: int = 5000
    max_time_steps: int = 10000
    x_size: int = 128
    y_size: int = 128

    def __post_init__(self):
        self.world = World(self.n_agents, self.x_size, self.y_size)
        self.viz = Visualizer(self.world)

    def run(self):
        self.viz.run()


if __name__ == "__main__":
    sim = Sim()
    sim.run()

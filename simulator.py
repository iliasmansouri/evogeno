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
        self.viz = Visualizer(self.x_size, self.y_size)

    def run(self):        
        if self.world.time_step % self.world.life_time == 0:
            for agent in self.world.agents:
                if agent.coord[0] < 64:
                    agent.duplicate()
                    self.world.reset_agent_location(agent)
                else:
                    agent.die()
                    self.world.agents.remove(agent)
        else:
            for agent in self.world.agents:
                agent.execute()
        self.world.time_step += 1
        self.viz.run_step(self.world.agents)


if __name__ == "__main__":
    sim = Sim()
    while True:
        sim.run()

from dataclasses import dataclass
import pygame
from world import World

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


@dataclass
class Visualizer:
    world: World
    cell_size: int = 7
    axis_labels: bool = False
    grid_coord_margin_size: int = 10
    fps: int = 1
    surface = pygame.display.set_mode(flags=pygame.RESIZABLE)

    def __post_init__(self):
        self.col_nb = self.world.x_size
        self.row_nb = self.world.y_size
        pygame.init()
        self.grid = [[0 for i in range(self.col_nb)] for j in range(self.row_nb)]
        self.font = pygame.font.SysFont("arial", 12, False)
        self.clock = pygame.time.Clock()
        self.running = True

    def draw_rectangle(self):
        for li in range(self.row_nb):
            li_coord = self.grid_coord_margin_size + li * self.cell_size
            if self.axis_labels:
                if li < 10:
                    ident = "   "
                else:
                    ident = "  "
                text = self.font.render(ident + str(li), 1, (0, 0, 0))
                self.surface.blit(text, (0, li_coord))
            for co in range(self.col_nb):
                col_coord = self.grid_coord_margin_size + co * self.cell_size
                if self.axis_labels:
                    if co < 10:
                        ident = "  "
                    else:
                        ident = " "
                    text = self.font.render(ident + str(co), 1, (0, 0, 0))
                    self.surface.blit(text, (col_coord, 1))
                pygame.draw.rect(
                    self.surface,
                    BLACK,
                    pygame.Rect(li_coord, col_coord, self.cell_size, self.cell_size),
                    1,
                )

    def draw_agents(self, agents):
        for agent in agents:
            x = (
                self.grid_coord_margin_size
                + agent.coord[0] * self.cell_size
                - self.cell_size // 2
            )
            y = (
                self.grid_coord_margin_size
                + agent.coord[1] * self.cell_size
                - self.cell_size // 2
            )
            pygame.draw.circle(self.surface, (255, 0, 0), (x, y), radius=5)

    def run(self):
        while self.running:
            # self.clock.tick(self.fps)
            self.world.step()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(WHITE)

            self.draw_agents(self.world.agents)
            self.draw_rectangle()

            pygame.display.flip()

        pygame.quit()

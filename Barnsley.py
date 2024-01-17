import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import random

class BarnsleyFernViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def render_barnsley_fern(self, num_points):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 1.0, 0.0)
        glPointSize(1.0)

        x, y = 0, 0

        glBegin(GL_POINTS)
        for _ in range(num_points):
            r = random.uniform(0, 100)

            if r < 1:
                x, y = 0, 0.16 * y
            elif r < 86:
                x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
            elif r < 93:
                x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
            else:
                x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

            screen_x = int((x + 2.5) * (self.width / 5))
            screen_y = int((y - 1) * (self.height / 10))
            glVertex2f(screen_x, screen_y)
        glEnd()
        glFlush()

    def show(self):
        pygame.init()
        display = (self.width, self.height)
        self.screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

        gluOrtho2D(0, self.width, 0, self.height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.render_barnsley_fern(num_points=50000)
            pygame.display.flip()

if __name__ == "__main__":
    viewer = BarnsleyFernViewer(800, 800)
    viewer.show()

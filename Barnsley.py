import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Set up window size
window_width = 800
window_height = 800

def barnsley_fern(n_points):
    points = np.zeros((n_points, 2))
    x, y = 0, 0

    for i in range(n_points - 1):
        r = np.random.random()

        if r <= 0.01:
            x, y = 0, 0.16 * y
        elif r <= 0.86:
            new_x = 0.85 * x + 0.04 * y
            new_y = -0.04 * x + 0.85 * y + 1.6
            x, y = new_x, new_y
        elif r <= 0.93:
            new_x = 0.2 * x - 0.26 * y
            new_y = 0.23 * x + 0.22 * y + 1.6
            x, y = new_x, new_y
        else:
            new_x = -0.15 * x + 0.28 * y
            new_y = 0.26 * x + 0.24 * y + 0.44
            x, y = new_x, new_y

        points[i + 1] = [x, y]

    return points

def draw_barnsley_fern(points):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_POINTS)
    for i in range(len(points)):
        x, y = points[i]
        glVertex2f((x + 2.182) * (window_width / 9.998), (y - 9.9983) * (window_height / 14.286))
    glEnd()

    glFlush()

def main():
    pygame.init()
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    n_points = 100000
    fern_points = barnsley_fern(n_points)

    gluOrtho2D(-window_width / 2, window_width / 2, -window_height / 2, window_height / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_barnsley_fern(fern_points)
        pygame.display.flip()

if __name__ == "__main__":
    main()

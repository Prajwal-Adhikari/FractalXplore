import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Set up window size
window_width = 800
window_height = 800

def hilbert(n, d, p0, p1, p2, p3):
    if n <= 0:
        draw_line(p0, p1)
        draw_line(p1, p2)
        draw_line(p2, p3)
        return

    mid = lambda a, b: ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    hilbert(n - 1, d, p0, mid(p0, p3), mid(p0, p1), mid(p0, p3))
    hilbert(n - 1, d, mid(p0, p1), p1, mid(p1, p2), mid(p1, p0))
    hilbert(n - 1, d, mid(p1, p2), mid(p1, p0), p2, mid(p2, p1))
    hilbert(n - 1, d, mid(p2, p3), mid(p2, p1), mid(p2, p3), p3)
    hilbert(n - 1, d, mid(p3, p0), mid(p3, p2), mid(p3, p0), p3)


def draw_line(p0, p1):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(p0[0], p0[1])
    glVertex2f(p1[0], p1[1])
    glEnd()


def main():
    pygame.init()
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, window_width, 0, window_height)

    depth = 5  # Adjust the depth to change the level of detail
    p0 = (100, 100)
    p1 = (700, 100)
    p2 = (700, 700)
    p3 = (100, 700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        hilbert(depth, 2, p0, p1, p2, p3)
        pygame.display.flip()

if __name__ == "__main__":
    main()

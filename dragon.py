import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Set up window size
window_width = 1920
window_height = 1080

def dragon_curve(n):
    sequence = [1]
    for i in range(n):
        sequence = sequence + [1] + [bit ^ 1 for bit in reversed(sequence)]
    return sequence

def draw_dragon_curve(n, scale):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    dragon_sequence = dragon_curve(n)
    angle = np.pi / 2
    x, y = 0, 0

    glBegin(GL_LINES)
    for step in dragon_sequence:
        angle += np.pi / 2 if step == 0 else -np.pi / 2
        new_x = x + scale * np.cos(angle)
        new_y = y + scale * np.sin(angle)
        glVertex2f(x, y)
        glVertex2f(new_x, new_y)
        x, y = new_x, new_y
    glEnd()

    glFlush()

def main():
    pygame.init()
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    level = 15    # Change the level for more iterations
    scale = 0.1     # Initial scale

    gluOrtho2D(-1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_dragon_curve(level, scale)
        pygame.display.flip()

if __name__ == "__main__":
    main()

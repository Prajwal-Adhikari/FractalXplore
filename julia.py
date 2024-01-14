# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import numpy as np

# # Set up window size
# window_width = 800
# window_height = 800

# def julia(c_real, c_imag, max_iteration):
#     # Set up iteration count and escape radius
#     escape_radius = 4
#     z_real, z_imag = np.meshgrid(np.linspace(-2, 2, window_width), np.linspace(-2, 2, window_height))
#     c = c_real + c_imag * 1j
#     z = z_real + z_imag * 1j
#     iterations = np.zeros_like(z, dtype=np.uint32)

#     for i in range(max_iteration):
#         z = z * z + c
#         mask = np.abs(z) < escape_radius
#         iterations += mask
#     return iterations

# def draw_julia(c_real, c_imag):
#     max_iteration = 100
#     iterations = julia(c_real, c_imag, max_iteration)

#     glClearColor(0.0, 0.0, 0.0, 1.0)
#     glClear(GL_COLOR_BUFFER_BIT)
#     glPointSize(1.0)

#     glBegin(GL_POINTS)
#     for y in range(window_height):
#         for x in range(window_width):
#             iteration = iterations[y, x]
#             brightness = 1 - iteration / max_iteration
#             glColor3f(brightness, brightness, brightness)
#             glVertex2f((x - window_width / 2) / (window_width / 4), (y - window_height / 2) / (window_height / 4))
#     glEnd()
#     glFlush()

# def main():
#     pygame.init()
#     display = (window_width, window_height)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#     c_real = -0.7
#     c_imag = 0.27015

#     gluOrtho2D(-2, 2, -2, 2)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         draw_julia(c_real, c_imag)
#         pygame.display.flip()

# if __name__ == "__main__":
#     main()


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Set up window size
window_width = 800
window_height = 800

def julia(c_real, c_imag, max_iteration):
    # Set up iteration count and escape radius
    escape_radius = 4
    z_real, z_imag = np.meshgrid(np.linspace(-2, 2, window_width), np.linspace(-2, 2, window_height))
    c = c_real + c_imag * 1j
    z = z_real + z_imag * 1j
    iterations = np.zeros_like(z, dtype=np.uint32)

    for i in range(max_iteration):
        z = z * z + c
        mask = np.abs(z) < escape_radius
        iterations += mask
    return iterations

def draw_julia(c_real, c_imag):
    max_iteration = 100
    iterations = julia(c_real, c_imag, max_iteration)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1.0)

    glBegin(GL_POINTS)
    for y in range(window_height):
        for x in range(window_width):
            iteration = iterations[y, x]
            brightness = 1 - iteration / max_iteration
            glColor3f(brightness, brightness, brightness)
            glVertex2f((x - window_width / 2) / (window_width / 4), (y - window_height / 2) / (window_height / 4))
    glEnd()
    glFlush()

def zoom(c_real, c_imag, x, y, zoom_factor):
    new_c_real = (x - window_width / 2) / (window_width / 4)
    new_c_imag = (y - window_height / 2) / (window_height / 4)
    c_real += new_c_real / zoom_factor
    c_imag += new_c_imag / zoom_factor
    return c_real, c_imag

def main():
    pygame.init()
    display = (window_width, window_height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    c_real = -0.7
    c_imag = 0.27015
    zoom_factor = 1.0

    gluOrtho2D(-2, 2, -2, 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    c_real, c_imag = zoom(c_real, c_imag, mouse_x, mouse_y, zoom_factor)
                    zoom_factor *= 2.0  # Increase zoom factor after each click for deeper zoom

        draw_julia(c_real, c_imag)
        pygame.display.flip()

if __name__ == "__main__":
    main()

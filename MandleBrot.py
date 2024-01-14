# import pygame
# from pygame.locals import *
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *

# # Set up window size
# window_width = 800
# window_height = 800

# # Define parameters for the Mandelbrot Set
# max_iteration = 50
# min_x, max_x = -2.0, 2.0
# min_y, max_y = -2.0, 2.0

# def mandelbrot(c_real, c_imag):
#     z_real, z_imag = 0, 0
#     for i in range(max_iteration):
#         z_real, z_imag = z_real * z_real - z_imag * z_imag + c_real, 2 * z_real * z_imag + c_imag
#         if z_real * z_real + z_imag * z_imag > 4:
#             return i
#     return max_iteration

# def draw_mandelbrot():
#     glClearColor(0.0, 0.0, 0.0, 1.0)
#     glClear(GL_COLOR_BUFFER_BIT)
#     glPointSize(1.0)

#     glBegin(GL_POINTS)
#     for y in range(window_height):
#         for x in range(window_width):
#             c_real = min_x + (max_x - min_x) * x / (window_width - 1)
#             c_imag = min_y + (max_y - min_y) * y / (window_height - 1)

#             iteration = mandelbrot(c_real, c_imag)
#             brightness = 1 - iteration / max_iteration
#             glColor3f(brightness, brightness, brightness)
#             glVertex2f(x, y)
#     glEnd()
#     glFlush()

# def resize(width, height):
#     glViewport(0, 0, width, height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0, width, 0, height, -1, 1)
#     glMatrixMode(GL_MODELVIEW)



# #zoom
# zoom_factor = 2.0  # Factor by which to zoom in

# def handle_mouse_click(mouse_x, mouse_y):
#     global min_x, max_x, min_y, max_y
#     selected_cx = min_x + (max_x - min_x) * mouse_x / window_width
#     selected_cy = min_y + (max_y - min_y) * (window_height - mouse_y) / window_height

#     # Calculate new boundaries for zoomed area
#     new_width = (max_x - min_x) / zoom_factor
#     new_height = (max_y - min_y) / zoom_factor
#     min_x = selected_cx - new_width / 2
#     max_x = selected_cx + new_width / 2
#     min_y = selected_cy - new_height / 2
#     max_y = selected_cy + new_height / 2


# def mandelbrot_stats():
#     # Calculate current viewing window coordinates
#     current_width = max_x - min_x
#     current_height = max_y - min_y
#     center_x = min_x + current_width / 2
#     center_y = min_y + current_height / 2

#     # Calculate and display statistics
#     stats = f"Viewing Window: ({min_x:.6f}, {max_x:.6f}), ({min_y:.6f}, {max_y:.6f})\n" \
#             f"Center: ({center_x:.6f}, {center_y:.6f})\n" \
#             f"Iteration Count: {max_iteration}"
#     font = pygame.font.Font(None, 20)
#     text_surface = font.render(stats, True, (255, 0, 0))
#     text_rect = text_surface.get_rect()
#     text_rect.topleft = (10, 10)
#     pygame.display.get_surface().blit(text_surface, text_rect)


# def main():
#     pygame.init()
#     display = (window_width, window_height)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#     resize(window_width, window_height)

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button clicked
#                     mouse_x, mouse_y = pygame.mouse.get_pos()
#                     handle_mouse_click(mouse_x, mouse_y)


#         draw_mandelbrot()
#         glFlush()
#         mandelbrot_stats()
#         pygame.display.flip()

# if __name__ == "__main__":
#     main()



# import pygame
# from OpenGL.GL import *
# from OpenGL.GLU import *

# class MandelbrotViewer:
#     def __init__(self, screen, width, height):
#         self.screen = screen
#         self.width = width
#         self.height = height
#         self.min_x, self.max_x = -2.0, 2.0
#         self.min_y, self.max_y = -2.0, 2.0
#         self.zoom_factor = 2.0
#         self.max_iteration = 50

#     def render_mandelbrot(self):
#         glClearColor(0.0, 0.0, 0.0, 1.0)
#         glClear(GL_COLOR_BUFFER_BIT)
#         glPointSize(1.0)

#         glBegin(GL_POINTS)
#         for y in range(self.height):
#             for x in range(self.width):
#                 c_real = self.min_x + (self.max_x - self.min_x) * x / (self.width - 1)
#                 c_imag = self.min_y + (self.max_y - self.min_y) * y / (self.height - 1)

#                 iteration = self.calculate_mandelbrot(c_real, c_imag)
#                 brightness = 1 - iteration / self.max_iteration
#                 glColor3f(brightness, brightness, brightness)
#                 glVertex2f(x, y)
#         glEnd()
#         glFlush()

#     def calculate_mandelbrot(self, c_real, c_imag):
#         z_real, z_imag = 0, 0
#         for i in range(self.max_iteration):
#             z_real, z_imag = z_real * z_real - z_imag * z_imag + c_real, 2 * z_real * z_imag + c_imag
#             if z_real * z_real + z_imag * z_imag > 4:
#                 return i
#         return self.max_iteration

#     def resize(self, width, height):
#         glViewport(0, 0, width, height)
#         glMatrixMode(GL_PROJECTION)
#         glLoadIdentity()
#         glOrtho(0, width, 0, height, -1, 1)
#         glMatrixMode(GL_MODELVIEW)

#     def handle_mouse_click(self, mouse_x, mouse_y):
#         selected_cx = self.min_x + (self.max_x - self.min_x) * mouse_x / self.width
#         selected_cy = self.min_y + (self.max_y - self.min_y) * (self.height - mouse_y) / self.height

#         # Calculate new boundaries for the zoomed area
#         new_width = (self.max_x - self.min_x) / self.zoom_factor
#         new_height = (self.max_y - self.min_y) / self.zoom_factor
#         self.min_x = selected_cx - new_width / 2
#         self.max_x = selected_cx + new_width / 2
#         self.min_y = selected_cy - new_height / 2
#         self.max_y = selected_cy + new_height / 2

#     def show(self):
#         self.render_mandelbrot()
#         pygame.display.flip()



# mandelbrot_set.py

# import pygame
# from OpenGL.GL import *
# from OpenGL.GLU import *

# class MandelbrotViewer:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.min_x, self.max_x = -2.0, 2.0
#         self.min_y, self.max_y = -2.0, 2.0
#         self.zoom_factor = 2.0
#         self.max_iteration = 50

#     def render_mandelbrot(self):
#         glClearColor(0.0, 0.0, 0.0, 1.0)
#         glClear(GL_COLOR_BUFFER_BIT)
#         glPointSize(1.0)

#         glBegin(GL_POINTS)
#         for y in range(self.height):
#             for x in range(self.width):
#                 c_real = self.min_x + (self.max_x - self.min_x) * x / (self.width - 1)
#                 c_imag = self.min_y + (self.max_y - self.min_y) * y / (self.height - 1)

#                 iteration = self.calculate_mandelbrot(c_real, c_imag)
#                 brightness = 1 - iteration / self.max_iteration
#                 glColor3f(brightness, brightness, brightness)
#                 glVertex2f(x, y)
#         glEnd()
#         glFlush()

#     def calculate_mandelbrot(self, c_real, c_imag):
#         z_real, z_imag = 0, 0
#         for i in range(self.max_iteration):
#             z_real, z_imag = z_real * z_real - z_imag * z_imag + c_real, 2 * z_real * z_imag + c_imag
#             if z_real * z_real + z_imag * z_imag > 4:
#                 return i
#         return self.max_iteration

#     def resize(self, width, height):
#         glViewport(0, 0, width, height)
#         glMatrixMode(GL_PROJECTION)
#         glLoadIdentity()
#         glOrtho(0, width, 0, height, -1, 1)
#         glMatrixMode(GL_MODELVIEW)

#     def handle_mouse_click(self, mouse_x, mouse_y):
#         selected_cx = self.min_x + (self.max_x - self.min_x) * mouse_x / self.width
#         selected_cy = self.min_y + (self.max_y - self.min_y) * (self.height - mouse_y) / self.height

#         # Calculate new boundaries for the zoomed area
#         new_width = (self.max_x - self.min_x) / self.zoom_factor
#         new_height = (self.max_y - self.min_y) / self.zoom_factor
#         self.min_x = selected_cx - new_width / 2
#         self.max_x = selected_cx + new_width / 2
#         self.min_y = selected_cy - new_height / 2
#         self.max_y = selected_cy + new_height / 2

#     def show_mandelbrot(self):
#         pygame.init()
#         display = (self.width, self.height)
#         pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

#         self.resize(self.width, self.height)

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if event.button == 1:  # Left mouse button clicked
#                         mouse_x, mouse_y = pygame.mouse.get_pos()
#                         self.handle_mouse_click(mouse_x, mouse_y)

#             self.render_mandelbrot()
#             glFlush()
#             pygame.display.flip()

# if __name__ == "__main__":
#     viewer = MandelbrotViewer(800, 800)
#     viewer.show_mandelbrot()



# mandelbrot_set.py

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class MandelbrotViewer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.min_x, self.max_x = -2.0, 2.0
        self.min_y, self.max_y = -2.0, 2.0
        self.zoom_factor = 2.0
        self.max_iteration = 50

    def render_mandelbrot(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(1.0)

        glBegin(GL_POINTS)
        for y in range(self.height):
            for x in range(self.width):
                c_real = self.min_x + (self.max_x - self.min_x) * x / (self.width - 1)
                c_imag = self.min_y + (self.max_y - self.min_y) * y / (self.height - 1)

                iteration = self.calculate_mandelbrot(c_real, c_imag)
                brightness = 1 - iteration / self.max_iteration
                glColor3f(brightness, brightness, brightness)
                glVertex2f(x, y)
        glEnd()
        glFlush()

    def calculate_mandelbrot(self, c_real, c_imag):
        z_real, z_imag = 0, 0
        for i in range(self.max_iteration):
            z_real, z_imag = z_real * z_real - z_imag * z_imag + c_real, 2 * z_real * z_imag + c_imag
            if z_real * z_real + z_imag * z_imag > 4:
                return i
        return self.max_iteration

    def resize(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def handle_mouse_click(self, mouse_x, mouse_y):
        selected_cx = self.min_x + (self.max_x - self.min_x) * mouse_x / self.width
        selected_cy = self.min_y + (self.max_y - self.min_y) * (self.height - mouse_y) / self.height

        # Calculate new boundaries for the zoomed area
        new_width = (self.max_x - self.min_x) / self.zoom_factor
        new_height = (self.max_y - self.min_y) / self.zoom_factor
        self.min_x = selected_cx - new_width / 2
        self.max_x = selected_cx + new_width / 2
        self.min_y = selected_cy - new_height / 2
        self.max_y = selected_cy + new_height / 2

    def show(self):
        pygame.init()
        display = (self.width, self.height)
        pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

        self.resize(self.width, self.height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        self.handle_mouse_click(mouse_x, mouse_y)

            self.render_mandelbrot()
            glFlush()
            pygame.display.flip()

if __name__ == "__main__":
    viewer = MandelbrotViewer(800, 800)
    viewer.show()

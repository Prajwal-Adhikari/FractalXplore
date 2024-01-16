import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class JuliaViewer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.min_x, self.max_x = -2.0, 2.0
        self.min_y, self.max_y = -2.0, 2.0
        self.zoom_factor = 2.0
        self.max_iteration = 50
        self.c_real, self.c_imag = -0.7, 0.27015  # Default Julia set parameters

    def render_julia(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(1.0)

        glBegin(GL_POINTS)
        for y in range(self.height):
            for x in range(self.width):
                z_real = self.min_x + (self.max_x - self.min_x) * x / (self.width - 1)
                z_imag = self.min_y + (self.max_y - self.min_y) * y / (self.height - 1)

                iteration = self.calculate_julia(z_real, z_imag)
                brightness = 1 - iteration / self.max_iteration
                glColor3f(brightness, brightness, brightness)
                glVertex2f(x, y)
        glEnd()
        glFlush()

    def calculate_julia(self, z_real, z_imag):
        for i in range(self.max_iteration):
            z_real, z_imag = z_real * z_real - z_imag * z_imag + self.c_real, 2 * z_real * z_imag + self.c_imag
            if z_real * z_real + z_imag * z_imag > 4:
                return i
        return self.max_iteration

    def draw_axes(self):
        glColor3f(1.0, 0.0, 0.0)  # Red color for axes
        glBegin(GL_LINES)
        # X-axis
        glVertex2f(0, self.height / 2)
        glVertex2f(self.width, self.height / 2)
        # Y-axis
        glVertex2f(self.width / 2, 0)
        glVertex2f(self.width / 2, self.height)
        glEnd()

    def display_stats(self):
        font = pygame.font.Font(None, 36)
        stats_surface = font.render(f"Iterations: {self.max_iteration}", True, (0,0,0))
        self.screen.blit(stats_surface, (10, 10))
        c_params_surface = font.render(f"Julia Set Parameters: ({self.c_real}, {self.c_imag})", True, (0,0,0))
        self.screen.blit(c_params_surface, (10, 50))

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
        self.screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

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

            self.render_julia()
            self.draw_axes()
            self.display_stats()
            glFlush()
            pygame.display.flip()

if __name__ == "__main__":
    viewer = JuliaViewer(800, 800)
    viewer.show()

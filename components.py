import pygame
from OpenGL.GL import *
import sys

class Popup:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self, popup_text, width, height):
        popup_rect = pygame.Rect(width // 4, height // 4, width // 2, height // 2)
        popup_bg_color = (220, 220, 220)
        border_radius = 10

        pygame.draw.rect(self.screen, popup_bg_color, popup_rect, border_radius=border_radius)

        instruction_font = pygame.font.Font(None, 30)

        y_offset = popup_rect.top + 30
        for line in popup_text:
            text_render = instruction_font.render(line, True, (0, 0, 0))
            text_rect = text_render.get_rect(topleft=(popup_rect.left + 30, y_offset))
            self.screen.blit(text_render, text_rect)
            y_offset += 30

        return popup_rect

class FractalSelectionMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self, width, height):
        menu_rect = pygame.Rect(width // 4, height // 4, width // 2, height // 2)
        menu_bg_color = (220, 220, 220)
        border_radius = 10

        pygame.draw.rect(self.screen, menu_bg_color, menu_rect, border_radius=border_radius)

        menu_font = pygame.font.Font(None, 30)

        options = [
            "Select a Fractal:",
            "1. Mandelbrot Set",
            "2. Julia Set",
            "3. Dragon Set",
        ]

        y_offset = menu_rect.top + 30
        for line in options:
            text_render = menu_font.render(line, True, (0, 0, 0))
            text_rect = text_render.get_rect(topleft=(menu_rect.left + 30, y_offset))
            self.screen.blit(text_render, text_rect)
            y_offset += 30

        return menu_rect

class HelloWindow:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)

    def show(self):
        self.screen.fill((255, 255, 255))  # Fill the screen with white color

        # Text rendering for "Hello"
        hello_text = self.font.render("Hello!", True, (0, 0, 0))  # Black text color
        hello_text_rect = hello_text.get_rect(center=(self.width // 2, self.height // 2))

        self.screen.blit(hello_text, hello_text_rect)
        pygame.display.flip()  # Update the display to show the "Hello" message

        waiting_for_close = True
        while waiting_for_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting_for_close = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        x, y = event.pos
                        if hello_text_rect.collidepoint(x, y):
                            waiting_for_close = False

            pygame.time.Clock().tick(60)

        self.screen.fill((0, 0, 0))  # Fill the screen with black color
        pygame.display.flip()  

class Homepage:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self):
        homepage_rect = pygame.Rect(0, 0, self.width, self.height)
        homepage_bg_color = (0, 0, 0)

        pygame.draw.rect(self.screen, homepage_bg_color, homepage_rect)

        return homepage_rect



class MandelbrotViewer:
    def __init__(self, width, height):
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
        stats_surface = font.render(f"Iterations: {self.max_iteration}", True, (255, 255, 255))
        pygame.display.get_surface().blit(stats_surface, (10, 10))

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
            self.draw_axes()
            self.display_stats()
            glFlush()
            pygame.display.flip()




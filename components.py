import pygame
from MandleBrot import MandelbrotViewer
from julia import JuliaViewer  # Import JuliaViewer from your JuliaSet module
from Barnsley import BarnsleyFernViewer
class Popup:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)

    def show(self, text, width, height):
        popup_rect = pygame.Rect(width // 4, height // 4, width // 2, height // 2)
        pygame.draw.rect(self.screen, (255, 255, 255), popup_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), popup_rect, 5)

        for i, line in enumerate(text):
            text_surface = self.font.render(line, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(popup_rect.centerx, popup_rect.top + 50 + i * 40))
            self.screen.blit(text_surface, text_rect)

        return popup_rect

class FractalSelectionMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.menu_items = ["Mandelbrot Set", "Julia Set", "Barnsley Fern"]  # Add any other fractal names as needed
        self.selected_fractal = None

    def show(self, width, height):
        button_width = 200  # Adjust the width of each button
        button_gap = 20  # Adjust the horizontal gap between buttons

        total_menu_width = 50 + len(self.menu_items) * (button_width + button_gap)
        menu_rect = pygame.Rect((width - total_menu_width) // 2, height // 4, total_menu_width, height // 2)

        pygame.draw.rect(self.screen, (255, 255, 255), menu_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), menu_rect, 5)

        for i, item in enumerate(self.menu_items):
            item_rect = pygame.Rect(menu_rect.left + 50 + i * (button_width + button_gap), menu_rect.top + 50, button_width, 40)
            pygame.draw.rect(self.screen, (150, 150, 150), item_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), item_rect, 2)

            text = self.font.render(item, True, (0, 0, 0))
            text_rect = text.get_rect(center=item_rect.center)
            self.screen.blit(text, text_rect)

            if item_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, (255, 0, 0), item_rect, 2)

                if pygame.mouse.get_pressed()[0] and not self.selected_fractal:
                    self.selected_fractal = item

        return menu_rect

    def get_selected_fractal(self):
        return self.selected_fractal

    def reset_selected_fractal(self):
        self.selected_fractal = None

class HelloWindow:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("Hello! Welcome to FractalXplore!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

class Homepage:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def show(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("This is the homepage. Enjoy exploring fractals!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

class FractalViewerController:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.fractal_viewer = None

    def set_fractal_viewer(self, fractal_name):
        if fractal_name == "Julia Set":
            self.fractal_viewer = JuliaViewer(self.width, self.height)  # Create JuliaViewer instance
        elif fractal_name == "Mandelbrot Set":
            self.fractal_viewer = MandelbrotViewer(self.width, self.height)
        elif fractal_name == "Barnsley Fern":
            self.fractal_viewer = BarnsleyFernViewer(self.width, self.height)

    def show_fractal_viewer(self):
        if self.fractal_viewer:
            self.fractal_viewer.show()
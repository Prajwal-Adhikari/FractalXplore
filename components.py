import pygame
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

# class HelloWindow:
#     def __init__(self, screen, width, height):
#         self.screen = screen
#         self.width = width
#         self.height = height

#     def show(self):
#         self.screen.fill((255, 255, 255))

#         hello_font = pygame.font.Font(None, 36)
#         hello_text = hello_font.render("Hello!", True, (0, 0, 0))
#         hello_text_rect = hello_text.get_rect(center=(self.width // 2, self.height // 2))

#         self.screen.blit(hello_text, hello_text_rect)

#         pygame.display.flip()
#         pygame.time.wait(2000)
#         self.screen.fill((0, 0, 0))

#         return hello_text_rect

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

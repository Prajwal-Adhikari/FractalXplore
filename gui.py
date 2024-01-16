# import pygame
# import cv2
# from components import Popup, FractalSelectionMenu, HelloWindow, Homepage 
# from MandleBrot import MandelbrotViewer

# # Pygame setup
# pygame.init()
# width, height = 1280, 800
# screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
# pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

# # Load the title image
# title_image = pygame.image.load("title.png").convert_alpha()

# clock = pygame.time.Clock()
# running = True
# is_maximized = False
# selected_fractal = None

# # OpenCV video capture
# video = cv2.VideoCapture("bgvideo.mp4")

# button_font = pygame.font.Font(None, 36)
# button_text_color = (0, 0, 0)
# button_bg_color = (150, 150, 150)

# # Define button rectangles
# button1_rect = pygame.Rect(0, 0, 280, 60)
# button2_rect = pygame.Rect(0, 0, 280, 60)

# # Initial button positions
# button1_rect.center = (width // 2, height // 2 - 60)
# button2_rect.center = (width // 2, height // 2 + 60)

# showing_popup = False
# showing_fractal_menu = False

# # Create instances of the components
# popup_component = Popup(screen, width, height)
# fractal_menu_component = FractalSelectionMenu(screen, width, height)
# hello_window_component = HelloWindow(screen, width, height)
# homepage_component = Homepage(screen, width, height)
# mandelbrot_viewer = MandelbrotViewer(width, height)  # Added line

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.VIDEORESIZE:
#             width, height = event.w, event.h
#             screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
#             button1_rect.center = (width // 2, height // 2 - 60)
#             button2_rect.center = (width // 2, height // 2 + 60)
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_f:
#                 is_maximized = not is_maximized
#                 if is_maximized:
#                     screen = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.FULLSCREEN)
#                 else:
#                     screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
#                 button1_rect.center = (width // 2, height // 2 - 60)
#                 button2_rect.center = (width // 2, height // 2 + 60)
#             elif event.key == pygame.K_ESCAPE:
#                 if showing_popup:
#                     showing_popup = False
#                 elif showing_fractal_menu:
#                     showing_fractal_menu = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if button1_rect.collidepoint(event.pos):
#                 showing_fractal_menu = True
#             elif button2_rect.collidepoint(event.pos):
#                 showing_popup = True
#             elif showing_popup:
#                 popup_rect = popup_component.show([], width, height)
#                 if not popup_rect.collidepoint(event.pos):
#                     showing_popup = False
#             elif showing_fractal_menu:
#                 menu_rect = fractal_menu_component.show(width, height)
#                 if menu_rect.collidepoint(event.pos):
#                     mandelbrot_viewer.show()  # Call the Mandelbrot viewer
#                     showing_fractal_menu = False
#                 else:
#                     homepage_component.show()
#                     showing_fractal_menu = False

#     if button1_rect.collidepoint(pygame.mouse.get_pos()):
#         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#     elif button2_rect.collidepoint(pygame.mouse.get_pos()):
#         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#     else:
#         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

#     ret, frame = video.read()
#     if ret:
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         video_aspect_ratio = frame.shape[1] / frame.shape[0]
#         screen_aspect_ratio = width / height

#         if video_aspect_ratio > screen_aspect_ratio:
#             scaled_width = int(height * video_aspect_ratio)
#             scaled_height = height
#         else:
#             scaled_width = width
#             scaled_height = int(width / video_aspect_ratio)

#         frame = cv2.resize(frame, (scaled_width, scaled_height))

#         x_offset = (scaled_width - width) // 2
#         y_offset = (scaled_height - height) // 2
#         cropped_frame = frame[y_offset:y_offset + height, x_offset:x_offset + width]

#         frame_surface = pygame.image.frombuffer(cropped_frame.flatten(), (width, height), 'RGB')
#         screen.blit(frame_surface, (0, 0))

#     title_rect = title_image.get_rect(center=(width // 2, title_image.get_height() // 2))
#     screen.blit(title_image, title_rect.topleft)

#     pygame.draw.rect(screen, button_bg_color, button1_rect, border_radius=10)
#     pygame.draw.rect(screen, button_bg_color, button2_rect, border_radius=10)

#     button1_text = button_font.render("Select a fractal", True, button_text_color)
#     button2_text = button_font.render("How to use", True, button_text_color)

#     screen.blit(button1_text, button1_text.get_rect(center=button1_rect.center))
#     screen.blit(button2_text, button2_text.get_rect(center=button2_rect.center))

#     if showing_popup:
#         popup_text = [
#             "Instructions to Use FractalXplore:",
#             "------------------------------------",
#             "1. Click on 'Select a fractal' to choose a fractal.",
#             "2. Explore various fractals using the interactive controls.",
#             "3. Click on 'How to use' to display these instructions.",
#             "4. Enjoy the mathemagical journey through fractals!",
#             "------------------------------------",
#         ]
#         popup_component.show(popup_text, width, height)
#         pygame.display.flip()
#     elif showing_fractal_menu:
#         fractal_menu_component.show(width, height)
#         pygame.display.flip()

#     pygame.display.flip()
#     clock.tick(60)

# video.release()
# pygame.quit()

# gui.py

# import pygame
# import cv2
# from components import Popup, FractalSelectionMenu, HelloWindow, Homepage
# from MandleBrot import MandelbrotViewer
# from julia import JuliaViewer

# class GUI:
#     def __init__(self, width, height):
#         pygame.init()
#         self.width, self.height = width, height
#         self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
#         pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

#         # Load the title image
#         self.title_image = pygame.image.load("title.png").convert_alpha()

#         self.clock = pygame.time.Clock()
#         self.running = True
#         self.is_maximized = False
#         self.selected_fractal = None

#         # OpenCV video capture
#         self.video = cv2.VideoCapture("bgvideo.mp4")

#         self.button_font = pygame.font.Font(None, 36)
#         self.button_text_color = (0, 0, 0)
#         self.button_bg_color = (150, 150, 150)

#         # Define button rectangles
#         self.button1_rect = pygame.Rect(0, 0, 280, 60)
#         self.button2_rect = pygame.Rect(0, 0, 280, 60)

#         # Initial button positions
#         self.button1_rect.center = (width // 2, height // 2 - 60)
#         self.button2_rect.center = (width // 2, height // 2 + 60)

#         self.showing_popup = False
#         self.showing_fractal_menu = False

#         # Create instances of the components
#         self.popup_component = Popup(self.screen, self.width, self.height)
#         self.fractal_menu_component = FractalSelectionMenu(self.screen, self.width, self.height)
#         self.hello_window_component = HelloWindow(self.screen, self.width, self.height)
#         self.homepage_component = Homepage(self.screen, self.width, self.height)
#         self.mandelbrot_viewer = MandelbrotViewer(self.width, self.height)
#         self.julia_viewer = JuliaViewer(self.width, self.height)

#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.VIDEORESIZE:
#                 self.width, self.height = event.w, event.h
#                 self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
#                 self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
#                 self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_f:
#                     self.is_maximized = not self.is_maximized
#                     if self.is_maximized:
#                         self.screen = pygame.display.set_mode(
#                             (self.width, self.height), pygame.RESIZABLE | pygame.FULLSCREEN
#                         )
#                     else:
#                         self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
#                     self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
#                     self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
#                 elif event.key == pygame.K_ESCAPE:
#                     if self.showing_popup:
#                         self.showing_popup = False
#                     elif self.showing_fractal_menu:
#                         self.showing_fractal_menu = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.button1_rect.collidepoint(event.pos):
#                     self.showing_fractal_menu = True
#                 elif self.button2_rect.collidepoint(event.pos):
#                     self.showing_popup = True
#                 elif self.showing_popup:
#                     popup_rect = self.popup_component.show([], self.width, self.height)
#                     if not popup_rect.collidepoint(event.pos):
#                         self.showing_popup = False
#                 elif self.showing_fractal_menu:
#                     menu_rect = self.fractal_menu_component.show(self.width, self.height)
#                     if menu_rect.collidepoint(event.pos):
#                         self.selected_fractal = self.fractal_menu_component.get_selected_fractal()
#                         if self.selected_fractal == "Mandelbrot Set":
#                             self.mandelbrot_viewer.show()
#                         elif self.selected_fractal == "Julia Set":
#                             self.julia_viewer.show()
#                         else:
#                             self.hello_window_component.show()
#                         self.showing_fractal_menu = False
#                     else:
#                         self.homepage_component.show()
#                         self.showing_fractal_menu = False

#     def update(self):
#         self.handle_events()

#         if self.button1_rect.collidepoint(pygame.mouse.get_pos()):
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#         elif self.button2_rect.collidepoint(pygame.mouse.get_pos()):
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#         else:
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

#         ret, frame = self.video.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             video_aspect_ratio = frame.shape[1] / frame.shape[0]
#             screen_aspect_ratio = self.width / self.height

#             if video_aspect_ratio > screen_aspect_ratio:
#                 scaled_width = int(self.height * video_aspect_ratio)
#                 scaled_height = self.height
#             else:
#                 scaled_width = self.width
#                 scaled_height = int(self.width / video_aspect_ratio)

#             frame = cv2.resize(frame, (scaled_width, scaled_height))

#             x_offset = (scaled_width - self.width) // 2
#             y_offset = (scaled_height - self.height) // 2
#             cropped_frame = frame[y_offset : y_offset + self.height, x_offset : x_offset + self.width]

#             frame_surface = pygame.image.frombuffer(cropped_frame.flatten(), (self.width, self.height), "RGB")
#             self.screen.blit(frame_surface, (0, 0))

#         title_rect = self.title_image.get_rect(center=(self.width // 2, self.title_image.get_height() // 2))
#         self.screen.blit(self.title_image, title_rect.topleft)

#         pygame.draw.rect(self.screen, self.button_bg_color, self.button1_rect, border_radius=10)
#         pygame.draw.rect(self.screen, self.button_bg_color, self.button2_rect, border_radius=10)

#         button1_text = self.button_font.render("Select a fractal", True, self.button_text_color)
#         button2_text = self.button_font.render("How to use", True, self.button_text_color)

#         self.screen.blit(button1_text, button1_text.get_rect(center=self.button1_rect.center))
#         self.screen.blit(button2_text, button2_text.get_rect(center=self.button2_rect.center))

#         if self.showing_popup:
#             popup_text = [
#                 "Instructions to Use FractalXplore:",
#                 "------------------------------------",
#                 "1. Click on 'Select a fractal' to choose a fractal.",
#                 "2. Explore various fractals using the interactive controls.",
#                 "3. Click on 'How to use' to display these instructions.",
#                 "4. Enjoy the mathemagical journey through fractals!",
#                 "------------------------------------",
#             ]
#             self.popup_component.show(popup_text, self.width, self.height)
#             pygame.display.flip()
#         elif self.showing_fractal_menu:
#             self.fractal_menu_component.show(self.width, self.height)
#             pygame.display.flip()

#         pygame.display.flip()
#         self.clock.tick(60)

#     def run(self):
#         while self.running:
#             self.update()

#         self.video.release()
#         pygame.quit()
    
# def main():
#     width, height = 1280, 800
#     gui = GUI(width, height)
#     gui.run()

# if __name__ == "__main__":
#     main()


import pygame
from components import Popup, FractalSelectionMenu, HelloWindow, Homepage
from MandleBrot import MandelbrotViewer
from julia import JuliaViewer
import cv2

class GUI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

        # Load the title image
        self.title_image = pygame.image.load("title.png").convert_alpha()

        self.clock = pygame.time.Clock()
        self.running = True
        self.is_maximized = False
        self.selected_fractal = None

        # OpenCV video capture
        self.video = cv2.VideoCapture("bgvideo.mp4")

        self.button_font = pygame.font.Font(None, 36)
        self.button_text_color = (0, 0, 0)
        self.button_bg_color = (150, 150, 150)

        # Define button rectangles
        self.button1_rect = pygame.Rect(0, 0, 280, 60)
        self.button2_rect = pygame.Rect(0, 0, 280, 60)

        # Initial button positions
        self.button1_rect.center = (width // 2, height // 2 - 60)
        self.button2_rect.center = (width // 2, height // 2 + 60)

        self.showing_popup = False
        self.showing_fractal_menu = False

        # Create instances of the components
        self.popup_component = Popup(self.screen, width, height)
        self.fractal_menu_component = FractalSelectionMenu(self.screen, width, height)
        self.hello_window_component = HelloWindow(self.screen, width, height)
        self.homepage_component = Homepage(self.screen, width, height)
        self.mandelbrot_viewer = MandelbrotViewer(width, height)
        self.julia_viewer = JuliaViewer(width, height)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
                self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.is_maximized = not self.is_maximized
                    if self.is_maximized:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE | pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                    self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
                    self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
                elif event.key == pygame.K_ESCAPE:
                    if self.showing_popup:
                        self.showing_popup = False
                    elif self.showing_fractal_menu:
                        self.showing_fractal_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button1_rect.collidepoint(event.pos):
                    self.showing_fractal_menu = True
                elif self.button2_rect.collidepoint(event.pos):
                    self.showing_popup = True
                elif self.showing_popup:
                    popup_rect = self.popup_component.show([], self.width, self.height)
                    if not popup_rect.collidepoint(event.pos):
                        self.showing_popup = False
                elif self.showing_fractal_menu:
                    menu_rect = self.fractal_menu_component.show(self.width, self.height)
                    if menu_rect.collidepoint(event.pos):
                        self.selected_fractal = self.fractal_menu_component.get_selected_fractal()
                        self.show_fractal_viewer()
                        self.showing_fractal_menu = False
                    else:
                        self.homepage_component.show()
                        self.showing_fractal_menu = False
        return self.running

    def show_fractal_viewer(self):
        if self.selected_fractal == "Mandelbrot Set":
            self.mandelbrot_viewer.show()
        elif self.selected_fractal == "Julia Set":
            self.julia_viewer.show()

    def update(self):
        pass

    def render(self):
        # (Rendering logic if needed)
        pass
    def run(self):
        video = cv2.VideoCapture("bgvideo.mp4")

        clock = pygame.time.Clock()

        while self.running:
            self.running = self.handle_events()
            self.update()
            self.render()

            pygame.display.flip()
            clock.tick(60)

            ret, frame = video.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                video_aspect_ratio = frame.shape[1] / frame.shape[0]
                screen_aspect_ratio = self.width / self.height

                if video_aspect_ratio > screen_aspect_ratio:
                    scaled_width = int(self.height * video_aspect_ratio)
                    scaled_height = self.height
                else:
                    scaled_width = self.width
                    scaled_height = int(self.width / video_aspect_ratio)

                frame = cv2.resize(frame, (scaled_width, scaled_height))

                x_offset = (scaled_width - self.width) // 2
                y_offset = (scaled_height - self.height) // 2
                cropped_frame = frame[y_offset:y_offset + self.height, x_offset:x_offset + self.width]

                frame_surface = pygame.image.frombuffer(cropped_frame.flatten(), (self.width, self.height), 'RGB')
                self.screen.blit(frame_surface, (0, 0))

            title_rect = self.title_image.get_rect(center=(self.width // 2, self.title_image.get_height() // 2))
            self.screen.blit(self.title_image, title_rect.topleft)

            pygame.draw.rect(self.screen, self.button_bg_color, self.button1_rect, border_radius=10)
            pygame.draw.rect(self.screen, self.button_bg_color, self.button2_rect, border_radius=10)

            button1_text = self.button_font.render("Select a fractal", True, self.button_text_color)
            button2_text = self.button_font.render("How to use", True, self.button_text_color)

            self.screen.blit(button1_text, button1_text.get_rect(center=self.button1_rect.center))
            self.screen.blit(button2_text, button2_text.get_rect(center=self.button2_rect.center))

            if self.showing_popup:
                popup_text = [
                    "Instructions to Use FractalXplore:",
                    "------------------------------------",
                    "1. Click on 'Select a fractal' to choose a fractal.",
                    "2. Explore various fractals using the interactive controls.",
                    "3. Click on 'How to use' to display these instructions.",
                    "4. Enjoy the mathemagical journey through fractals!",
                    "------------------------------------",
                ]
                self.popup_component.show(popup_text, self.width, self.height)
                pygame.display.flip()
            elif self.showing_fractal_menu:
                self.fractal_menu_component.show(self.width, self.height)
                pygame.display.flip()

        video.release()
        pygame.quit()

if __name__ == "__main__":
    gui = GUI()
    gui.run()

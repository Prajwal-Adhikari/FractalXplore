import pygame
from components import Popup, FractalSelectionMenu, HelloWindow, Homepage
from MandleBrot import MandelbrotViewer
from julia import JuliaViewer
from Barnsley import BarnsleyFernViewer
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
        self.button3_rect = pygame.Rect(0, 0, 280, 60)

        # Initial button positions
        self.button1_rect.center = (width // 2, height // 2 - 60)
        self.button2_rect.center = (width // 2, height // 2 + 60)
        self.button3_rect.center = (width // 2, height // 2 + 180)

        self.showing_popup = False
        self.showing_fractal_menu = False

        # Create instances of the components
        self.popup_component = Popup(self.screen, width, height)
        self.fractal_menu_component = FractalSelectionMenu(self.screen, width, height)
        self.hello_window_component = HelloWindow(self.screen, width, height)
        self.homepage_component = Homepage(self.screen, width, height)
        self.mandelbrot_viewer = MandelbrotViewer(width, height)
        self.julia_viewer = JuliaViewer(width, height)
        self.barnsley_fern_viewer = BarnsleyFernViewer(width,height) 


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.w, event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
                self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
                self.button3_rect.center = (self.width // 2, self.height // 2 + 180)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.is_maximized = not self.is_maximized
                    if self.is_maximized:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE | pygame.FULLSCREEN)
                    else:
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                    self.button1_rect.center = (self.width // 2, self.height // 2 - 60)
                    self.button2_rect.center = (self.width // 2, self.height // 2 + 60)
                    self.button3_rect.center = (self.width // 2, self.height // 2 + 180)

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
                        print(self.selected_fractal)
                        self.show_fractal_viewer()
                        self.showing_fractal_menu = False
                    else:
                        self.homepage_component.show()
                        self.showing_fractal_menu = False

        return self.running

    def show_fractal_viewer(self):
        if self.selected_fractal == "Julia Set":
            self.julia_viewer.show()
        elif self.selected_fractal == "Mandelbrot Set":
            self.mandelbrot_viewer.show()
        elif self.selected_fractal == "Barnsley Fern":
            self.barnsley_fern_viewer.show()

  

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



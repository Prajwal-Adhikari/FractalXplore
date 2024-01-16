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
# mandelbrot_viewer = MandelbrotViewer(screen, width, height)  # Added line

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
#                     # Display the Mandelbrot set
#                     mandelbrot_viewer.show()
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

import pygame
import cv2
from components import Popup, FractalSelectionMenu, HelloWindow, Homepage 
from MandleBrot import MandelbrotViewer

# Pygame setup
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

# Load the title image
title_image = pygame.image.load("title.png").convert_alpha()

clock = pygame.time.Clock()
running = True
is_maximized = False
selected_fractal = None

# OpenCV video capture
video = cv2.VideoCapture("bgvideo.mp4")

button_font = pygame.font.Font(None, 36)
button_text_color = (0, 0, 0)
button_bg_color = (150, 150, 150)

# Define button rectangles
button1_rect = pygame.Rect(0, 0, 280, 60)
button2_rect = pygame.Rect(0, 0, 280, 60)

# Initial button positions
button1_rect.center = (width // 2, height // 2 - 60)
button2_rect.center = (width // 2, height // 2 + 60)

showing_popup = False
showing_fractal_menu = False

# Create instances of the components
popup_component = Popup(screen, width, height)
fractal_menu_component = FractalSelectionMenu(screen, width, height)
hello_window_component = HelloWindow(screen, width, height)
homepage_component = Homepage(screen, width, height)
mandelbrot_viewer = MandelbrotViewer(width, height)  # Added line

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            button1_rect.center = (width // 2, height // 2 - 60)
            button2_rect.center = (width // 2, height // 2 + 60)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                is_maximized = not is_maximized
                if is_maximized:
                    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                button1_rect.center = (width // 2, height // 2 - 60)
                button2_rect.center = (width // 2, height // 2 + 60)
            elif event.key == pygame.K_ESCAPE:
                if showing_popup:
                    showing_popup = False
                elif showing_fractal_menu:
                    showing_fractal_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos):
                showing_fractal_menu = True
            elif button2_rect.collidepoint(event.pos):
                showing_popup = True
            elif showing_popup:
                popup_rect = popup_component.show([], width, height)
                if not popup_rect.collidepoint(event.pos):
                    showing_popup = False
            elif showing_fractal_menu:
                menu_rect = fractal_menu_component.show(width, height)
                if menu_rect.collidepoint(event.pos):
                    mandelbrot_viewer.show()  # Call the Mandelbrot viewer
                    showing_fractal_menu = False
                else:
                    homepage_component.show()
                    showing_fractal_menu = False

    if button1_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif button2_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        video_aspect_ratio = frame.shape[1] / frame.shape[0]
        screen_aspect_ratio = width / height

        if video_aspect_ratio > screen_aspect_ratio:
            scaled_width = int(height * video_aspect_ratio)
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = int(width / video_aspect_ratio)

        frame = cv2.resize(frame, (scaled_width, scaled_height))

        x_offset = (scaled_width - width) // 2
        y_offset = (scaled_height - height) // 2
        cropped_frame = frame[y_offset:y_offset + height, x_offset:x_offset + width]

        frame_surface = pygame.image.frombuffer(cropped_frame.flatten(), (width, height), 'RGB')
        screen.blit(frame_surface, (0, 0))

    title_rect = title_image.get_rect(center=(width // 2, title_image.get_height() // 2))
    screen.blit(title_image, title_rect.topleft)

    pygame.draw.rect(screen, button_bg_color, button1_rect, border_radius=10)
    pygame.draw.rect(screen, button_bg_color, button2_rect, border_radius=10)

    button1_text = button_font.render("Select a fractal", True, button_text_color)
    button2_text = button_font.render("How to use", True, button_text_color)

    screen.blit(button1_text, button1_text.get_rect(center=button1_rect.center))
    screen.blit(button2_text, button2_text.get_rect(center=button2_rect.center))

    if showing_popup:
        popup_text = [
            "Instructions to Use FractalXplore:",
            "------------------------------------",
            "1. Click on 'Select a fractal' to choose a fractal.",
            "2. Explore various fractals using the interactive controls.",
            "3. Click on 'How to use' to display these instructions.",
            "4. Enjoy the mathemagical journey through fractals!",
            "------------------------------------",
        ]
        popup_component.show(popup_text, width, height)
        pygame.display.flip()
    elif showing_fractal_menu:
        fractal_menu_component.show(width, height)
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)

video.release()
pygame.quit()

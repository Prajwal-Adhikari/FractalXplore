import pygame
import cv2
import numpy as np

def show_popup(screen, popup_text, width, height):
    # Render a simple popup window with instructions
    popup_rect = pygame.Rect(width // 4, height // 4, width // 2, height // 2)  # Centered popup
    popup_bg_color = (220, 220, 220)  # Background color for the popup window
    border_radius = 10  # Radius for the rounded corners

    pygame.draw.rect(screen, popup_bg_color, popup_rect, border_radius=border_radius)
    
    # Text rendering for instructions
    instruction_font = pygame.font.Font(None, 30)
    
    y_offset = popup_rect.top + 30  # Starting Y position for the text
    for line in popup_text:
        text_render = instruction_font.render(line, True, (0, 0, 0))
        text_rect = text_render.get_rect(topleft=(popup_rect.left + 30, y_offset))  # Left-align the text
        screen.blit(text_render, text_rect)
        y_offset += 30  # Increase Y position for the next line

    return popup_rect  # Return the popup rectangle

def show_fractal_selection_menu(screen, width, height):
    # Render a menu to select a fractal
    menu_rect = pygame.Rect(width // 4, height // 4, width // 2, height // 2)  # Centered menu
    menu_bg_color = (220, 220, 220)  # Background color for the menu window
    border_radius = 10  # Radius for the rounded corners

    pygame.draw.rect(screen, menu_bg_color, menu_rect, border_radius=border_radius)
    
    # Text rendering for menu options
    menu_font = pygame.font.Font(None, 30)
    
    options = [
        "Select a Fractal:",
        "1. Mandelbrot Set",
        "2. Julia Set",
        "3. Dragon Set",
    ]

    y_offset = menu_rect.top + 30  # Starting Y position for the text
    for line in options:
        text_render = menu_font.render(line, True, (0, 0, 0))
        text_rect = text_render.get_rect(topleft=(menu_rect.left + 30, y_offset))  # Left-align the text
        screen.blit(text_render, text_rect)
        y_offset += 30  # Increase Y position for the next line

    return menu_rect

def show_hello_window(screen, width, height):
    # Render a new window with a simple "Hello" message
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Text rendering for "Hello"
    hello_font = pygame.font.Font(None, 36)
    hello_text = hello_font.render("Hello!", True, (0, 0, 0))  # Black text color
    hello_text_rect = hello_text.get_rect(center=(width // 2, height // 2))

    screen.blit(hello_text, hello_text_rect)

    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds) to display the "Hello" message
    screen.fill((0, 0, 0))  # Fill the screen with black color

    return hello_text_rect

def show_homepage(screen, width, height):
    # Render content for the homepage
    homepage_rect = pygame.Rect(0, 0, width, height)
    homepage_bg_color = (0, 0, 0)  # Black background color

    pygame.draw.rect(screen, homepage_bg_color, homepage_rect)

    # You can add additional content for the homepage here

    return homepage_rect

# Pygame setup
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

# Load the title image
title_image = pygame.image.load("title.png").convert_alpha()

clock = pygame.time.Clock()
running = True
is_maximized = False  # To keep track of the window's maximization state
selected_fractal = None  # Variable to keep track of the selected fractal

# OpenCV video capture
video = cv2.VideoCapture("bgvideo.mp4")

button_font = pygame.font.Font(None, 36)
button_text_color = (0, 0, 0)  # Black color for the button text
button_bg_color = (150, 150, 150)  # Grey color for the button background

# Define button rectangles
button1_rect = pygame.Rect(0, 0, 280, 60)
button2_rect = pygame.Rect(0, 0, 280, 60)

# Initial button positions
button1_rect.center = (width // 2, height // 2 - 60)
button2_rect.center = (width // 2, height // 2 + 60)

showing_popup = False  # Flag to track whether the pop-up is currently being displayed
showing_fractal_menu = False  # Flag to track whether the fractal selection menu is currently being displayed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            # Recalculate button and popup positions when the window is resized
            button1_rect.center = (width // 2, height // 2 - 60)
            button2_rect.center = (width // 2, height // 2 + 60)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                is_maximized = not is_maximized
                if is_maximized:
                    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE | pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                # Recalculate button and popup positions when the window is maximized or restored
                button1_rect.center = (width // 2, height // 2 - 60)
                button2_rect.center = (width // 2, height // 2 + 60)
            elif event.key == pygame.K_ESCAPE:
                if showing_popup:
                    showing_popup = False
                elif showing_fractal_menu:
                    showing_fractal_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos):
                # Display fractal selection menu
                showing_fractal_menu = True
            elif button2_rect.collidepoint(event.pos):
                # Display popup
                showing_popup = True
            elif showing_popup:
                # Check if the mouse click is outside the popup area
                popup_rect = show_popup(screen, [], width, height)
                if not popup_rect.collidepoint(event.pos):
                    showing_popup = False
            elif showing_fractal_menu:
                # Check which fractal option is selected
                menu_rect = show_fractal_selection_menu(screen, width, height)
                if menu_rect.collidepoint(event.pos):
                    # If menu item 1 (Mandelbrot Set) is selected, show "Hello" window
                    show_hello_window(screen, width, height)
                    showing_fractal_menu = False
                else:
                    # If any other part of the menu is clicked, go back to the homepage
                    show_homepage(screen, width, height)
                    showing_fractal_menu = False

    # Handle mouse cursor
    if button1_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif button2_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Render video frame
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize and crop the video frame to fit the screen
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

    # Render title image
    title_rect = title_image.get_rect(center=(width // 2, title_image.get_height() // 2))
    screen.blit(title_image, title_rect.topleft)

    # Draw buttons
    pygame.draw.rect(screen, button_bg_color, button1_rect, border_radius=10)
    pygame.draw.rect(screen, button_bg_color, button2_rect, border_radius=10)

    button1_text = button_font.render("Select a fractal", True, button_text_color)
    button2_text = button_font.render("How to use", True, button_text_color)

    screen.blit(button1_text, button1_text.get_rect(center=button1_rect.center))
    screen.blit(button2_text, button2_text.get_rect(center=button2_rect.center))

    # Render pop-up or fractal menu if showing
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
        show_popup(screen, popup_text, width, height)
        pygame.display.flip()
    elif showing_fractal_menu:
        show_fractal_selection_menu(screen, width, height)
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)

# Release the video capture
video.release()
pygame.quit()

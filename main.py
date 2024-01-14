import pygame
from gui import GUI

def main():
    pygame.init()
    width, height = 1280, 800
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("FractalXplore - A Mathemagical Odyssey Through Fractals")

    gui = GUI(screen, width, height)

    clock = pygame.time.Clock()
    running = True

    while running:
        running = gui.handle_events()
        gui.update()
        gui.render()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()



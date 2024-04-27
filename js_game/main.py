import sys

import pygame
from tmp.button import Button, Text


def main():
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption("Basic Pygame program")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    b = Button(
        (0, 0),
        (100, 50),
        Text(
            text="ymp",
            font=pygame.font.SysFont("Corbel", 35),
            color=(0, 0, 0),
        ),
        (0, 0, 0),
        (255, 255, 255),
        background,
    )
    pygame.display.flip()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        b.update(screen, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()

import pygame
import sys


def show_taskbar(screen):
    # Colors
    taskbar_color = (50, 50, 50)
    icon_color = (200, 200, 200)

    # Screen resolution
    width = screen.get_width()
    height = screen.get_height()

    # Taskbar dimensions
    taskbar_height = 40

    # Icon dimensions and position
    icon_size = 30
    icon_x = 10
    icon_y = (taskbar_height - icon_size) // 2

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, taskbar_color, [0, height - taskbar_height, width, taskbar_height])

        pygame.draw.circle(screen, icon_color, (icon_x + icon_size // 2, height - taskbar_height + icon_y + icon_size // 2), icon_size // 2)
        pygame.draw.circle(screen, icon_color, (icon_x + 70, height - taskbar_height + icon_y + icon_size // 2), icon_size // 2)
        pygame.draw.rect(screen, icon_color, [icon_x + 100, height - taskbar_height + icon_y, icon_size, icon_size])

        pygame.display.update()
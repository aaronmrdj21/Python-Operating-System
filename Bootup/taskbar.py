import pygame
import sys
import datetime

def show_taskbar(screen):
    # Colors
    taskbar_color = (50, 50, 50)
    icon_color = (200, 200, 200)

    # Screen resolution
    width = screen.get_width()
    height = screen.get_height()

    # Taskbar dimensions
    taskbar_height = 40
    
    today = datetime.datetime.now()
    today = today.strftime("%B %d, %Y")

    color = (255, 255, 255)
    smallfont = pygame.font.SysFont('Corbel', 15)
    date = smallfont.render(today, True, color)

    # Icon dimensions and position
    icon_size = 30

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, taskbar_color, [0, height - taskbar_height, width, taskbar_height])

        pygame.draw.circle(screen, icon_color, (20, 480), icon_size // 2)
        pygame.draw.circle(screen, (255,255,0), (60, 480), icon_size // 2)
        pygame.draw.rect(screen, icon_color, (80, 465, icon_size, icon_size))
        pygame.draw.circle(screen, (255,0,0), (130, 480), icon_size // 2)
        pygame.draw.circle(screen, (0,255,0), (170, 480), icon_size // 2)
        screen.blit(date, (380, 470))
        # screen.blit(Date, (130, 24 - 40 + 45))
        pygame.display.update()
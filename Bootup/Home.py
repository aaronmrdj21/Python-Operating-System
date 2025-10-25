import pygame
import Login
import taskbar

pygame.init()

# Game Window
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Operating System Simulator")
run = True
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (win_width, win_height))

Login.show_login_screen(win)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                # Exits fullscreen mode and closes the window
                run = False
    background = pygame.transform.scale(background, (win_width, win_height))
    win.blit(background, (0, 0))
    taskbar.show_taskbar(win)
    pygame.display.update()

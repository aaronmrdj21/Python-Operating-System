import pygame
import Login
import taskbar

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Aaron's Operating System Simulator")
run = True
backgroundImage = pygame.image.load("background.jpg")

Login.show_login_screen(win)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    backgroundImage = pygame.transform.scale(backgroundImage, (win_width, win_height))
    win.blit(backgroundImage, (0, 0))
    taskbar.show_taskbar(win)
    
    pygame.display.update()

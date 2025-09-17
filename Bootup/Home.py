import pygame
import Login

pygame.init()

# Game Window
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height), pygame.FULLSCREEN)
pygame.display.set_caption("Operating System Simulator")
run = True

Login.show_login_screen(win)
exit_button_rect = pygame.Rect(700, 0, 30, 20)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button_rect.collidepoint(event.pos):
                # Exits fullscreen mode and closes the window
                run = False
        
    win.fill((0, 0,255))
    pygame.draw.rect(win, (255, 0, 0), exit_button_rect)
    pygame.display.update()
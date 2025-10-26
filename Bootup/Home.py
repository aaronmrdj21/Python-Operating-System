import pygame
import Login
import taskbar
import subprocess
import sys
import os

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Aaron's Operating System Simulator")
run = True
backgroundImage = pygame.image.load("background.jpg")

def open_internet_explorer():
    # Get the path to the internet explorer script
    ie_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Apps', 'internet.py')
    # Launch the internet explorer in a new window
    subprocess.Popen([sys.executable, ie_path])

def open_App2():
    print("Opening App2...")

Login.show_login_screen(win)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
    backgroundImage = pygame.transform.scale(backgroundImage, (win_width, win_height))
    win.blit(backgroundImage, (0, 0))


    taskbar.show_taskbar(win, callbacks={
        'icon1': open_internet_explorer,
        'icon2': open_App2,
        'icon3': lambda: print("Icon3 clicked"),
        'icon4': lambda: print("Icon4 clicked"),
        'icon5': lambda: print("Icon5 clicked")
    })    
    pygame.display.update()

import pygame
import sys
import subprocess
import sys
import os

pygame.init()

# Window setup
ie_width = 500
ie_height = 500
ie_window = pygame.display.set_mode((ie_width, ie_height))
pygame.display.set_caption("Aaron's Internet Explorer")

def open_internet_explorer():
    # Get the path to the internet explorer script
    ie_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Apps', 'internet.py')
    # Launch the internet explorer in a new window
    subprocess.Popen([sys.executable, ie_path])

def open_App2():
    print("Opening App2...")

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Bootup import taskbar


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    ie_window.fill((255, 255, 255))  # White background
    
    taskbar.show_taskbar(ie_window, callbacks={'icon1': open_internet_explorer,
        'icon2': open_App2,
        'icon3': lambda: print("Icon3 clicked"),
        'icon4': lambda: print("Icon4 clicked"),
        'icon5': lambda: print("Icon5 clicked")})   
    pygame.display.update()
    pygame.display.update()

pygame.quit()
sys.exit()
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

# Initialize fonts
font = pygame.font.SysFont('arial', 42, bold=True)  # Modern search engine style
search_font = pygame.font.SysFont('arial', 32)  # Slightly smaller font for input

# Render title text with a modern blue color
text = font.render("A-SEARCH", True, (66, 133, 244))  # Google blue color

# Search box setup
search_box = pygame.Rect(100, 200, 300, 40)  # x, y, width, height
search_text = ''
search_active = False
search_box_color = pygame.Color('lightgray')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if search_active:
                if event.key == pygame.K_RETURN:
                    print(f"Searching for: {search_text}")
                    # Here you could add search functionality
                elif event.key == pygame.K_BACKSPACE:
                    search_text = search_text[:-1]
                else:
                    search_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if search box is clicked
            if search_box.collidepoint(event.pos):
                search_active = True
            else:
                search_active = False

    ie_window.fill((255, 255, 255))  # White background
    
    # Draw title
    ie_window.blit(text, (220, 150))  # Position of "A-SEARCH"
    
    # Draw search box
    search_box_color = pygame.Color('white') if search_active else pygame.Color('lightgray')
    pygame.draw.rect(ie_window, search_box_color, search_box)
    pygame.draw.rect(ie_window, (100, 100, 100), search_box, 2)  # Border
    
    # Draw search text
    search_surface = search_font.render(search_text, True, (0, 0, 0))
    # Add padding inside the search box
    ie_window.blit(search_surface, (search_box.x + 10, search_box.y + 10))

    taskbar.show_taskbar(ie_window, callbacks={'icon1': open_internet_explorer,
        'icon2': open_App2,
        'icon3': lambda: print("Icon3 clicked"),
        'icon4': lambda: print("Icon4 clicked"),
        'icon5': lambda: print("Icon5 clicked")})   
    pygame.display.update()

pygame.quit()
sys.exit()
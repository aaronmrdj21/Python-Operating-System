import pygame
import sys
import subprocess
import sys
import os

pygame.init()
pygame.scrap.init()  # Initialize clipboard functionality

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
font = pygame.font.SysFont('arial', 42, bold=True, italic=True)
search_font = pygame.font.SysFont('arial', 32)  # Slightly smaller font for input

# Render title text with a modern blue color
text = font.render("A-SEARCH", True, (66, 133, 244))  # Google blue color

# Search box setup
search_box = pygame.Rect(100, 200, 300, 40)  # x, y, width, height
search_text = ''
search_active = False
search_box_color = pygame.Color('lightgray')
cursor_visible = True
cursor_timer = 0
CURSOR_BLINK_TIME = 500  # Milliseconds
clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and search_active:
            if event.key == pygame.K_ESCAPE:
                search_active = False  # Deactivate search box on escape
            elif event.key == pygame.K_RETURN:
                print(f"Searching for: {search_text}")
                # Here you could add search functionality
            elif event.key == pygame.K_BACKSPACE:
                search_text = search_text[:-1]
                cursor_visible = True
                cursor_timer = 0
            elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                # Handle paste
                try:
                    search_text += pygame.scrap.get(pygame.SCRAP_TEXT).decode('utf-8')
                except:
                    pass
            else:
                if event.unicode and event.unicode.isprintable():
                    search_text += event.unicode
                    cursor_visible = True
                    cursor_timer = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if search box is clicked
            if search_box.collidepoint(event.pos):
                search_active = True
                cursor_visible = True  # Reset cursor blink
                cursor_timer = 0
            else:
                search_active = False

    # Update cursor blink timer
    cursor_timer += clock.tick(60)  # 60 FPS
    if cursor_timer >= CURSOR_BLINK_TIME:
        cursor_timer = 0
        cursor_visible = not cursor_visible

    # Drawing
    ie_window.fill((255, 255, 255))  # White background
    
    # Draw title
    ie_window.blit(text, (220, 150))  # Position of "A-SEARCH"
    
    # Draw search box with hover effect
    search_box_color = pygame.Color('white') if search_active else pygame.Color('lightgray')
    pygame.draw.rect(ie_window, search_box_color, search_box)
    border_color = (66, 133, 244) if search_active else (100, 100, 100)  # Blue when active
    pygame.draw.rect(ie_window, border_color, search_box, 2)  # Border
    
    # Draw search text and cursor
    if len(search_text) == 0 and not search_active:
        # Draw placeholder text
        placeholder = search_font.render("Search the web...", True, (160, 160, 160))
        ie_window.blit(placeholder, (search_box.x + 10, search_box.y + 10))
    else:
        # Draw actual text
        search_surface = search_font.render(search_text, True, (0, 0, 0))
        ie_window.blit(search_surface, (search_box.x + 10, search_box.y + 10))
        
        # Draw blinking cursor when active
        if search_active and cursor_visible:
            cursor_x = search_box.x + 10 + search_surface.get_width()
            cursor_y = search_box.y + 8
            pygame.draw.line(ie_window, (0, 0, 0), 
                           (cursor_x, cursor_y),
                           (cursor_x, cursor_y + 24), 2)

    taskbar.show_taskbar(ie_window, callbacks={'icon1': open_internet_explorer,
        'icon2': open_App2,
        'icon3': lambda: print("Icon3 clicked"),
        'icon4': lambda: print("Icon4 clicked"),
        'icon5': lambda: print("Icon5 clicked")})   
    pygame.display.update()

pygame.quit()
sys.exit()
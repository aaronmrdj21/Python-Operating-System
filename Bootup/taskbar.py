import pygame
import sys
import datetime
import math

def show_topbar(screen=None, height=24, color=(50, 50, 50), icon_color=(200, 200, 200)):
    """Draw a thin top bar at the top of the given surface.

    - screen: pygame Surface (defaults to pygame.display.get_surface())
    - height: bar height in pixels (default 24)
    - color: background color of the top bar
    - icon_color: color used for simple icons

    This function is non-blocking and only draws the bar. Keep it lightweight so
    callers can use it inside their main loop (Home.py already calls it).
    """
    if screen is None:
        screen = pygame.display.get_surface()
        if screen is None:
            return  # nothing to draw

    width = screen.get_width()
    # Draw bar background
    pygame.draw.rect(screen, color, (0, 0, width, height))

    # Small left-side icons (visual only)
    padding = 8
    icon_size = height - padding * 2
    icon_y = height // 2
    x = padding + icon_size // 2
    # draw three small circular icons (like window controls / quick actions)
    pygame.draw.circle(screen, icon_color, (x, icon_y), icon_size // 2)
    x += icon_size + padding
    pygame.draw.circle(screen, (255, 100, 100), (x, icon_y), icon_size // 2)
    x += icon_size + padding
    pygame.draw.circle(screen, (100, 255, 100), (x, icon_y), icon_size // 2)

    # Right side: show time or title
    smallfont = pygame.font.SysFont('Corbel', max(12, height - 6))
    # include seconds so the topbar shows realtime updates
    now = datetime.datetime.now().strftime("%H:%M:%S")
    time_surf = smallfont.render(now, True, (220, 220, 220))
    screen.blit(time_surf, (width - time_surf.get_width() - padding, (height - time_surf.get_height()) // 2))


def show_taskbar(screen, callbacks=None):
    # Colors
    taskbar_color = (50, 50, 50)
    icon_color = (200, 200, 200)
    
    callbacks = callbacks or {}

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
    icon_radius = icon_size // 2
    icon1_pos = (20, height - taskbar_height // 2)   # (20, 480) for 500px height
    icon2_pos = (60, height - taskbar_height // 2)
    icon3_rect = pygame.Rect(80, height - taskbar_height - 15, icon_size, icon_size)
    icon4_pos = (130, height - taskbar_height // 2)
    icon5_pos = (170, height - taskbar_height // 2)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                mx, my = ev.pos

                # Icon1 (circle)
                if math.hypot(mx - icon1_pos[0], my - icon1_pos[1]) <= icon_radius:
                    cb = callbacks.get('icon1')
                    if cb: cb()
                    else: print("Icon1 clicked")
                    continue
                
                # Icon2
                if math.hypot(mx - icon2_pos[0], my - icon2_pos[1]) <= icon_radius:
                    cb = callbacks.get('icon2')
                    if cb: cb()
                    else: print("Icon2 clicked")
                    continue

                # Icon3 (rect)
                if icon3_rect.collidepoint((mx, my)):
                    cb = callbacks.get('icon3')
                    if cb: cb()
                    else: print("Icon3 clicked")
                    continue

                # Icon4
                if math.hypot(mx - icon4_pos[0], my - icon4_pos[1]) <= icon_radius:
                    cb = callbacks.get('icon4')
                    if cb: cb()
                    else: print("Icon4 clicked")
                    continue

                # Icon5
                if math.hypot(mx - icon5_pos[0], my - icon5_pos[1]) <= icon_radius:
                    cb = callbacks.get('icon5')
                    if cb: cb()
                    else: print("Icon5 clicked")
                    continue
        #The Taskbar
        # Draw topbar as well so its clock updates while this function runs its own loop
        try:
            show_topbar(screen)
        except Exception:
            pass
        pygame.draw.rect(screen, taskbar_color, [0, height - taskbar_height, width, taskbar_height])
        # The Icons
        Icon1 = pygame.draw.circle(screen, icon_color, (20, 480), icon_size // 2)
        Icon2 = pygame.draw.circle(screen, (255,255,0), (60, 480), icon_size // 2)
        Icon3 = pygame.draw.rect(screen, icon_color, (80, 465, icon_size, icon_size))
        Icon4 = pygame.draw.circle(screen, (255,0,0), (130, 480), icon_size // 2)
        Icon5 =  pygame.draw.circle(screen, (0,255,0), (170, 480), icon_size // 2)
        screen.blit(date, (380, 470))
        
        pygame.display.update()
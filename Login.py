
import pygame
import sys

def show_login_screen(screen):
    # Colors
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    
    # Screen resolution
    width = screen.get_width()
    height = screen.get_height()
    
    # Title Text
    font = pygame.font.Font(None, 36)
    welcome_text = font.render("Enter your password!", True, (255, 255, 255))
    welcome_text_rect = welcome_text.get_rect(center=(width / 2, height / 4)) 

    # Font and text for button
    smallfont = pygame.font.SysFont('Corbel', 35)
    play_text = smallfont.render('Enter', True, color)
    
    # Enter Button dimensions and position
    enter_button_width = 140
    enter_button_height = 40
    enter_button_x = width / 2 - enter_button_width / 2 
    enter_button_y = welcome_text_rect.bottom + 60 + 60

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if a mouse button is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse is within button coordinates
                mouse = pygame.mouse.get_pos()
                
                if enter_button_x <= mouse[0] <= enter_button_x + enter_button_width and enter_button_y <= mouse[1] <= enter_button_y + enter_button_height:
                    print("Booting up...")
                    return  # Exit the menu and return control to main_game.py

        # Draw button
        mouse = pygame.mouse.get_pos()
        if enter_button_x <= mouse[0] <= enter_button_x + enter_button_width and enter_button_y <= mouse[1] <= enter_button_y + enter_button_height:
            pygame.draw.rect(screen, color_light, [enter_button_x, enter_button_y, enter_button_width, enter_button_height])
        else:
            pygame.draw.rect(screen, color_dark, [enter_button_x, enter_button_y, enter_button_width, enter_button_height])

        # Draw text on button
        screen.blit(play_text, (enter_button_x + 30, enter_button_y + 5))
        
        # Draw welcome text at the top-center
        screen.blit(welcome_text, welcome_text_rect)

        # Update the display
        pygame.display.update()





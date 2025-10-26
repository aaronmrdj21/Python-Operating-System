
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
    
    # Load bootup sound
    sound = pygame.mixer.Sound('bootup_sound.wav')
    
    # textbox
    input_text = ""
    input_active = False
    input_box = pygame.Rect(width/2 - 100, welcome_text_rect.bottom + 30, 200, 32)
    input_box_color = pygame.Color('lightskyblue3')
    txt_font = pygame.font.Font(None, 32)
    
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

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Check if input_box is clicked
                if input_box.collidepoint(ev.pos):
                    input_active = True
                else:
                    input_active = False
                input_box_color = pygame.Color('lightskyblue3') if input_active else pygame.Color('gray')
                

                # Check if Enter button is clicked
                mouse = pygame.mouse.get_pos()
                if enter_button_x <= mouse[0] <= enter_button_x + enter_button_width and enter_button_y <= mouse[1] <= enter_button_y + enter_button_height:
                    print(f"Password entered: {input_text}")
                    return input_text  # Return the password and exit

            if ev.type == pygame.KEYDOWN:
                if input_active:
                    if ev.key == pygame.K_RETURN:
                        print(f"Password entered: {input_text}")
                    
                        sound.play()
                        sound.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
                        return input_text  # Return the password and exit
                    elif ev.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += ev.unicode

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
        
        # Draw input box
        pygame.draw.rect(screen, input_box_color, input_box, 2)
        txt_surface = txt_font.render(input_text, True, color)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Update the display
        pygame.display.update()






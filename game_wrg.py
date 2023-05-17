'''
# ################################################################################################################

# ========================================
# WALL RABBIT GUN game
# ========================================

# Author: @andreicarpena


# Game play:
# [+]   Balancing and Rules similar to Rock Paper Scissors


# Change log:
# @andreicarpena    :   20230513    :   v1, creation
                    :   20230516    :   Change rabbit face
 
# ################################################################################################################
'''



import pygame
import random

pygame.init()
clock = pygame.time.Clock()

# initialize scores
global playerscore, computerscore
playerscore = 0
computerscore = 0


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Wall Rabbit Gun")

background_image = pygame.image.load('graphics/black.png').convert()
font = pygame.font.Font('font/Arial.ttf', 33)
play_message = font.render("[Wall Rabbit Gun]", True, (255, 235, 193))
play_message2 = font.render("Click any object below to start", True, (255, 235, 193))
play_message3 = font.render("By Andrei", True, (255, 235, 193))

score_font = pygame.font.Font('font/Arial.ttf', 25)


button_wall = pygame.image.load('graphics/button_wall.png')
button_rabbit = pygame.image.load('graphics/button_rabbit.png')
button_gun = pygame.image.load('graphics/button_gun.png')


wall_rect = button_wall.get_rect(topleft=(25, 330))
rabbit_rect = button_wall.get_rect(topleft=(225, 330))
gun_rect = button_wall.get_rect(topleft=(425, 330))

wall = pygame.image.load('graphics/wall.png')
rabbit = pygame.image.load('graphics/rabbit.png')
gun = pygame.image.load('graphics/gun.png')
weapon_choices = [wall, rabbit, gun]

is_start = False
user_weapon = None
comp_weapon = None
is_user_weapon = False

is_show_weapon = False

def choose_object(player_object_index):
    global is_start, user_weapon, comp_weapon, is_user_weapon, is_show_weapon
    global playerscore, computerscore, comp_score_message, user_score_message, game_message
    playerscore = 0
    computerscore = 0
    is_start = True
    user_weapon = weapon_choices[player_object_index]
    is_user_weapon = True
    is_show_weapon = False
    comp_weapon_index = random.randint(0, 2)
    comp_weapon = weapon_choices[comp_weapon_index]

    game_message = ""

    # Check who wins
    # NOTE: [wall, rabbit, gun]

    if player_object_index == comp_weapon_index:
        playerscore += 0
        computerscore += 0
    elif player_object_index == 0:
        if comp_weapon_index == 2:
            print("Wall not affected by gun! You win!")
            game_message = "Wall not affected by gun!"
            playerscore += 1
            play_message = font.render("Wall not affected by gun!", True, (255, 235, 193))
            screen.blit(play_message, (100, 170))

            user_score_message = score_font.render("Your Score " + str(playerscore), True, (255, 235, 193))
            screen.blit(user_score_message, (1, 10))
            
        else:
            print("Rabbit can jump over wall! You lose.")
            game_message = "Rabbit can jump over wall! You lose."
            computerscore += 1
            comp_score_message = score_font.render("Comp Score " + str(computerscore), True, (255, 235, 193))
            screen.blit(comp_score_message, (420, 20))
    elif player_object_index == 1 :
        if comp_weapon_index == 0:
            print("Rabbit can jump over wall! You win!")
            game_message = "Rabbit can jump over wall! You win!"
            playerscore +=1
            user_score_message = score_font.render("Your Score " + str(playerscore), True, (255, 235, 193))
            screen.blit(user_score_message, (50, 20))
        else:
            print("Gun can hurt rabbit! You lose.")
            game_message = "Gun can hurt rabbit! You lose."
            computerscore +=1 
            comp_score_message = score_font.render("Comp Score " + str(computerscore), True, (255, 235, 193))
            screen.blit(comp_score_message, (420, 20))
    elif player_object_index == 2 : #gun
        if comp_weapon_index == 1:
            print("Gun can hurt rabbit! You win!")
            game_message = "Gun can hurt rabbit! You win!"
            playerscore += 1
            user_score_message = score_font.render("Your Score " + str(playerscore), True, (255, 235, 193))
            screen.blit(user_score_message, (50, 20))
        else:
            print("Wall not affected by gun! You lose.")
            game_message = "Wall not affected by gun! You lose."
            computerscore += 1
            comp_score_message = score_font.render("Comp Score " + str(computerscore), True, (255, 235, 193))
            screen.blit(comp_score_message, (420, 220))

    pygame.display.update()
    return game_message

 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if wall_rect.collidepoint(event.pos):
                _msg = choose_object(0)
                print("wall")

            elif rabbit_rect.collidepoint(event.pos):
                _msg = choose_object(1)
                print('rabbit')

            elif gun_rect.collidepoint(event.pos):
                _msg = choose_object(2)
                print("gun")
        else:
            _msg = ""

    screen.blit(background_image, (0, 0))
    #screen.blit(user_score_message, (50, 20))
    #screen.blit(comp_score_message, (420, 20))

    
    #screen.blit(comp_score_message, (420, 20))

    if is_start is False:
        screen.blit(play_message, (20, 110))
        screen.blit(play_message2, (50, 200))
        screen.blit(play_message3, (50, 240))
        gm = score_font.render(_msg, True, (255, 235, 193))
        screen.blit(gm, (50, 20))


    if is_show_weapon:
        screen.blit(user_weapon, (60, 70))
        screen.blit(comp_weapon, (350, 70))
        gm = score_font.render(_msg, True, (255, 235, 193))
        screen.blit(gm, (50, 20))

    if is_user_weapon:
        is_show_weapon = True
        gm = score_font.render(_msg, True, (255, 235, 193))
        screen.blit(gm, (50, 20))

    screen.blit(button_wall, wall_rect)
    screen.blit(button_rabbit, rabbit_rect)
    screen.blit(button_gun, gun_rect)

    pygame.display.update()
    clock.tick(10)

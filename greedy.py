import random
import score_calc
import button
import time

import pygame
# import random
# import time

# initialize pygame
pygame.init()

with open("greedyscores.txt", "r") as game_info_saved:
    game_info = game_info_saved.readlines()

# constants
greedy_options = [250, 350, 450, 550]
usable_fives = 0
too_much = 0
kept = False
score = 0
number_of_dice = 6
color = game_info[4].strip("\n")
waiting = 0
game_width = 1000
game_height = 1000
game_color = (95, 147, 65)
fps = 60
image_color = (255, 255, 255)
angle1 = random.randint(0, 360)
angle2 = random.randint(0, 360)
angle3 = random.randint(0, 360)
angle4 = random.randint(0, 360)
angle5 = random.randint(0, 360)
angle6 = random.randint(0, 360)
angle_speed = 0
dice_1_x = 250
dice_1_y = 250
dice_2_x = 500
dice_2_y = 250
dice_3_x = 750
dice_3_y = 250
dice_4_x = 250
dice_4_y = 500
dice_5_x = 500
dice_5_y = 500
dice_6_x = 750
dice_6_y = 500
rolled = False
saved_dice = []
switch_dice_counter = 0

# max name is 16 characters

player_name = game_info[5].strip("\n")
player_score = int(game_info[0].strip("\n"))
comp1_name = game_info[6].strip("\n")
comp1_score = int(game_info[1].strip("\n"))
comp2_name = game_info[7].strip("\n")
comp2_score = int(game_info[2].strip("\n"))
comp3_name = game_info[8].strip("\n")
comp3_score = int(game_info[3].strip("\n"))
comp1_greedy = int(game_info[9].strip("\n"))
comp2_greedy = int(game_info[10].strip("\n"))
comp3_greedy = int(game_info[11].strip("\n"))
winner = ""
turn_name = [player_name, comp1_name, comp2_name, comp3_name]
turn_score = [player_score, comp1_score, comp2_score, comp3_score]
turn = int(game_info[12].strip("\n"))

brand_new_game = False

if player_score == 10000:
    winner = player_name
elif comp1_score == 10000:
    winner = comp1_name
elif comp2_score == 10000:
    winner = comp2_name
elif comp3_score == 10000:
    winner = comp3_name

player = f"{player_name} {player_score}"
comp1 = f"{comp1_name} {comp1_score}"
comp2 = f"{comp2_name} {comp2_score}"
comp3 = f"{comp3_name} {comp3_score}"

opening_text = turn_name[turn] + " rolling."

turn_text = pygame.font.SysFont("inkfree", 30, bold=True)
turn_text_text = turn_text.render(opening_text, True, (0, 0, 0))
turn_text_x = 10
turn_text_y = 10
turn_text_rect = turn_text_text.get_rect()
turn_text_rect.topleft = (turn_text_x, turn_text_y)

short_keys = "Once you get 1000 points you are on the board. Then your goal is to reach 10000 points. Press r to roll."
short_keys += "s to save your current game settings."

short_keys2 = "m for the main menu. From there you can see in depth game info in instructions. Choose your dice color."
short_keys2 += "Or select new names for the game."

short_key = pygame.font.SysFont("arial", 18, bold=True)
short_key_text = short_key.render(short_keys, True, (255, 255, 255))
short_key_text_x = 15
short_key_text_y = 980
short_key_text_rect = turn_text_text.get_rect()
short_key_text_rect.bottomleft = (short_key_text_x, short_key_text_y)

short_key2 = pygame.font.SysFont("arial", 18, bold=True)
short_key2_text = short_key.render(short_keys2, True, (255, 255, 255))
short_key2_text_x = 15
short_key2_text_y = 1000
short_key_text2_rect = turn_text_text.get_rect()
short_key_text2_rect.bottomleft = (short_key2_text_x, short_key2_text_y)

font = pygame.font.SysFont("arial", 18, bold=True)
text = font.render(player, True, (0, 0, 0))
font_x = 0
font_y = 0
text_rect = text.get_rect()
text_rect.topleft = (font_x, font_y)

text2 = font.render(comp1, True, (0, 0, 0))
font_x = 0
font_y = 0
text_rect2 = text2.get_rect()
text_rect2.topleft = (font_x, font_y)

text3 = font.render(comp2, True, (0, 0, 0))
font_x = 0
font_y = 0
text_rect3 = text3.get_rect()
text_rect3.topleft = (font_x, font_y)

text4 = font.render(comp3, True, (0, 0, 0))
font_x = 0
font_y = 0
text_rect4 = text4.get_rect()
text_rect4.topleft = (font_x, font_y)

# print(pygame.font.get_fonts())

dice_numbers = []

dice_1_x_change = random.randint(3, 5)
dice_1_y_change = random.randint(3, 5)
dice_2_x_change = - random.randint(3, 5)
dice_2_y_change = random.randint(3, 5)
dice_3_x_change = random.randint(3, 5)
dice_3_y_change = - random.randint(3, 5)
dice_4_x_change = - random.randint(3, 5)
dice_4_y_change = - random.randint(3, 5)
dice_5_x_change = random.randint(3, 5)
dice_5_y_change = - random.randint(3, 5)
dice_6_x_change = - random.randint(3, 5)
dice_6_y_change = random.randint(3, 5)

# create the screen
screen = pygame.display.set_mode((game_width, game_height))
icon = pygame.image.load("gMoney.ico")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# image used but for maybe a colored box
# img0 = pygame.Surface((50, 50))
# img0.fill(image_color)

play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
play_button = button.Button(75, 65, play_img, 1)

new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
new_game_button = button.Button(75, 230, new_game_img, 1)

dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
dice_colors_button = button.Button(75, 620, dice_colors_img, 1)

instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
instructions_button = button.Button(525, 65, instructions_img, 1)

pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
pick_names_button = button.Button(525, 230, pick_names_img, 1)

quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
quit_button = button.Button(525, 620, quit_img, 1)

# color buttons

black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
black_button = button.Button(75, 65, black_img, 1)

white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
white_button = button.Button(75, 230, white_img, 1)

blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
blue_button = button.Button(75, 620, blue_img, 1)

menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
menu_button = button.Button(75, 785, menu_img, 1)

green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
green_button = button.Button(525, 65, green_img, 1)

yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
yellow_button = button.Button(525, 230, yellow_img, 1)

red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
red_button = button.Button(525, 620, red_img, 1)

purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
purple_button = button.Button(525, 785, purple_img, 1)

# buttons for the naming screen
player_img = pygame.image.load("buttons/player clicked.png").convert_alpha()
player_button = button.Button(75, 65, player_img, 1)

comp1_img = pygame.image.load("buttons/comp 1 clicked.png").convert_alpha()
comp1_button = button.Button(75, 180, comp1_img, 1)

comp2_img = pygame.image.load("buttons/comp 2 clicked.png").convert_alpha()
comp2_button = button.Button(525, 65, comp2_img, 1)

comp3_img = pygame.image.load("buttons/comp 3 clicked.png").convert_alpha()
comp3_button = button.Button(525, 180, comp3_img, 1)

name_entry_rect = pygame.Rect(250, 600, 500, 100)

names_entered = "Delete"

header = pygame.image.load("table.png").convert_alpha()
header = pygame.transform.scale(header, (1000, 1000))
font_x = 500
font_y = 500
header_rect = header.get_rect()
header_rect.center = (font_x, font_y)

info_for_player = pygame.image.load("do these.png").convert_alpha()
info_for_player = pygame.transform.scale(info_for_player, (600, 700))
info_for_player_x = 500
info_for_player_y = 420
info_for_player_rect = info_for_player.get_rect()
info_for_player_rect.center = (info_for_player_x, info_for_player_y)

notepad = pygame.image.load(f"notepad.png").convert_alpha()
notepad = pygame.transform.scale(notepad, (176, 330))
notepad_rect = notepad.get_rect()
notepad_rect.bottomright = (975, 975)

keep_rolling = False
active = False
spun = False
gaming = False
main_menu = True
dice_selection = False
instruction_menu = False
pick_names = False
while gaming or main_menu or dice_selection or instruction_menu or pick_names:

    turn_name = [player_name, comp1_name, comp2_name, comp3_name]
    turn_score = [player_score, comp1_score, comp2_score, comp3_score]

    dice_1_begin = pygame.image.load(f"{color}/dice 1.png").convert_alpha()
    dice_1_begin = pygame.transform.scale(dice_1_begin, (64, 64))
    dice_1_rect_begin = dice_1_begin.get_rect()
    dice_1_rect_begin.center = (dice_1_x, dice_1_y)

    dice_2_begin = pygame.image.load(f"{color}/dice 2.png").convert_alpha()
    dice_2_begin = pygame.transform.scale(dice_2_begin, (64, 64))
    dice_2_rect_begin = dice_2_begin.get_rect()
    dice_2_rect_begin.center = (dice_2_x, dice_2_y)

    dice_3_begin = pygame.image.load(f"{color}/dice 3.png").convert_alpha()
    dice_3_begin = pygame.transform.scale(dice_3_begin, (64, 64))
    dice_3_rect_begin = dice_3_begin.get_rect()
    dice_3_rect_begin.center = (dice_3_x, dice_3_y)

    dice_4_begin = pygame.image.load(f"{color}/dice 4.png").convert_alpha()
    dice_4_begin = pygame.transform.scale(dice_4_begin, (64, 64))
    dice_4_rect_begin = dice_4_begin.get_rect()
    dice_4_rect_begin.center = (dice_4_x, dice_4_y)

    dice_5_begin = pygame.image.load(f"{color}/dice 5.png").convert_alpha()
    dice_5_begin = pygame.transform.scale(dice_5_begin, (64, 64))
    dice_5_rect_begin = dice_5_begin.get_rect()
    dice_5_rect_begin.center = (dice_5_x, dice_5_y)

    dice_6_begin = pygame.image.load(f"{color}/dice 6.png").convert_alpha()
    dice_6_begin = pygame.transform.scale(dice_6_begin, (64, 64))
    dice_6_rect_begin = dice_6_begin.get_rect()
    dice_6_rect_begin.center = (dice_6_x, dice_6_y)
    while pick_names:
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption("Choose names for the player and computers:")
        screen.blit(header, header_rect)
        screen.blit(short_key_text, short_key_text_rect)
        if active is False:
            pygame.draw.rect(screen, (150, 150, 150), name_entry_rect)
        elif active:
            pygame.draw.rect(screen, (255, 255, 255), name_entry_rect)
        name_surface = short_key.render(names_entered, True, (0, 0, 0))
        name_surface_rect = name_surface.get_rect()
        name_surface_rect.width = 500
        name_surface_rect.height = 100
        screen.blit(name_surface, (250, 600))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name_entry_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.QUIT:
                gaming = False
                main_menu = False
                dice_selection = False
                instruction_menu = False
                pick_names = False
            if event.type == pygame.KEYDOWN:
                if active is False:
                    if event.key == pygame.K_g:
                        gaming = True
                        main_menu = False
                        dice_selection = False
                        instruction_menu = False
                        pick_names = False
                    if event.key == pygame.K_m:
                        gaming = False
                        main_menu = True
                        dice_selection = False
                        instruction_menu = False
                        pick_names = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        names_entered = names_entered[:-1]
                    else:
                        names_entered += event.unicode
            elif event.type == pygame.KEYUP and active:
                if event.key == pygame.K_BACKSPACE:
                    names_entered = names_entered[:-1]
        if menu_button.draw(screen):
            main_menu = True
            gaming = False
            dice_selection = False
            instruction_menu = False
            pick_names = False

        if player_button.draw(screen):
            player_name = names_entered
            names_entered = "Delete"
            write_to_scores = str(player_score) + "\n"
            write_to_scores += str(comp1_score) + "\n"
            write_to_scores += str(comp2_score) + "\n"
            write_to_scores += str(comp3_score) + "\n"
            write_to_scores += color + "\n"
            write_to_scores += player_name + "\n"
            write_to_scores += comp1_name + "\n"
            write_to_scores += comp2_name + "\n"
            write_to_scores += comp3_name + "\n"
            write_to_scores += str(comp1_greedy) + "\n"
            write_to_scores += str(comp2_greedy) + "\n"
            write_to_scores += str(comp3_greedy) + "\n"
            write_to_scores += str(turn)

            with open("greedyscores.txt", "w") as new_info:
                new_info.write(write_to_scores)
            time.sleep(1)
        if comp1_button.draw(screen):
            comp1_name = names_entered
            names_entered = "Delete"
            write_to_scores = str(player_score) + "\n"
            write_to_scores += str(comp1_score) + "\n"
            write_to_scores += str(comp2_score) + "\n"
            write_to_scores += str(comp3_score) + "\n"
            write_to_scores += color + "\n"
            write_to_scores += player_name + "\n"
            write_to_scores += comp1_name + "\n"
            write_to_scores += comp2_name + "\n"
            write_to_scores += comp3_name + "\n"
            write_to_scores += str(comp1_greedy) + "\n"
            write_to_scores += str(comp2_greedy) + "\n"
            write_to_scores += str(comp3_greedy) + "\n"
            write_to_scores += str(turn)

            with open("greedyscores.txt", "w") as new_info:
                new_info.write(write_to_scores)
            time.sleep(1)
        if comp2_button.draw(screen):
            comp2_name = names_entered
            names_entered = "Delete"
            write_to_scores = str(player_score) + "\n"
            write_to_scores += str(comp1_score) + "\n"
            write_to_scores += str(comp2_score) + "\n"
            write_to_scores += str(comp3_score) + "\n"
            write_to_scores += color + "\n"
            write_to_scores += player_name + "\n"
            write_to_scores += comp1_name + "\n"
            write_to_scores += comp2_name + "\n"
            write_to_scores += comp3_name + "\n"
            write_to_scores += str(comp1_greedy) + "\n"
            write_to_scores += str(comp2_greedy) + "\n"
            write_to_scores += str(comp3_greedy) + "\n"
            write_to_scores += str(turn)

            with open("greedyscores.txt", "w") as new_info:
                new_info.write(write_to_scores)
            time.sleep(1)
        if comp3_button.draw(screen):
            comp3_name = names_entered
            names_entered = "Delete"
            write_to_scores = str(player_score) + "\n"
            write_to_scores += str(comp1_score) + "\n"
            write_to_scores += str(comp2_score) + "\n"
            write_to_scores += str(comp3_score) + "\n"
            write_to_scores += color + "\n"
            write_to_scores += player_name + "\n"
            write_to_scores += comp1_name + "\n"
            write_to_scores += comp2_name + "\n"
            write_to_scores += comp3_name + "\n"
            write_to_scores += str(comp1_greedy) + "\n"
            write_to_scores += str(comp2_greedy) + "\n"
            write_to_scores += str(comp3_greedy) + "\n"
            write_to_scores += str(turn)

            with open("greedyscores.txt", "w") as new_info:
                new_info.write(write_to_scores)
            time.sleep(1)

        if 75 <= pos_mouse[0] <= 475:
            if 65 <= pos_mouse[1] <= 165:
                player_img = pygame.image.load("buttons/player unclicked.png").convert_alpha()
                player_button = button.Button(75, 65, player_img, 1)
            else:
                player_img = pygame.image.load("buttons/player clicked.png").convert_alpha()
                player_button = button.Button(75, 65, player_img, 1)
            if 180 <= pos_mouse[1] <= 280:
                comp1_img = pygame.image.load("buttons/comp 1 unclicked.png").convert_alpha()
                comp1_button = button.Button(75, 180, comp1_img, 1)
            else:
                comp1_img = pygame.image.load("buttons/comp 1 clicked.png").convert_alpha()
                comp1_button = button.Button(75, 180, comp1_img, 1)
            if 785 <= pos_mouse[1] <= 935:
                menu_img = pygame.image.load("buttons/menu unclicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
            else:
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
        elif 525 <= pos_mouse[0] <= 925:
            if 65 <= pos_mouse[1] <= 165:
                comp2_img = pygame.image.load("buttons/comp 2 unclicked.png").convert_alpha()
                comp2_button = button.Button(525, 65, comp2_img, 1)
            else:
                comp2_img = pygame.image.load("buttons/comp 2 clicked.png").convert_alpha()
                comp2_button = button.Button(525, 65, comp2_img, 1)
            if 180 <= pos_mouse[1] <= 280:
                comp3_img = pygame.image.load("buttons/comp 3 unclicked.png").convert_alpha()
                comp3_button = button.Button(525, 180, comp3_img, 1)
            else:
                comp3_img = pygame.image.load("buttons/comp 3 clicked.png").convert_alpha()
                comp3_button = button.Button(525, 180, comp3_img, 1)
        else:
            menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
            menu_button = button.Button(75, 785, menu_img, 1)
            player_img = pygame.image.load("buttons/player clicked.png").convert_alpha()
            player_button = button.Button(75, 65, player_img, 1)
            comp1_img = pygame.image.load("buttons/comp 1 clicked.png").convert_alpha()
            comp1_button = button.Button(75, 180, comp1_img, 1)
            comp2_img = pygame.image.load("buttons/comp 2 clicked.png").convert_alpha()
            comp2_button = button.Button(525, 65, comp2_img, 1)
            comp3_img = pygame.image.load("buttons/comp 3 clicked.png").convert_alpha()
            comp3_button = button.Button(525, 180, comp3_img, 1)
        pygame.display.update()
        clock.tick(fps)
    while instruction_menu:
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption("Game Rules and Instructions:")
        screen.blit(header, header_rect)
        screen.blit(info_for_player, info_for_player_rect)
        screen.blit(short_key_text, short_key_text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                main_menu = False
                dice_selection = False
                instruction_menu = False
                pick_names = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    gaming = True
                    main_menu = False
                    dice_selection = False
                    instruction_menu = False
                    pick_names = False
                if event.key == pygame.K_m:
                    gaming = False
                    main_menu = True
                    dice_selection = False
                    instruction_menu = False
                    pick_names = False

        if 75 <= pos_mouse[0] <= 475:
            if 785 <= pos_mouse[1] <= 935:
                menu_img = pygame.image.load("buttons/menu unclicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
            else:
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
        else:
            menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
            menu_button = button.Button(75, 785, menu_img, 1)

        if menu_button.draw(screen):
            main_menu = True
            gaming = False
            dice_selection = False
            instruction_menu = False
            pick_names = False

        pygame.display.update()
        clock.tick(fps)
    while dice_selection:
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption("Select Dice Color")
        screen.fill((95, 147, 65))
        screen.blit(header, header_rect)
        screen.blit(short_key_text, short_key_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                main_menu = False
                dice_selection = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    gaming = True
                    main_menu = False
                    dice_selection = False
                if event.key == pygame.K_m:
                    gaming = False
                    main_menu = True
                    dice_selection = False

        if black_button.draw(screen):
            color = "black"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if white_button.draw(screen):
            color = "white"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if blue_button.draw(screen):
            color = "blue"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if menu_button.draw(screen):
            main_menu = True
            gaming = False
            dice_selection = False
        if green_button.draw(screen):
            color = "green"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if yellow_button.draw(screen):
            color = "yellow"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if red_button.draw(screen):
            color = "red"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if purple_button.draw(screen):
            color = "purple"
            time.sleep(1)
            gaming = False
            main_menu = True
            dice_selection = False
        if 75 <= pos_mouse[0] <= 475:
            if 65 <= pos_mouse[1] <= 215:
                black_img = pygame.image.load("buttons/black unclicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 230 <= pos_mouse[1] <= 380:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white unclicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 620 <= pos_mouse[1] <= 770:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue unclicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 785 <= pos_mouse[1] <= 935:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu unclicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            else:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
        elif 525 <= pos_mouse[0] <= 925:
            if 65 <= pos_mouse[1] <= 215:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green unclicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 230 <= pos_mouse[1] <= 380:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow unclicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 620 <= pos_mouse[1] <= 770:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red unclicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            elif 785 <= pos_mouse[1] <= 935:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple unclicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
            else:
                black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
                black_button = button.Button(75, 65, black_img, 1)
                white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
                white_button = button.Button(75, 230, white_img, 1)
                blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
                blue_button = button.Button(75, 620, blue_img, 1)
                menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
                menu_button = button.Button(75, 785, menu_img, 1)
                green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
                green_button = button.Button(525, 65, green_img, 1)
                yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
                yellow_button = button.Button(525, 230, yellow_img, 1)
                red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
                red_button = button.Button(525, 620, red_img, 1)
                purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
                purple_button = button.Button(525, 785, purple_img, 1)
        else:
            black_img = pygame.image.load("buttons/black clicked.png").convert_alpha()
            black_button = button.Button(75, 65, black_img, 1)
            white_img = pygame.image.load("buttons/white clicked.png").convert_alpha()
            white_button = button.Button(75, 230, white_img, 1)
            blue_img = pygame.image.load("buttons/blue clicked.png").convert_alpha()
            blue_button = button.Button(75, 620, blue_img, 1)
            menu_img = pygame.image.load("buttons/menu clicked.png").convert_alpha()
            menu_button = button.Button(75, 785, menu_img, 1)
            green_img = pygame.image.load("buttons/green clicked.png").convert_alpha()
            green_button = button.Button(525, 65, green_img, 1)
            yellow_img = pygame.image.load("buttons/yellow clicked.png").convert_alpha()
            yellow_button = button.Button(525, 230, yellow_img, 1)
            red_img = pygame.image.load("buttons/red clicked.png").convert_alpha()
            red_button = button.Button(525, 620, red_img, 1)
            purple_img = pygame.image.load("buttons/purple clicked.png").convert_alpha()
            purple_button = button.Button(525, 785, purple_img, 1)
        pygame.display.update()
        clock.tick(fps)
    while main_menu:
        dice_1_rotated = pygame.transform.rotate(dice_1_begin, angle1)
        dice_1_rect_rotated = dice_1_rotated.get_rect()
        dice_1_rect_rotated.center = (dice_1_x, dice_1_y)

        dice_2_rotated = pygame.transform.rotate(dice_2_begin, angle2)
        dice_2_rect_rotated = dice_2_rotated.get_rect()
        dice_2_rect_rotated.center = (dice_2_x, dice_2_y)

        dice_3_rotated = pygame.transform.rotate(dice_3_begin, angle3)
        dice_3_rect_rotated = dice_3_rotated.get_rect()
        dice_3_rect_rotated.center = (dice_3_x, dice_3_y)

        dice_4_rotated = pygame.transform.rotate(dice_4_begin, angle4)
        dice_4_rect_rotated = dice_4_rotated.get_rect()
        dice_4_rect_rotated.center = (dice_4_x, dice_4_y)

        dice_5_rotated = pygame.transform.rotate(dice_5_begin, angle5)
        dice_5_rect_rotated = dice_5_rotated.get_rect()
        dice_5_rect_rotated.center = (dice_5_x, dice_5_y)

        dice_6_rotated = pygame.transform.rotate(dice_6_begin, angle6)
        dice_6_rect_rotated = dice_6_rotated.get_rect()
        dice_6_rect_rotated.center = (dice_6_x, dice_6_y)
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption("Greedy Main Menu")
        screen.blit(header, header_rect)
        screen.blit(dice_1_rotated, dice_1_rect_rotated)
        screen.blit(dice_2_rotated, dice_2_rect_rotated)
        screen.blit(dice_3_rotated, dice_3_rect_rotated)
        screen.blit(dice_4_rotated, dice_4_rect_rotated)
        screen.blit(dice_5_rotated, dice_5_rect_rotated)
        screen.blit(dice_6_rotated, dice_6_rect_rotated)
        screen.blit(short_key_text, short_key_text_rect)
        screen.blit(short_key2_text, short_key_text2_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                main_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    player_score = 0
                    comp1_score = 0
                    comp2_score = 0
                    comp3_score = 0
                    turn = 0
                    angle_speed = 0
                    rolled = False
                    spun = False
                    waiting = 0
                    brand_new_game = True
                if event.key == pygame.K_g:
                    gaming = True
                    main_menu = False
        if 75 <= pos_mouse[0] <= 475:
            if 65 <= pos_mouse[1] <= 215:
                play_img = pygame.image.load("buttons/play unclicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            elif 230 <= pos_mouse[1] <= 380:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game unclicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            elif 620 <= pos_mouse[1] <= 770:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors unclicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            else:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
        elif 525 <= pos_mouse[0] <= 925:
            if 65 <= pos_mouse[1] <= 215:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions unclicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            elif 230 <= pos_mouse[1] <= 380:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names unclicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            elif 620 <= pos_mouse[1] <= 770:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit unclicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
            else:
                play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
                play_button = button.Button(75, 65, play_img, 1)
                new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
                new_game_button = button.Button(75, 230, new_game_img, 1)
                dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
                dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
                instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
                instructions_button = button.Button(525, 65, instructions_img, 1)
                pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
                pick_names_button = button.Button(525, 230, pick_names_img, 1)
                quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
                quit_button = button.Button(525, 620, quit_img, 1)
        else:
            play_img = pygame.image.load("buttons/play clicked.png").convert_alpha()
            play_button = button.Button(75, 65, play_img, 1)
            new_game_img = pygame.image.load("buttons/new game clicked.png").convert_alpha()
            new_game_button = button.Button(75, 230, new_game_img, 1)
            dice_colors_img = pygame.image.load("buttons/dice colors clicked.png").convert_alpha()
            dice_colors_button = button.Button(75, 620, dice_colors_img, 1)
            instructions_img = pygame.image.load("buttons/instructions clicked.png").convert_alpha()
            instructions_button = button.Button(525, 65, instructions_img, 1)
            pick_names_img = pygame.image.load("buttons/pick names clicked.png").convert_alpha()
            pick_names_button = button.Button(525, 230, pick_names_img, 1)
            quit_img = pygame.image.load("buttons/quit clicked.png").convert_alpha()
            quit_button = button.Button(525, 620, quit_img, 1)
        if play_button.draw(screen):
            gaming = True
            main_menu = False
        if new_game_button.draw(screen):
            player_score = 0
            comp1_score = 0
            comp2_score = 0
            comp3_score = 0
            turn = 0
            comp1_greedy = random.choice(greedy_options)
            comp2_greedy = random.choice(greedy_options)
            comp3_greedy = random.choice(greedy_options)
            angle_speed = 0
            rolled = False
            spun = False
            waiting = 0
            brand_new_game = True
            winner = ""
        if dice_colors_button.draw(screen):
            gaming = False
            main_menu = False
            dice_selection = True
            time.sleep(1)
        if pick_names_button.draw(screen):
            gaming = False
            main_menu = False
            pick_names = True
            dice_selection = False
            instruction_menu = False
        if quit_button.draw(screen):
            gaming = False
            main_menu = False
        if instructions_button.draw(screen):
            gaming = False
            main_menu = False
            instruction_menu = True
        pygame.display.update()
        clock.tick(fps)
    while gaming:
        pygame.display.set_caption("Are You Feeling Greedy!?!?!?!")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    main_menu = True
                    gaming = False
                if event.key == pygame.K_r:
                    if rolled is False and winner == "" and turn == 0:
                        if len(saved_dice) == 6:
                            saved_dice = []
                            usable_fives = 0
                        number_of_dice = 6 - len(saved_dice)
                        dice_numbers = []
                        for i in range(number_of_dice):
                            dice_numbers.append(random.randint(1, 6))
                        spun = True
                        angle_speed = 20
                if event.key == pygame.K_k:
                    if rolled is False and winner == "" and turn == 0 and (player_score + score) <= 10000:
                        if player_score + score >= 1000:
                            rolled = True
                            kept = True
                if event.key == pygame.K_5:
                    if usable_fives >= 1 and len(saved_dice) > 1 and player_score >= 1000:
                        usable_fives -= 1
                        score -= 50
                        saved_dice.remove(5)
                        if rolled is False and winner == "" and turn == 0:
                            if len(saved_dice) == 6:
                                saved_dice = []
                                usable_fives = 0
                            number_of_dice = 6 - len(saved_dice)
                            dice_numbers = []
                            for i in range(number_of_dice):
                                dice_numbers.append(random.randint(1, 6))
                            spun = True
                            angle_speed = 20
                if event.key == pygame.K_s:
                    write_to_scores = str(player_score) + "\n"
                    write_to_scores += str(comp1_score) + "\n"
                    write_to_scores += str(comp2_score) + "\n"
                    write_to_scores += str(comp3_score) + "\n"
                    write_to_scores += color + "\n"
                    write_to_scores += player_name + "\n"
                    write_to_scores += comp1_name + "\n"
                    write_to_scores += comp2_name + "\n"
                    write_to_scores += comp3_name + "\n"
                    write_to_scores += str(comp1_greedy) + "\n"
                    write_to_scores += str(comp2_greedy) + "\n"
                    write_to_scores += str(comp3_greedy) + "\n"
                    write_to_scores += str(turn)

                    with open("greedyscores.txt", "w") as new_info:
                        new_info.write(write_to_scores)
                if event.key == pygame.K_n:
                    player_score = 0
                    comp1_score = 0
                    comp2_score = 0
                    comp3_score = 0
                    turn = 0
                    comp1_greedy = random.choice(greedy_options)
                    comp2_greedy = random.choice(greedy_options)
                    comp3_greedy = random.choice(greedy_options)
                    angle_speed = 0
                    rolled = False
                    spun = False
                    waiting = 0
                    brand_new_game = True
                    winner = ""

        notepad_rotated = pygame.transform.rotate(notepad, -20)
        notepad_rect_rotated = notepad_rotated.get_rect()
        notepad_rect_rotated.bottomright = (1000, 1000)

        word_x = notepad_rect_rotated[0]
        word_y = notepad_rect_rotated[1]

        rotated_text = pygame.transform.rotate(text, -20)
        rotated_text_rect = rotated_text.get_rect()
        rotated_text_rect.topleft = ((word_x + 95), (word_y + 35))

        rotated_text2 = pygame.transform.rotate(text2, -20)
        rotated_text2_rect = rotated_text2.get_rect()
        rotated_text2_rect.topleft = ((word_x + 85), (word_y + 60))

        rotated_text3 = pygame.transform.rotate(text3, -20)
        rotated_text3_rect = rotated_text3.get_rect()
        rotated_text3_rect.topleft = ((word_x + 75), (word_y + 85))

        rotated_text4 = pygame.transform.rotate(text4, -20)
        rotated_text4_rect = rotated_text4.get_rect()
        rotated_text4_rect.topleft = ((word_x + 67), (word_y + 110))

        if turn != 0 and spun is False and winner == "":
            if len(saved_dice) == 6:
                keep_rolling = True
            else:
                keep_rolling = False
            if (len(saved_dice)) == 4 or len(saved_dice) == 5:
                too_few_dice = True
                if usable_fives != 0 and len(saved_dice) == 4:
                    too_few_dice = False
            else:
                too_few_dice = False
            if turn == 1:
                if (((score >= comp1_greedy or too_few_dice) and keep_rolling is False) or score + comp1_score == 10000) and (comp1_score + score) <= 10000:
                    if comp1_score >= 1000 or score >= 1000:
                        if (score >= comp1_greedy or too_few_dice) and keep_rolling is False and (comp1_score + score) <= 10000:
                            kept = True
                            rolled = True
                    else:
                        if len(saved_dice) == 6:
                            saved_dice = []
                        number_of_dice = 6 - len(saved_dice)
                        dice_numbers = []
                        for i in range(number_of_dice):
                            dice_numbers.append(random.randint(1, 6))
                        spun = True
                        angle_speed = 20
                elif (comp1_score + score) > 10000:
                    kept = False
                    rolled = True
                    score = 12000
                else:
                    if len(saved_dice) == 6:
                        saved_dice = []
                    if usable_fives >= 1 and len(saved_dice) > 1 and (score >= 1000 or comp3_score >= 1000):
                        saved_dice.remove(5)
                        usable_fives -= 1
                        score -= 50
                    number_of_dice = 6 - len(saved_dice)
                    dice_numbers = []
                    for i in range(number_of_dice):
                        dice_numbers.append(random.randint(1, 6))
                    spun = True
                    angle_speed = 20
            elif turn == 2:
                if (((score >= comp2_greedy or too_few_dice) and keep_rolling is False) or score + comp2_score == 10000) and (comp2_score + score) <= 10000:
                    if comp2_score >= 1000 or score >= 1000:
                        if (score >= comp2_greedy or too_few_dice) and keep_rolling is False and (comp2_score + score) <= 10000:
                            kept = True
                            rolled = True
                    else:
                        if len(saved_dice) == 6:
                            saved_dice = []
                        if usable_fives >= 1 and len(saved_dice) > 1:
                            saved_dice.remove(5)
                            usable_fives -= 1
                            score -= 50
                        number_of_dice = 6 - len(saved_dice)
                        dice_numbers = []
                        for i in range(number_of_dice):
                            dice_numbers.append(random.randint(1, 6))
                        spun = True
                        angle_speed = 20
                elif (comp2_score + score) > 10000:
                    kept = False
                    rolled = True
                    score = 12000
                else:
                    if len(saved_dice) == 6:
                        saved_dice = []
                    if usable_fives >= 1 and len(saved_dice) > 1 and (score >= 1000 or comp3_score >= 1000):
                        saved_dice.remove(5)
                        usable_fives -= 1
                        score -= 50
                    number_of_dice = 6 - len(saved_dice)
                    dice_numbers = []
                    for i in range(number_of_dice):
                        dice_numbers.append(random.randint(1, 6))
                    spun = True
                    angle_speed = 20
            elif turn == 3:
                if (((score >= comp3_greedy or too_few_dice) and keep_rolling is False) or score + comp3_score == 10000) and (comp3_score + score) <= 10000:
                    if comp3_score >= 1000 or score >= 1000:
                        if (score >= comp3_greedy or too_few_dice) and keep_rolling is False and (comp3_score + score) <= 10000:
                            kept = True
                            rolled = True
                    else:
                        if len(saved_dice) == 6:
                            saved_dice = []
                        if usable_fives >= 1 and len(saved_dice) > 1:
                            saved_dice.remove(5)
                            usable_fives -= 1
                            score -= 50
                        number_of_dice = 6 - len(saved_dice)
                        dice_numbers = []
                        for i in range(number_of_dice):
                            dice_numbers.append(random.randint(1, 6))
                        spun = True
                        angle_speed = 20
                elif (comp3_score + score) > 10000:
                    kept = False
                    rolled = True
                    score = 12000
                else:
                    if len(saved_dice) == 6:
                        saved_dice = []
                    if usable_fives >= 1 and len(saved_dice) > 1 and (score >= 1000 or comp3_score >= 1000):
                        saved_dice.remove(5)
                        usable_fives -= 1
                        score -= 50
                    number_of_dice = 6 - len(saved_dice)
                    dice_numbers = []
                    for i in range(number_of_dice):
                        dice_numbers.append(random.randint(1, 6))
                    spun = True
                    angle_speed = 20

        if angle_speed > 0:
            switch_dice_counter += 1
            if len(dice_numbers) == 6:
                if switch_dice_counter % 40 == 0:
                    dice_1_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle1 += angle_speed
            else:
                dice_1_begin = pygame.image.load(f"{color}/dice {saved_dice[0]}.png").convert_alpha()
            if len(dice_numbers) >= 5:
                if switch_dice_counter % 40 == 0:
                    dice_2_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle2 += angle_speed
            else:
                dice_2_begin = pygame.image.load(f"{color}/dice {saved_dice[1]}.png").convert_alpha()
            if len(dice_numbers) >= 4:
                if switch_dice_counter % 40 == 0:
                    dice_3_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle3 += angle_speed
            else:
                dice_3_begin = pygame.image.load(f"{color}/dice {saved_dice[2]}.png").convert_alpha()
            if len(dice_numbers) >= 3:
                if switch_dice_counter % 40 == 0:
                    dice_4_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle4 += angle_speed
            else:
                dice_4_begin = pygame.image.load(f"{color}/dice {saved_dice[3]}.png").convert_alpha()
            if len(dice_numbers) >= 2:
                if switch_dice_counter % 40 == 0:
                    dice_5_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle5 += angle_speed
            else:
                dice_5_begin = pygame.image.load(f"{color}/dice {saved_dice[4]}.png").convert_alpha()
            if len(dice_numbers) >= 1:
                if switch_dice_counter % 40 == 0:
                    dice_6_begin = pygame.image.load(f"{color}/dice {random.randint(1, 6)}.png").convert_alpha()
                angle6 += angle_speed
            else:
                dice_6_begin = pygame.image.load(f"{color}/dice {saved_dice[5]}.png").convert_alpha()
            angle_speed -= .05
            if dice_1_x <= 100:
                dice_1_x += 10
                dice_1_x_change *= -1
            elif dice_1_x >= 340:
                dice_1_x -= 10
                dice_1_x_change *= -1
            if dice_2_x <= 390:
                dice_2_x += 10
                dice_2_x_change *= -1
            elif dice_2_x >= 612:
                dice_2_x -= 10
                dice_2_x_change *= -1
            if dice_3_x <= 658:
                dice_3_x += 10
                dice_3_x_change *= -1
            elif dice_3_x >= 900:
                dice_3_x -= 10
                dice_3_x_change *= -1
            if dice_1_y <= 100:
                dice_1_y += 10
                dice_1_y_change *= -1
            elif dice_1_y >= 340:
                dice_1_y -= 10
                dice_1_y_change *= -1
            if dice_2_y <= 100:
                dice_2_y += 10
                dice_2_y_change *= -1
            elif dice_2_y >= 340:
                dice_2_y -= 10
                dice_2_y_change *= -1
            if dice_3_y <= 100:
                dice_3_y += 10
                dice_3_y_change *= -1
            elif dice_3_y >= 340:
                dice_3_y -= 10
                dice_3_y_change *= -1
            if dice_4_x <= 100:
                dice_4_x += 10
                dice_4_x_change *= -1
            elif dice_4_x >= 340:
                dice_4_x -= 10
                dice_4_x_change *= -1
            if dice_5_x <= 390:
                dice_5_x += 10
                dice_5_x_change *= -1
            elif dice_5_x >= 612:
                dice_5_x -= 10
                dice_5_x_change *= -1
            if dice_6_x <= 658:
                dice_6_x += 10
                dice_6_x_change *= -1
            elif dice_6_x >= 900:
                dice_6_x -= 10
                dice_6_x_change *= -1
            if dice_4_y <= 360:
                dice_4_y += 10
                dice_4_y_change *= -1
            elif dice_4_y >= 640:
                dice_4_y -= 10
                dice_4_y_change *= -1
            if dice_5_y <= 360:
                dice_5_y += 10
                dice_5_y_change *= -1
            elif dice_5_y >= 640:
                dice_5_y -= 10
                dice_5_y_change *= -1
            if dice_6_y <= 360:
                dice_6_y += 10
                dice_6_y_change *= -1
            elif dice_6_y >= 640:
                dice_6_y -= 10
                dice_6_y_change *= -1

            if len(dice_numbers) == 6:
                dice_1_x += dice_1_x_change
                dice_1_y += dice_1_y_change
            if len(dice_numbers) >= 5:
                dice_2_x += dice_2_x_change
                dice_2_y += dice_2_y_change
            if len(dice_numbers) >= 4:
                dice_3_x += dice_3_x_change
                dice_3_y += dice_3_y_change
            if len(dice_numbers) >= 3:
                dice_4_y += dice_4_y_change
                dice_4_x += dice_4_x_change
            if len(dice_numbers) >= 2:
                dice_5_y += dice_5_y_change
                dice_5_x += dice_5_x_change
            if len(dice_numbers) >= 1:
                dice_6_x += dice_6_x_change
                dice_6_y += dice_6_y_change
        elif spun and angle_speed != 0:
            angle_speed = 0
            score_and_point_dice = score_calc.score_calculator(dice_numbers)
            if score_and_point_dice[0] != 0:
                score += score_and_point_dice[0]
            else:
                score = 0
            saved_dice += score_and_point_dice[2]
            for die in score_and_point_dice[2]:
                if dice_numbers.count(die) != 0:
                    dice_numbers.remove(die)
            dice_numbers.sort()

            if (turn_score[turn] + score) > 10000 and waiting == 0:
                kept = False
                rolled = True
                too_much = score
                score = 12000
            elif (turn_score[turn] + score) == 10000:
                kept = True
                rolled = True
            elif (turn_score[turn]) >= 1000:
                if 0 < score_and_point_dice[2].count(5) < 3:
                    usable_fives += score_and_point_dice[2].count(5)

            if len(dice_numbers) == 6:
                dice_1_begin = pygame.image.load(f"{color}/dice {dice_numbers[5]}.png").convert_alpha()
            else:
                dice_1_begin = pygame.image.load(f"{color}/dice {saved_dice[0]}.png").convert_alpha()
            if len(dice_numbers) >= 5:
                dice_2_begin = pygame.image.load(f"{color}/dice {dice_numbers[4]}.png").convert_alpha()
            else:
                dice_2_begin = pygame.image.load(f"{color}/dice {saved_dice[1]}.png").convert_alpha()
            if len(dice_numbers) >= 4:
                dice_3_begin = pygame.image.load(f"{color}/dice {dice_numbers[3]}.png").convert_alpha()
            else:
                dice_3_begin = pygame.image.load(f"{color}/dice {saved_dice[2]}.png").convert_alpha()
            if len(dice_numbers) >= 3:
                dice_4_begin = pygame.image.load(f"{color}/dice {dice_numbers[2]}.png").convert_alpha()
            else:
                dice_4_begin = pygame.image.load(f"{color}/dice {saved_dice[3]}.png").convert_alpha()
            if len(dice_numbers) >= 2:
                dice_5_begin = pygame.image.load(f"{color}/dice {dice_numbers[1]}.png").convert_alpha()
            else:
                dice_5_begin = pygame.image.load(f"{color}/dice {saved_dice[4]}.png").convert_alpha()
            if len(dice_numbers) >= 1:
                dice_6_begin = pygame.image.load(f"{color}/dice {dice_numbers[0]}.png").convert_alpha()
            else:
                dice_6_begin = pygame.image.load(f"{color}/dice {saved_dice[5]}.png").convert_alpha()
            if turn == 0:
                use_this = f"{player_name} let's see what you have there."
            elif turn == 1:
                use_this = f"{comp1_name} let's see what you have there."
            elif turn == 2:
                use_this = f"{comp2_name} let's see what you have there."
            else:
                use_this = f"{comp3_name} let's see what you have there."
            turn_text_text = turn_text.render(use_this, True, (0, 0, 0))
            rolled = True
        if angle_speed == 0 and len(dice_numbers) == 0 and len(saved_dice) == 0:
            dice_1_begin = pygame.image.load(f"{color}/dice 1.png").convert_alpha()
            dice_2_begin = pygame.image.load(f"{color}/dice 2.png").convert_alpha()
            dice_3_begin = pygame.image.load(f"{color}/dice 5.png").convert_alpha()
            dice_4_begin = pygame.image.load(f"{color}/dice 1.png").convert_alpha()
            dice_5_begin = pygame.image.load(f"{color}/dice 6.png").convert_alpha()
            dice_6_begin = pygame.image.load(f"{color}/dice 1.png").convert_alpha()

        if rolled:
            waiting += 1
            if waiting >= 200:
                waiting = 0
                rolled = False
                spun = False

                if kept:
                    saved_dice = []
                    kept = False
                    if turn == 0:
                        use_this = f"{player_name} kept {score}. {comp1_name} its your turn."
                        player_score += score
                        turn_score[turn] = player_score
                        usable_fives = 0
                        turn += 1
                    elif turn == 1:
                        use_this = f"{comp1_name} kept {score}. {comp2_name} its your turn."
                        comp1_score += score
                        turn_score[turn] = comp1_score
                        usable_fives = 0
                        turn += 1
                    elif turn == 2:
                        use_this = f"{comp2_name} kept {score}. {comp3_name} its your turn."
                        comp2_score += score
                        turn_score[turn] = comp2_score
                        usable_fives = 0
                        turn += 1
                    else:
                        use_this = f"{comp3_name} kept {score}. {player_name} its your turn."
                        comp3_score += score
                        turn_score[turn] = comp3_score
                        usable_fives = 0
                        turn = 0
                    turn_text_text = turn_text.render(use_this, True, (0, 0, 0))
                    score = 0
                elif score == 0:
                    saved_dice = []
                    if turn == 0:
                        use_this = f"{player_name} got nothing honey!! {comp1_name} roll em!!"
                        usable_fives = 0
                        turn += 1
                    elif turn == 1:
                        use_this = f"{comp1_name} got nothing honey!! {comp2_name} roll em!!"
                        usable_fives = 0
                        turn += 1
                    elif turn == 2:
                        use_this = f"{comp2_name} got nothing honey!! {comp3_name} roll em!!"
                        usable_fives = 0
                        turn += 1
                    else:
                        use_this = f"{comp3_name} got nothing honey!! {player_name} press r to roll em!!"
                        usable_fives = 0
                        turn = 0
                    turn_text_text = turn_text.render(use_this, True, (0, 0, 0))
                elif score == 12000:
                    saved_dice = []
                    if turn != 3:
                        if turn == 0:
                            use_this = f"Sorry {player_name}, {too_much} is too much!! {comp1_name} roll em!!"
                            usable_fives = 0
                            turn += 1
                        elif turn == 1:
                            use_this = f"Sorry {comp1_name}, {too_much} is too much!! {comp2_name} roll em!!"
                            usable_fives = 0
                            turn += 1
                        else:
                            use_this = f"Sorry {comp2_name}, {too_much} is too much!! {comp3_name} roll em!!"
                            usable_fives = 0
                            turn += 1
                    else:
                        use_this = f"Sorry {comp3_name}, {too_much} is too much!!"
                        use_this += f" {player_name} press r to roll em!!"
                        usable_fives = 0
                        turn = 0
                    turn_text_text = turn_text.render(use_this, True, (0, 0, 0))
                    score = 0
                else:
                    if usable_fives == 0 and turn == 0:
                        if score >= 1000 or player_score >= 1000:
                            use_this = f"{player_name} that's {score}. Press r to roll or k to keep it."
                        else:
                            use_this = f"{player_name} that's {score}. Press r to roll to get on the board."
                    elif usable_fives != 0 and turn == 0:
                        if score >= 1000 or player_score >= 1000:
                            if usable_fives >= 1 and len(saved_dice) > 1:
                                use_this = f"{turn_name[turn]} that's {score}. "
                                use_this += "Press r to roll, k to keep it or 5 to roll with a 5."
                            else:
                                use_this = f"{turn_name[turn]} that's {score}. "
                                use_this += "Press r to roll, k to keep it"
                        else:
                            use_this = f"{turn_name[turn]} that's {score}. "
                            use_this += "Press r to roll, k to keep it"
                    else:
                        if turn == 1:
                            use_this = f"{comp1_name} that's {score}."
                        elif turn == 2:
                            use_this = f"{comp2_name} that's {score}."
                        elif turn == 3:
                            use_this = f"{comp3_name} that's {score}."
                        else:
                            if turn == 1:
                                use_this = f"{comp1_name} that's {score}."
                            elif turn == 2:
                                use_this = f"{comp2_name} that's {score}."
                            else:
                                use_this = f"{comp3_name} that's {score}."
                    turn_text_text = turn_text.render(use_this, True, (0, 0, 0))

                if player_score == 10000:
                    winner = player_name
                elif comp1_score == 10000:
                    winner = comp1_name
                elif comp2_score == 10000:
                    winner = comp2_name
                elif comp3_score == 10000:
                    winner = comp3_name

        if rolled is False and spun is False and waiting == 0:
            if winner != "":
                use_this = f"{winner} is the winner with 10000. Press n to begin a new game."
                turn_text_text = turn_text.render(use_this, True, (0, 0, 0))

        dice_1_rotated = pygame.transform.rotate(dice_1_begin, angle1)
        dice_1_rect_rotated = dice_1_rotated.get_rect()
        dice_1_rect_rotated.center = (dice_1_x, dice_1_y)

        dice_2_rotated = pygame.transform.rotate(dice_2_begin, angle2)
        dice_2_rect_rotated = dice_2_rotated.get_rect()
        dice_2_rect_rotated.center = (dice_2_x, dice_2_y)

        dice_3_rotated = pygame.transform.rotate(dice_3_begin, angle3)
        dice_3_rect_rotated = dice_3_rotated.get_rect()
        dice_3_rect_rotated.center = (dice_3_x, dice_3_y)

        dice_4_rotated = pygame.transform.rotate(dice_4_begin, angle4)
        dice_4_rect_rotated = dice_4_rotated.get_rect()
        dice_4_rect_rotated.center = (dice_4_x, dice_4_y)

        dice_5_rotated = pygame.transform.rotate(dice_5_begin, angle5)
        dice_5_rect_rotated = dice_5_rotated.get_rect()
        dice_5_rect_rotated.center = (dice_5_x, dice_5_y)

        dice_6_rotated = pygame.transform.rotate(dice_6_begin, angle6)
        dice_6_rect_rotated = dice_6_rotated.get_rect()
        dice_6_rect_rotated.center = (dice_6_x, dice_6_y)

        if brand_new_game:
            brand_new_game = False
            use_this = f"{player_name} please press r to begin a new round."
            turn_text_text = turn_text.render(use_this, True, (0, 0, 0))
        text = font.render(f"{player_name} {player_score}", True, (0, 0, 0))
        text2 = font.render(f"{comp1_name} {comp1_score}", True, (0, 0, 0))
        text3 = font.render(f"{comp2_name} {comp2_score}", True, (0, 0, 0))
        text4 = font.render(f"{comp3_name} {comp3_score}", True, (0, 0, 0))
        screen.blit(header, header_rect)
        screen.blit(turn_text_text, turn_text_rect)
        screen.blit(notepad_rotated, notepad_rect_rotated)
        screen.blit(short_key_text, short_key_text_rect)
        screen.blit(short_key2_text, short_key_text2_rect)
        screen.blit(rotated_text, rotated_text_rect)
        screen.blit(rotated_text2, rotated_text2_rect)
        screen.blit(rotated_text3, rotated_text3_rect)
        screen.blit(rotated_text4, rotated_text4_rect)
        screen.blit(dice_1_rotated, dice_1_rect_rotated)
        screen.blit(dice_2_rotated, dice_2_rect_rotated)
        screen.blit(dice_3_rotated, dice_3_rect_rotated)
        screen.blit(dice_4_rotated, dice_4_rect_rotated)
        screen.blit(dice_5_rotated, dice_5_rect_rotated)
        screen.blit(dice_6_rotated, dice_6_rect_rotated)

        pygame.display.update()
        clock.tick(fps)

write_to_scores = str(player_score) + "\n"
write_to_scores += str(comp1_score) + "\n"
write_to_scores += str(comp2_score) + "\n"
write_to_scores += str(comp3_score) + "\n"
write_to_scores += color + "\n"
write_to_scores += player_name + "\n"
write_to_scores += comp1_name + "\n"
write_to_scores += comp2_name + "\n"
write_to_scores += comp3_name + "\n"
write_to_scores += str(comp1_greedy) + "\n"
write_to_scores += str(comp2_greedy) + "\n"
write_to_scores += str(comp3_greedy) + "\n"
write_to_scores += str(turn)

with open("greedyscores.txt", "w") as new_info:
    new_info.write(write_to_scores)

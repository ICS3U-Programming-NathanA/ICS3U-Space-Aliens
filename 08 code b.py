#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Jan.9, 2022
# This program is called "Space Attack" program on the PyBadge


import stage
import ugame
import time
import random

# imports the constants file
import constants


def splash_scene():
    # this function is the main game scene
    menu_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # gets the background image from the file for the menu_scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a grid on the pybadge for the background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # displays the images on screen at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # create layers on the pybadge
    # take images and add them to a list
    game.layers = [background]
    game.render_block()

    # repeat forever game loop
    while True:
        # pauses for 2 seconds
        time.sleep(2.0)
        menu_scene()


def menu_scene():

    # this function is the main game scene

    # gets the background image from the file for the menu_scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    menu_sound = open("menu.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    music_loop = 0

    # add text objects
    text = []
    # customization for the text
    # text 3 width is 29, height is 12 and set the palette to the constants RED_PALETTE
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move the text to (20, 10)
    text1.move(20, 10)
    # What the text says
    text1.text("Faster than Light")
    # add text to a list
    text.append(text1)

    # customization for the text
    # text 2 width is 29, height is 12 and set the palette to the constants RED_PALETTE
    text2 = stage.Text(
        width=24, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move the text to (40, 110)
    text2.move(40, 110)
    # What the text says
    text2.text("PRESS START")
    # add text to a list
    text.append(text2)

    # create a grid on the pybadge for the background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # displays the images on screen at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # create layers on the pybadge
    # take images and add them to a list
    game.layers = text + [background]
    game.render_block()

    sound.play(menu_sound)
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # If they press the start key
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw sprites
        game.tick()
        # play sound
        if music_loop >= 1875.96000075:
            sound.play(menu_sound)
            music_loop = 0
        else:
            music_loop += 1


def game_scene():

    # this function is the main game scene

    # gets the background image from the file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # gets the sprite from the file
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons you want to keep information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # create a grid on the pybadge for the background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # display the sprite that updates every frame
    ship = stage.Sprite(
        image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    alien = stage.Sprite(
        image_bank_sprite,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    # displays the images on screen at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # create layers on the pybadge
    # take images and add them to a list
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # If they press the "A" key
        if keys & ugame.K_X != 0:
            # if the a button is up
            if a_button == constants.button_state["button_up"]:
                # set it to being button pressed
                a_button = constants.button_state["button_just_pressed"]
                # elif the button is just pressed
            elif a_button == constants.button_state["button_just_pressed"]:
                # make sure it does not repeat, if the button is pressed once and it is still held down
                a_button = constants.button_state["button_still_pressed"]
        else:
            # if the a button is still pressed
            if a_button == constants.button_state["button_still_pressed"]:
                # set a button to it being released
                a_button = constants.button_state["button_released"]
            else:
                # else if button is up
                a_button = constants.button_state["button_up"]
        # If they press the "B" key
        if keys & ugame.K_O:
            pass
        # If they press the start key
        if keys & ugame.K_START:
            pass
        # If they press the select key
        if keys & ugame.K_SELECT:
            pass
        # If they press the right key
        if keys & ugame.K_RIGHT:
            # if statement to check if its at the right side of the screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        # If they press the left key
        if keys & ugame.K_LEFT:
            # if statement to check if its at the left side of the screen
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # If they press the up key
        if keys & ugame.K_UP:
            pass
        # If they press the down key
        if keys & ugame.K_DOWN:
            pass

        # update game logic
        # play the shoot sound if button "A" is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # redraw sprites/alien
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    splash_scene()

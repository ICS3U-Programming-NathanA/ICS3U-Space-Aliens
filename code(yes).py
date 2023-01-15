#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Jan.9, 2022
# This program is called "Space Attack" program on the PyBadge


import stage
import ugame

# imports the constants file
import constants


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
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                # make sure it does not repeat, if the button is pressed once and it is still held down
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
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
    game_scene()

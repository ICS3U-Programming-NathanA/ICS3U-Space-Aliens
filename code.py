#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Jan.9, 2022
# This program is called "Space Attack" program on the PyBadge


import stage
import ugame
import time
import random
import supervisor
# imports the constants file
import constants


def splash_scene():
    # this function is the main game scene
    splash_scene_sound = open("coin.wav", "rb")
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
    sound.play(splash_scene_sound)
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

    # text 2 width is 29, height is 12 and set the palette to the constants RED_PALETTE
    text3 = stage.Text(
        width=24, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move the text to (40, 110)
    text3.move(5, 50)
    # What the text says
    text3.text("Press B to see")
    # add text to a list
    text.append(text3)

        # text 2 width is 29, height is 12 and set the palette to the constants RED_PALETTE
    text4 = stage.Text(
        width=24, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # move the text to (40, 110)
    text4.move(5, 62)
    # What the text says
    text4.text("instructions")
    # add text to a list
    text.append(text4)

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
        # Check if the "B" button is pressed
        if keys & ugame.K_O != 0:
            instructions_scene()
        # redraw sprites
        game.tick()
        # play sound
        if music_loop >= 1875.96000075:
            sound.play(menu_sound)
            music_loop = 0
        else:
            music_loop += 1


def instructions_scene():
    # This function displays the instructions scene

    # Load the image "mt_game_studio.bmp" for the background
    # The background will be white
    image_bank_3 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Add text objects for the menu scene
    text = []
    # Create a Text object with a width of 15, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=15,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 10)
    text1.move(5, 10)
    # Set the text to "AQUA-KINGDOM : INSTRUCTIONS"
    text1.text("INSTRUCTIONS")
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 50)
    text2.move(5, 25)
    # Set the text
    text2.text("Get highest score")
    # Add the text object to the text list
    text.append(text2)

    # Create a Text object with a width of 20, height of 12, no font, and the red palette
    text3 = stage.Text(
        width=20,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )

    # Move the text to the position (20, 90)
    text3.move(5, 37)
    # Set the text
    text3.text("Move and shoot")
    # Add the text object to the text list
    text.append(text3)

    # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text4 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 70)
    text4.move(5, 49)
    # Set the text
    text4.text("By pressing the")
    # Add the text object to the text list
    text.append(text4)

    # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text5 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 70)
    text5.move(5, 61)
    # Set the text
    text5.text("buttons on the")
    # Add the text object to the text list
    text.append(text5)

        # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text6 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 70)
    text6.move(5, 73)
    # Set the text
    text6.text("left and the")
    # Add the text object to the text list
    text.append(text6)

            # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text7 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 70)
    text7.move(5, 85)
    # Set the text
    text7.text("A button")
    # Add the text object to the text list
    text.append(text7)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    # For the instructions scene, we only need the background and text
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Get user input (buttons pressed)
        keys = ugame.buttons.get_pressed()

        # Check if the 'A' button is pressed
        if keys & ugame.K_X != 0:
            # If the 'A' button is pressed, run the menu scene
            menu_scene()

        game.tick()

def game_scene():

    # set the score to 0
    score = 0
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))
    def show_alien():
        # this function takes amd alien off screen and moves it on screen
        for alien_number in range(len(aliens)):
            # Check if the x position of the alien is less than 0
            if aliens[alien_number].x < 0:
                # If so, move the alien to a random position on the x-axis within the screen's width 
                # and off the top of the screen
                aliens[alien_number].move(
                    random.randint(
                     # left edge of the screen
                        0 + constants.SPRITE_SIZE,
                         # right edge of the screen
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                     # off the top of the screen
                    constants.OFF_TOP_SCREEN,
                )
                # Exit the loop
                break
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

    # get sound ready
    boom_sound = open("boom.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # get sound ready
    crash_sound = open("crash.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # create a grid on the pybadge for the background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # randomizes the background for game_scene
    # finds the next x value
    for x_location in range(constants.SCREEN_GRID_X):
        # finds the next y value
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # display the sprite that updates every frame
    ship = stage.Sprite(
        image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # create a list of the aliens
    aliens = []
    # Loop through all the aliens
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprite, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)
    # calls show_alien()
    show_alien()

    # create a list of the lasers for when we shoot
    lasers = []
    # Loop through all the lasers
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprite, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

    # displays the images on screen at 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # create layers on the pybadge
    # take images and add them to a list
    game.layers = [score_text] + lasers + [ship] + aliens + [background]
    # render the background and initial location of the sprite list
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
            # fire a laser, if we have enough power
            for laser_number in range(len(lasers)):
                # check if the x position of the laser is less then 0
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # each frame move the lasers
        for laser_number in range(len(lasers)):
            # check if the laser is in the frame
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                # Check if the laser has gone off the top of the screen
                # If it has, move it offscreen and play the laser sound effect
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
        # each frame move the lasers
        for alien_number in range(len(lasers)):
            # check if the laser is in the frame
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                # Check if the laser has gone off the top of the screen
                # If it has, move it offscreen and play the laser sound effect
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    show_alien()
                    score -= 1
                    # if the score is less than 0
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))
        # Iterate through all the lasers
        for laser_number in range(len(lasers)):
            # Check if the laser is still on the screen (x position is greater than 0)
            if lasers[laser_number].x > 0:
                  # Iterate through all the aliens
                for alien_number in range(len(aliens)):
                # Check if the alien is still on the screen (x position is greater than 0)
                    if aliens[alien_number].x > 0:
                        # Check if the laser and alien are colliding
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1, aliens[alien_number].y,
                            aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # when you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
        # Iterate through all the aliens
        for alien_number in range(len(aliens)):
            # Check if the aliens are still on the screen (x position is greater than 0)
            if aliens[alien_number].x > 0:
                # Check if the alien and ship are colliding
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                ship.x, ship.y,
                ship.x + 15, ship.y - 15):
                    # alien hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)

        # redraw sprites/alien
        game.render_sprites(lasers + [ship] + aliens)
        # wait until refresh rate finishes
        game.tick()

def game_over_scene(final_score):

    sound = ugame.audio
    sound.stop()

    # image banks for circuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the image bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # makes a list called text
    text = []
    # customizes the text
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    # The texts position
    text1.move(22,20)
    # What the text displays
    text1.text("Final Score: {:0>2d}".format(final_score))
    # add text to the list
    text.append(text1)

    # customizes the text2
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    # The texts position
    text2.move(22,55)
    # What the text displays
    text2.text("GAME OVER")
    # add text to the list
    text.append(text2)

    # customizes the text3
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None)
    # The texts position
    text3.move(32,110)
    # What the text displays
    text3.text("PRESS SELECT")
    # add text to the list
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]

    game.render_block()


    while True:

        keys = ugame.buttons.get_pressed()

        # Check if the SELECT button is pressed
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

            game.tick()


if __name__ == "__main__":
    splash_scene()

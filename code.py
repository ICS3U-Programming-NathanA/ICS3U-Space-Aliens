#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Jan.9, 2022
# This program is called "Space Attack" program on the PyBadge

import ugame
import stage


def game_scene():

    # this function is the main game scene

    # gets the image from the file
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # create a grid on the pybadge
    background = stage.Grid(image_bank_background, 10, 8)

    # displays the images on screen at 60fps
    game = stage.Stage(ugame.display, 60)
    # create layers on the pybadge
    # take images and add them to a list
    game.layers = [background]
    game.render_block()

    while True:
        # repeat forever, or you turn it off
        pass


if __name__ == "__main__":
    game_scene()

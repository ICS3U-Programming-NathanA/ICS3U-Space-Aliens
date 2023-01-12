#!/usr/bin/env python3
 
# Created by: Nathan Araujo
# Date: Jan.9, 2022
# This program is called "Space Attack" program on the PyBadge
 
import stage
import ugame
 
def game_scene():
 
   # this function is the main game scene
 
   # gets the background image from the file
   image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
   # gets the sprite from the file
   image_bank_sprite = stage.Bank.from_bmp16("space_aliens_good.bmp")
 
   # create a grid on the pybadge for the background
   background = stage.Grid(image_bank_background, 10, 8)
   # display the sprite that updates every frame
   ship = stage.Sprite(image_bank_sprite, 5, 75, 66)
   # displays the images on screen at 60fps
   game = stage.Stage(ugame.display, 60)
   # create layers on the pybadge
   # take images and add them to a list
   game.layers = [ship]+[background]
   game.render_block()
 
   while True:
       # get user input
 
       # update game logic
 
       # redraw sprites
       game.render_sprites([ship])
       game.tick()
 
if __name__ == "__main__":
   game_scene()
 

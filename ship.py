#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: ship.py
# @Author: Longwei Zhang
# @Create Time: 5/1/25 18:33
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


import pygame


class Ship():
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based one the movement flag"""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)
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
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def bilitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)
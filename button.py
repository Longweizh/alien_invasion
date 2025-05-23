#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: button.py
# @Author: Longwei Zhang
# @Create Time: 5/9/25 04:50
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


import pygame


class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and the properties of the button
        self.width, self.height = 200, 50
        self.button_color = (232, 119, 34)
        self.text_color = (0, 60, 165)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                    self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: scoreboard.py
# @Author: Longwei Zhang
# @Create Time: 5/12/25 15:55
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================

import pygame.font
class Scoreboard:
    """A class representing the score"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings
        self.text_color = (232, 119, 34)
        self.font = pygame.font.SysFont('None', 48)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)

        # Display the score on top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
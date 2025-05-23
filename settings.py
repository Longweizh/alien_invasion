#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: settings.py
# @Author: Longwei Zhang
# @Create Time: 5/1/25 18:07
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize the game's setting"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (19, 41, 75)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (232, 74, 39)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        # How quickly the game speed up
        self.speed_scale = 1.1

        # How quickly the score speed up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1
        self.alien_points = 50

        # Fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        #print(self.alien_points)




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
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (232, 74, 39)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1
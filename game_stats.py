#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: game_stats.py
# @Author: Longwei Zhang
# @Create Time: 5/8/25 18:44
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


class GameStats:
    """track game stats"""

    def __init__(self,ai_game):
        """Initialize game stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize game stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
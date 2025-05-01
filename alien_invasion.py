#!/usr/bin/python3
# -*- coding=utf-8 -*-

# ===================================
# @Filename: alien_invasion.py
# @Author: Longwei Zhang
# @Create Time: 5/1/25 16:13
# @Email:lz539@georgetown.edu
# @Description: 
# ===================================


import sys
import pygame


class AlienInvasion:
    """Overall class to manage Alien Invasion"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()



"""
File: template.py
Author: Your Name
Date: 2024-03-20
Description: Template for basic Pygame graphics setup.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Program")

# Define colours from https://www.pygame.org/docs/ref/color_list.html
WHITE = (255, 255, 255)
RED = (200, 16, 46)
BLUE = (1, 33, 105)

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(BLUE)
    pygame.draw.line(screen, WHITE, (0, 400), (600, 0), 75)
    pygame.draw.line(screen, WHITE, (0, 0), (600, 400), 75)
    pygame.draw.line(screen, RED, (300, 185), (600, -15), 25)
    pygame.draw.line(screen, RED, (300, 185), (600, 385), 25)
    pygame.draw.line(screen, RED, (300, 215), (0, 15), 25)
    pygame.draw.line(screen, RED, (300, 215), (0, 415), 25)
    pygame.draw.line(screen, WHITE, (300, 0), (300, 400), 100)
    pygame.draw.line(screen, WHITE, (0, 200), (600, 200), 100)
    pygame.draw.line(screen, RED, (300, 0), (300, 400), 66)
    pygame.draw.line(screen, RED, (0, 200), (600, 200), 66)

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()

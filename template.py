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
WHITE = pygame.Color("white")
GREY = pygame.Color("gray67")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREY, (300, 200), 50)

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()

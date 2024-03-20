"""
File: demo.py
Author: Dave Cheng
Date: 2024-03-20
Description: Demonstration of basic Pygame setup with graphics drawing functions.
"""

# IMPORTING LIBRARIES
# This enables the Pygame library function in your Python program.
# Necessary for all Pygame programs. Do not change this line.
import pygame
import sys

# INITIALIZE PYGAME
# Necessary for all Pygame programs. Do not change this line.
pygame.init()

# SET UP DISPLAY AREA
# This sets up the Pygame window that opens when you run the program. You can 
# modify the size of the window as well as its caption.
width, height = 600, 400                    # CHANGE THIS LINE FOR SIZE
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Program")    # CHANGE THIS LINE FOR WINDOW TITLE

# COLOUR NAME DEFINITIONS
# Define easy-to-remember names for colours. Note these variable names are in 
# ALL CAPS, denoting CONSTANTS that will not change throughout the program.
#
# Define colours manually using RGB values from https://rgbcolorpicker.com/
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Define preset named colours from https://www.pygame.org/docs/ref/color_list.html
RED = pygame.Color("crimson")
GREY = pygame.Color("gray67")

# MAIN LOOP
# Pygame is essentially a continuous loop that redraws the screen graphics
# contents over and over again until some condition causes it to quit.
# The `running` variable and `while` loop sets this up. 

running = True

while running:
    # EVENT HANDLER
    # This section determines when to stop Pygame. In our case, the
    # only condition to end the program is when the user closes the
    # Pygame graphics window. When the user closes the window, this
    # sets the `running` variable to `False` and stop Pygame.
    # Do not remove this section.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # GRAPHICS
    # Here is where you draw all of your screen elements. You can 
    # customize this section as much as you'd like.
    screen.fill(WHITE)

    pygame.draw.line(screen, RED, (50, 50), (150, 50), 5)
    pygame.draw.circle(screen, GREY, (250, 100), 50)
    pygame.draw.rect(screen, RED, pygame.Rect(350, 50, 100, 80))
    pygame.draw.ellipse(screen, GREY, pygame.Rect(100, 200, 150, 100))
    pygame.draw.arc(screen, BLACK, pygame.Rect(300, 200, 100, 100), 0, 3.14)
    pygame.draw.polygon(screen, RED, [(500, 200), (550, 250), (450, 250)])

    # UPDATE DISPLAY
    # Update the window to show the graphics.
    pygame.display.flip()

# QUIT PYGAME
# Main loop has exited, so stop Pygame running.
pygame.quit()
sys.exit()

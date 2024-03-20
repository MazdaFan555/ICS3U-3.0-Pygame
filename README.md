# Introduction to Pygame

Pygame is a popular Python library designed for writing video games and interactive programs. It provides functionalities to handle graphics, sound, and user input, making it a versatile tool for game development.

## Installing Pygame
You have to manually install Pygame on your local development environment before you can start coding with it. If you've followed my setup procedures [here](https://docs.google.com/document/d/140jEi-QY2gCjiQ8Qbi7BuEOaEHQ6UFc0riZlkPmict4), then continue with the following steps to add Pygame to you machine.

### Pygame on macOS
In Visual Studio Code, open a terminal window and run the command:

```
python3 -m pip install -U pygame==2.5.2 --user
```

If you get an error, try the command with the explicit path to your Python installation:

```
 /usr/local/bin/python3 -m pip install -U pygame==2.5.2 --user
 ```

### Pygame on Windows
In Visual Studio Code, open a terminal window and run the command:

```
python -m pip install -U pygame==2.5.2 --user
```

If you get an error, specify the path to the Python installation in your command It should look something like:

```
C:\Users\YOURNAME\AppData\Local\Programs\Python\Python312\python.exe
```

where YOURNAME is your Windows username. This also assumes you downloaded and installed version Python 3.12 to get Python312 in the path. 

If you are not sure about your path, you can find where Python is installed manually with the following steps:

- Type python in the Windows Search Bar.
- Right-click the Python App and then select Open file location.
- Right-click again on the Python shortcut and then select Open file location.
- You should now get a location (path) where Python is installed on Windows. It should look something like: 
```
C:\Users\YOURNAME\AppData\Local\Programs\Python\Python312 
```

Finally, use this path to run the Pygame installation command in a terminal:

```
C:\Users\Cheng\AppData\Local\Programs\Python\Python312\python -m pip install -U pygame==2.5.2 --user
```

## Pygame Template
Let us take a look at a simple Pygame program:

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Basic Shapes in Pygame")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw various shapes
    pygame.draw.line(screen, RED, (50, 50), (150, 50), 5)
    pygame.draw.circle(screen, GREEN, (250, 100), 50)
    pygame.draw.ellipse(screen, BLUE, (350, 50, 100, 80))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(100, 200, 150, 100))
    pygame.draw.arc(screen, CYAN, pygame.Rect(300, 200, 100, 100), 0, 3.14)
    pygame.draw.polygon(screen, MAGENTA, [(500, 200), (550, 250), (450, 250)])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
```

In this program:

- We import the Pygame module and initialize it.
- We set up a 600x400 window.
- We define colors for various shapes.
- In the main game loop, we handle quitting the program when the window is closed (`pygame.QUIT` event).
- We fill the screen with white (`WHITE` color) on each iteration of the loop.
- We draw various shapes using Pygame's drawing functions (`pygame.draw.line()`, `pygame.draw.circle()`, `pygame.draw.ellipse()`, `pygame.draw.rect()`, `pygame.draw.arc()`, `pygame.draw.polygon()`).
- We update the display to show the drawn shapes.
- When the user closes the window, we quit Pygame and exit the program.

In this repo, you can use `template.py` for a basic framework or starting point for your own program. 

## Working Demonstration
In this repo, you can check out `demo.py` for a fully-commented, running demonstration of some basic shapes drawn in Pygame.

## Additional Documentation
There is a lot of helpful documentation online. To start, you can check out:
- [pygame.draw()](https://www.pygame.org/docs/ref/draw.html) - Pygame module for drawing shapes.
- [pygame.color()](https://www.pygame.org/docs/ref/color.html) - Pygame module for defining colours. You can use a [list of predefined colour names](https://www.pygame.org/docs/ref/color_list.html) or pick your own custom RGB values with a [colour picker](https://rgbcolorpicker.com/).


## Practice Challenges
Now that you have your own Pygame installation library running, try to use the `pygame.draw()` functions with these challenges:

### 1. Flags of the World
Pick a country's flag of the world and draw it. Start easy with simple shapes (e.g. France, Italy, Japan) and increase difficulty with more complex designs (e.g. Canada, China). Add a flagpole to finish your design.

### 2. Brand Logos
Pick a well-known logo for a popular brand and draw it. Deconstruct the logo into its components -- simple geometric shapes, polygones, lines, etc.
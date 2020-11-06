# -------- IMPORTS -------------
from grid_functions import *
import pygame
import time
import numpy as np
#-------------------------------


pygame.init() # Pygame initialization


# ------------------------ PYGAME GET COLORS --------------------------
color_list = []
cbb = 200 # Color bright boundary

for x in pygame.colordict.THECOLORS.items():
    if (not (x[1][0] >= cbb and x[1][1] >= cbb and x[1][2] >= cbb)\
        and (not (x[1][0] == x[1][1] == x[1][2]))): # No grayscale/very light colors
        color_list.append(x[1])
# ---------------------------------------------------------------------

pause = True # Main Pause Control

# ------------------------ GLOBAL CHANGE VARIABLES --------------------

d = 15 # Dimensions of each square

nX = 100 # Number of squares in axis X
nY = 60 # Number of squares in axis Y

# ---------------------------------------------------------------------

# ------------------------ SCREEN DISPLAY -----------------------------
w,h = nX * d, nY * d # Calculating width and height of desired screen

screen = pygame.display.set_mode((w,h))
bg = 255,255,255 # Background color (currently set to white)
screen.fill(bg)
# ---------------------------------------------------------------------

               
# ------------------------ MAIN GRID CREATION -------------------------

grid = create_grid(nY,nX)

# ---------------------------------------------------------------------

# ------------------------ ASSIGN COLOR PER COLUMN --------------------

color = create_grid(nY,nX)

offset = np.random.randint(len(color_list) - nX)

for c in range(len(grid[0])):
    for r in range(len(grid)):
        color[r][c] = color_list[c%len(color_list) + offset]
        
# ---------------------------------------------------------------------
       

# ------------------------- MAIN EXECUTION LOOP -----------------------

while True:
    screen.fill(bg)
    
    for x in range(nX):
        for y in range(nY):
            polygon = [(x*d,y*d),((x+1)*d,y*d),((x+1)*d,(y+1)*d),(x*d,(y+1)*d)] # Get corners of square
            
            pygame.draw.polygon(screen, (0,0,0), polygon,1) # Draw grid
            
            if grid[y][x] != 0: # If alive draw assigned color
                pygame.draw.polygon(screen, color[y][x], polygon,0)
    
    if not pause: # If game is not paused, update the next generation
        grid = next_gen(grid)
        t = 0.1
    else:
        t = 0 # Time is set to zero when paused so painting is more fluent
        
    pygame.display.flip() # Display game
    time.sleep(t) # Wait t seconds
    
    
    # ------------ EVENT CONTROLS --------------
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Space pauses game
            pause = not pause
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:   # R resets game space
            grid = create_grid(nY,nX)
        
        mC = pygame.mouse.get_pressed() # Get mouse buttong events
        
        if sum(mC) > 0: # If a mouse button is pressed
            mX, mY = pygame.mouse.get_pos() # Mouse position variables
            gridX = int(np.floor(mX // d)) # Calculate which square it is X
            gridY = int(np.floor(mY // d)) # Calculate which square it is Y
            if gridY < nY and gridX < nX:
                grid[gridY][gridX] = not mC[2] # If left click -> Alive. Otherwise -> Dead
    # -----------------------------------------

# ----------------------- END OF MAIN EXECUTION LOOP -------------------
                
            
            
import os

import sys, pygame

import models.pokemon as pokemon
import const.initials as cinitials
import const.files as cfiles
import helpers.files as hfiles
import helpers.jsonparser as jparser
import const.colors as colors
import configuration as config

# Initializing parameters
size = width, height = config.SCREEN_WIDTH, config.SCREEN_HEIGHT
speed = [2,2]
horizontalSpace = config.HORIZONTAL_SPACE
verticalSpace = config.VERTICAL_SPACE
cursorY = config.CURSOR_INITIAL_POSITION_Y
cursorX = config.CURSOR_INITIAL_POSITION_X
firstRow = 0

# Starting game
pygame.init()
pygame.display.set_caption('Pkmn Combat Simulator')
screen = pygame.display.set_mode(size)

# Get pokemons in a matrix
pkmnMatrix = []
pkmnRow = []
pkmnJSON = hfiles.readAllPkmn(cfiles.PKMN_JSON_PATH)
counter = 0

for currentPkmn in pkmnJSON:
    
    pkmnRow.append(currentPkmn)
    counter += 1

    if counter == config.MAX_COLUMNS or int(currentPkmn["Nº"]) == len(pkmnJSON):
        pkmnMatrix.append(pkmnRow[:])
        counter = 0
        pkmnRow = []


while 1:
    
    for event in pygame.event.get():
        # Add listener to close the window
        if event.type == pygame.QUIT: sys.exit()

        # Add listener to move the cursor
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if cursorX < 280:
                cursorX += config.HORIZONTAL_SPACE
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if cursorX > 0:
                cursorX -= config.HORIZONTAL_SPACE
        if pygame.key.get_pressed()[pygame.K_UP]:
            if cursorY > 10:
                cursorY -= config.VERTICAL_SPACE
            elif firstRow > 0:
                firstRow -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if cursorY < 150:
                cursorY += config.VERTICAL_SPACE
            elif firstRow < len(pkmnMatrix) - 3:
                firstRow += 1

    # Add some color and title
    screen.fill(colors.WHITE)

    # Display the matrix
    currentVertical = config.INIT_VERTICAL
    maxRows = firstRow + config.MAX_ROWS
    for index in range(firstRow, maxRows):
        currentHorizontal = config.INIT_HORIZONTAL
        currentRow = pkmnMatrix[index]
        for currentPkmn in currentRow:
            imageToLoad = pygame.image.load(cfiles.PKMN_IMAGES_PATH + "/front-{}.png".format(currentPkmn["Nº"]))
            screen.blit(imageToLoad, (currentHorizontal, currentVertical))
            currentHorizontal += horizontalSpace
        currentVertical += verticalSpace

    # Add cursor
    pygame.draw.rect(screen, colors.BLACK, pygame.Rect(cursorX, cursorY, config.CURSOR_WIDTH, config.CURSOR_HEIGHT), 4)



    pygame.display.update()
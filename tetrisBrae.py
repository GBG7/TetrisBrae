"""

Name: Taha Sarfraz
Date: jan 15th
Author: lil solar (taha)
Program: tetris_brae
Desc: This program utilizes the Pygame library to create a functional Tetris game. The game includes a grid for the Tetrominoes to fall and stack on,
a next piece preview, and a system for clearing full rows.
The player can move and rotate the falling Tetromino using the arrow keys, and the game ends if a Tetromino is unable to fit onto the grid.
"""

import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - generate_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

#I - idea
pygame.font.init()
pygame.mixer.init()
window_width = 800
window_height = 700
play_area_width = 300 # meaning 300 // 10 = 30 width per block
play_area_height = 600 # meaning 600 // 20 = 20 height per block
block_dimension = 30

play_area_x_coord = (window_width - play_area_width) // 2
play_area_y_coord = window_height - play_area_height

#D - display
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')

#E - Entities
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

gameOver = pygame.mixer.Sound('tetrisgameover.mp3')
gameOver.set_volume(0.5)

rowClear = pygame.mixer.Sound('tetrisrowclear.mp3')
rowClear.set_volume(1)
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 237, 169), (174, 174, 196), (206, 2, 46), (177, 86, 216), (126, 220, 234), (221, 217, 218), (173, 20, 150)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3\



#def draw_score(text, size, color, surface):
    #blits display score to surface
#    global score
#    font = pygame.font.SysFont('comicsans', 30)
#    label = font.render('Score: {}'.format(score),1,(255,255,255))
#    sx = play_area_x_coord - label.get_width() - 100
#    sy = play_area_y_coord + play_area_height/2 - 100
#    surface.blit(label, (sx + 10, sy-30))

def clear_rows(game_grid, occupied_positions):
    # This function removes any completed rows from the game grid and shifts the rows above it down.
    # A completed row is a row where all the spaces are filled.
    #rowClear.play()
    global score
    score = 0
    num_of_rows_removed = 0
    # Iterate through the rows of the game grid starting from the bottom
    for row_index in range(len(game_grid)-1,-1,-1):
        current_row = game_grid[row_index]
        # Check if the current row is a completed row (i.e. all spaces are filled)
        if (0, 0, 0) not in current_row:
            num_of_rows_removed += 1
            # remove the positions of the completed row from the occupied_positions
            index_to_remove = row_index
            for column_index in range(len(current_row)):
                try:
                    del occupied_positions[(column_index, row_index)]
                except:
                    continue
    # Shift the rows above the completed row down by the number of rows removed
    if num_of_rows_removed > 0:
        rowClear.play()
        score+= 1
        print(score)
        for key in sorted(list(occupied_positions), key=lambda pos: pos[1])[::-1]:
            column, row = key
            if row < index_to_remove:
                new_key = (column, row + num_of_rows_removed)
                occupied_positions[new_key] = occupied_positions.pop(key)



def draw_grid(canvas, rows, columns):
    x_start = play_area_x_coord #  play_area_x_coord is defined elsewhere
    y_start = play_area_y_coord
    for i in range(rows):
        pygame.draw.line(canvas, (128,128,128), (x_start, y_start+ i*30), (x_start + play_area_width, y_start + i * 30))  # horizontal lines
        for j in range(columns):
            pygame.draw.line(canvas, (128,128,128), (x_start + j * 30, y_start), (x_start + j * 30, y_start + play_area_height))  # vertical lines

def check_lost(positions):
    """
    This function checks if the game is lost by checking if any block of the tetromino has reached the top of the grid.
    """
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False



def is_valid_space(tetromino, game_grid):
    """
    This function checks if the given tetromino has a valid space on the game grid.
    It checks if the positions of the tetromino are occupied by other blocks on the grid.
    """
    valid_positions = [[(x, y) for x in range(10) if game_grid[y][x] == (0,0,0)] for y in range(20)]
    # get a list of all valid positions on the grid (empty spaces)
    valid_positions = [pos for row in valid_positions for pos in row]
    formatted_tetromino = convert_shape_format(tetromino)

    for position in formatted_tetromino:
        if position not in valid_positions:
            if position[1] > -1:
                return False
    # if all positions are valid, return True
    return True
    return True


def draw_next_shape(tetromino, screen):
    """
    This function displays the next tetromino on the screen.
    """
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    x_start = play_area_x_coord + play_area_width + 50
    y_start = play_area_y_coord + play_area_height/2 - 100
    format = tetromino.shape[tetromino.rotation % len(tetromino.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(screen, tetromino.color, (x_start + j*30, y_start + i*30, 30, 30), 0)

    screen.blit(label, (x_start + 10, y_start- 30))



def draw_window(canvas):
    """
    This function renders the game window by filling the canvas with black color, displaying the title,
    rendering the game grid, drawing the grid and border, and updating the display.
    """
    canvas.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 50)
    label = font.render('TETRIS BRAE', 1, (255,255,255))

    canvas.blit(label, (play_area_x_coord + play_area_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(canvas, grid[i][j], (play_area_x_coord + j* 30, play_area_y_coord + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(canvas, 50, 10)
    pygame.draw.rect(canvas, (168,221,204), (play_area_x_coord, play_area_y_coord, play_area_width, play_area_height), 5)
    # canvas.blit(




def convert_shape_format(tetromino):
    """
    This function converts the shape format of the tetromino to a list of coordinates.
    """
    coordinates = []
    format = tetromino.shape[tetromino.rotation % len(tetromino.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                coordinates.append((tetromino.x + j, tetromino.y + i))

    for i, pos in enumerate(coordinates):
        coordinates[i] = (pos[0] - 2, pos[1] - 4)

    return coordinates



def get_piece():
    #gets shape lol
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))


def on_screen_text_mid(text, font_size, color, canvas):
    """
    This function renders the given text in the center of the canvas using the given font size and color
    """
    font = pygame.font.SysFont('comicsans', font_size, bold=True)
    label = font.render(text, 1, color)

    canvas.blit(label, (play_area_x_coord + play_area_width/2 - (label.get_width() / 2), play_area_y_coord + play_area_height/2 - label.get_height()/2))

def generate_grid(fixed_blocks={}):
    """
    This function creates a grid of 20x10 with all blocks initially set to black (0,0,0).
    It then updates the blocks in the grid with the color of the fixed blocks passed in the function.
    """
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col,row) in fixed_blocks:
                color = fixed_blocks[(col,row)]
                grid[row][col] = color
    return grid

#Action
def main():
    global grid
    # dictionary containing positions of locked in blocks
    # in the format of (x,y):(R,G,B)
    locked_blocks = {}
    grid = generate_grid(locked_blocks)
    change_piece = False
    game_run = True
    current_piece = get_piece()
    next_piece = get_piece()

    #Assign
    clock = pygame.time.Clock()
    fall_time = 0

    #Loop
    while game_run:

        fall_speed = 0.27

        grid = generate_grid(locked_blocks)
        fall_time += clock.get_rawtime()
        #Time
        clock.tick()

        # Piece falling code
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (is_valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        #Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.x += 1

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not is_valid_space(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not is_valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)


        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_blocks[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_piece()
            change_piece = False

            # call four times to check for multiple clear rows
            clear_rows(grid, locked_blocks)
            #rowClear.play()

        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if check_lost(locked_blocks):
            game_run = False
            pygame.mixer.music.set_volume(0)
            gameOver.play()


    on_screen_text_mid("You Lost", 40, (255,255,255), win)
    #Refresh screen
    pygame.display.update()
    pygame.time.delay(2000)


def main_menu():
    game_run = True
    while game_run:
        win.fill((0,0,0))
        on_screen_text_mid('Press a key to begin (no mouse click)', 40, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

            if event.type == pygame.KEYDOWN:
                main()

        pygame.mixer.music.load('tetrisundertale.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    pygame.quit()


#win = pygame.display.set_mode((window_width, window_height))
#pygame.display.set_caption('Tetris')

main_menu()  # start game

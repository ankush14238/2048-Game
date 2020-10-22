SIZE = 400 #size of the grid

GRID_LEN = 4 #grid length(4x4)

GRID_PADDING = 10 #padding between each cell in the grid

BACKGROUND_COLOR_GAME = "#92877d" #background color of the game

BACKGROUND_COLOR_CELL_EMPTY = "#9e948a" #background color of the cell when it is empty



#dictionary for background color of cells with the values. Here values are the number in the cell and keys are hexcodes for corresponding color

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",

                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", }


#dictionary for color of the text of the number present in the cell

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2",

                   4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                   32768: "#776e65", 65536: "#f9f6f2", }


#initialising font size and font type
FONT = ("Verdana", 40, "bold")



#initialising the keys for movement

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
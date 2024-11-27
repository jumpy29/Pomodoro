# Define color variables (blue, pink, etc.)
PRIMARY_BLUE = '#ECECEB'
SECONDARY_BLUE = '#189AB4'
STAT_COLOR_BLUE = '#189AB4'

PRIMARY_PINK = '#fae1dd'
SECONDARY_PINK = '#495057'
STAT_COLOR_PINK = '#F79489'

PRIMARY_PURPLE = '#C3C7DF'
SECONDARY_PURPLE = '#695E93'
STAT_COLOR_PURPLE = '#8155BA'

PRIMARY_RED = '#E43D40'
SECONDARY_RED = '#FABEC0'
STAT_COLOR_RED = '#F85C70'

PRIMARY_WOOD = '#E9DAC4'
SECONDARY_WOOD = '#875F59'
STAT_COLOR_WOOD = '#1C0803'

# Define global variables to store active colors
PRIMARY = PRIMARY_BLUE
SECONDARY = SECONDARY_BLUE
STAT_COLOR = STAT_COLOR_BLUE

# Functions to change color theme
def change_to_blue():
    global PRIMARY, SECONDARY, STAT_COLOR
    PRIMARY = PRIMARY_BLUE
    SECONDARY = SECONDARY_BLUE
    STAT_COLOR = STAT_COLOR_BLUE

def change_to_pink():
    global PRIMARY, SECONDARY, STAT_COLOR
    PRIMARY = PRIMARY_PINK
    SECONDARY = SECONDARY_PINK
    STAT_COLOR = STAT_COLOR_PINK

def change_to_purple():
    global PRIMARY, SECONDARY, STAT_COLOR
    PRIMARY = PRIMARY_PURPLE
    SECONDARY = SECONDARY_PURPLE
    STAT_COLOR = STAT_COLOR_PURPLE

def change_to_red():
    global PRIMARY, SECONDARY, STAT_COLOR
    PRIMARY = PRIMARY_RED
    SECONDARY = SECONDARY_RED
    STAT_COLOR = STAT_COLOR_RED

def change_to_wood():
    global PRIMARY, SECONDARY, STAT_COLOR
    PRIMARY = PRIMARY_WOOD
    SECONDARY = SECONDARY_WOOD
    STAT_COLOR = STAT_COLOR_WOOD
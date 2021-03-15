import os

# Colors
BLACK = (0,0,0)
WHITE = (235,235,235)
GRAY = (100,100,100)
RED = (180,32,42)
GOLD = (255,215,0)
PURPLE = (219,84,180)

# Window Resolution and Metadata
WIN_RES = {"w": 640, "h": 780}
TITLE = "Star Fighter"
AUTHOR = "zyenapz"
VERSION = "2.0"
SCALE = 4

# Directories
GAME_DIR = os.path.dirname("..") # What the fuck?
DATA_DIR = os.path.join(GAME_DIR, "data")
FONT_DIR = os.path.join(DATA_DIR, "font")
IMG_DIR = os.path.join(DATA_DIR, "img")
SCRIPTS_DIR = os.path.join(DATA_DIR, "scripts")
SFX_DIR = os.path.join(DATA_DIR, "sfx")
GAME_FONT = os.path.join(FONT_DIR, "04B_03__.TTF")
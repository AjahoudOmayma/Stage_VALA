import pygame
import neat  # For NEAT algorithm to train the bird's AI
import time
import os
import random

# Set window dimensions
WIN_WIDTH = 600
WIN_HEIGHT = 800

# Load and scale images for the bird animation frames
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]

# Load and scale the pipe, base, and background images
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

# Define the Bird class
class Bird:
    # Class-level constants for animation and rotation behavior
    IMGS = BIRD_IMGS           # The three bird animation images
    MAX_ROTATION = 25          # Maximum upward rotation angle
    ROT_VEL = 20               # Rotation velocity (degrees per frame)
    ANIMATION_TIME = 5         # Time before switching to the next animation frame

    def __init__(self, x, y):
        self.x = x                     # Bird's horizontal position
        self.y = y                     # Bird's vertical position
        self.tilt = 0                  # Current rotation angle (0 = no tilt)
        self.tick_count = 0           # Counter for how many frames since the last jump
        self.vel = 0                  # Bird's current vertical velocity
        self.height = self.y          # Bird's height when the last jump happened
        self.img_count = 0            # Counter to track which image to show in the animation
        self.img = self.IMGS[0]       # Start with the first image as the bird's sprite
    
    def jump(self):
        self.vel = -10.5           # Set an upward velocity (negative = up on screen)
        self.tick_count = 0        # Reset the tick counter (used to calculate movement since jump)
        self.height = self.y       # Record the height at the moment of the jump



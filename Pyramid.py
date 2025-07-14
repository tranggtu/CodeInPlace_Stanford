"""
File: pyramid.py
Draws a pyramid consisting of bricks arranged in horizontal rows.
The number of bricks in each row decreases by one as we move up the pyramid.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    start_x = int((CANVAS_WIDTH - BRICK_WIDTH * BRICKS_IN_BASE)/2)
    start_y = int(CANVAS_HEIGHT - BRICK_HEIGHT)

    for k in range(BRICKS_IN_BASE, 0, -1):
        x,y = start_x, start_y
        for i in range(k):
            draw_bricks(canvas, x, y)
            x = x + BRICK_WIDTH

        start_x = start_x + int(BRICK_WIDTH /2)
        start_y = start_y - BRICK_HEIGHT


def draw_bricks(canvas, start_x, start_y):
    end_x = start_x + BRICK_WIDTH
    end_y = start_y + BRICK_HEIGHT
    # Draw bricks at frame (start_x, start_y)
    canvas.create_rectangle(
        start_x, start_y,
        end_x, end_y, 
        "yellow", "black"
    )
    

if __name__ == '__main__':
    main()
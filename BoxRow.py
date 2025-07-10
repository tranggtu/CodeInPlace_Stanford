"""
File: boxrow.py
Make a line of boxes such that boxes fill the bottom of the canvas.
Each box should have a width and height of BOX_SIZE
"""
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw 5 boxes in line with one another
    # boxes fill the bottom of the canvas

    for i in range(N_BOXES):
        left_x = int(i * BOX_SIZE)
        top_y = int(CANVAS_HEIGHT - BOX_SIZE)
        right_x = int(BOX_SIZE * (i+1))
        bottom_y = CANVAS_HEIGHT
        canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "white",
            "black"
        )

if __name__ == '__main__':
    main()
    
"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width/2-ball_radius),
                          y=(self.window.height/2-ball_radius))
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.click)
        onmousemoved(self.move)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                if j <= 1:
                    brick.color = 'red'
                    brick.fill_color = 'red'
                if 1 < j <= 3:
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                if 3 < j <= 5:
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                if 5 < j <= 7:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                if j > 7:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                self.window.add(brick, x=i*(BRICK_WIDTH+BRICK_SPACING), y=BRICK_OFFSET+j*(BRICK_HEIGHT+BRICK_SPACING))

        self.num_brick = brick_cols * brick_rows

    def move(self, mouse):
        if mouse.x+self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x

    def click(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = - self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_velocity(self):
        self.__dx = 0
        self.__dy = 0

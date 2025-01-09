"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = 0
    dy = 0
    num_lives = NUM_LIVES
    num_brick = graphics.num_brick

    # Add the animation loop here!
    while True:
        # End-game condition
        if num_lives <= 0:
            break
        if num_brick <= 0:
            break

        # Get new velocity and move
        if dx == 0 and dy == 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        graphics.ball.move(dx, dy)

        # Change direction when ball hit walls or ceiling
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy

        # When ball hits the ground
        if graphics.ball.y >= graphics.window.height - graphics.ball.height:
            graphics.ball.move((graphics.window.width-graphics.ball.width)/2 - graphics.ball.x,
                               (graphics.window.height-graphics.ball.height)/2 - graphics.ball.y)
            num_lives -= 1
            dx = 0
            dy = 0
            graphics.reset_velocity()

        # Objects at 4 vertexes of the ball
        object_00 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        object_20 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        object_02 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        object_22 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y +
                                                  graphics.ball.height)

        # Ball's information(x, y, width, height)
        ball_x = graphics.ball.x
        ball_y = graphics.ball.y
        ball_w = graphics.ball.width
        ball_h = graphics.ball.height

        # Bounce and break
        if object_00 is not None:
            if dx > 0 and dy < 0:
                dy = -dy
            if dx < 0 and dy > 0:
                dx = -dx
            if dx < 0 and dy < 0:
                if graphics.window.get_object_at(ball_x + 1, ball_y) is None:
                    dx = -dx
                else:
                    # dx = -dx
                    dy = -dy
            if object_00 is not graphics.paddle:
                graphics.window.remove(object_00)
                num_brick -= 1

        elif object_20 is not None:
            if dx < 0 and dy < 0:
                dy = -dy
            if dx > 0 and dy > 0:
                dx = -dx
            if dx > 0 and dy < 0:
                if graphics.window.get_object_at(ball_x + ball_w - 1, ball_y) is None:
                    dx = -dx
                else:
                    # dx = -dx
                    dy = -dy
            if object_20 is not graphics.paddle:
                graphics.window.remove(object_20)
                num_brick -= 1

        elif object_02 is not None:
            if dx > 0 and dy > 0:
                dy = -dy
            if dx < 0 and dy < 0:
                dx = -dx
            if dx < 0 and dy > 0:
                if graphics.window.get_object_at(ball_x + 1, ball_y + ball_h) is None:
                    dx = -dx
                else:
                    # dx = -dx
                    dy = -dy
            if object_02 is not graphics.paddle:
                graphics.window.remove(object_02)
                num_brick -= 1

        elif object_22 is not None:
            if dx < 0 and dy > 0:
                dy = -dy
            if dx > 0 and dy < 0:
                dx = -dx
            if dx > 0 and dy > 0:
                if graphics.window.get_object_at(ball_x + ball_w - 1, ball_y + ball_h) is None:
                    dx = -dx
                else:
                    dy = -dy
            if object_22 is not graphics.paddle:
                graphics.window.remove(object_22)
                num_brick -= 1
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

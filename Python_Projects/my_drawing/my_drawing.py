"""
File: my_drawing.py
Name: JP WU
----------------------
Break down the desired drawing into different components, where each component is an object created using the
GObject class.

Finally, add all components to the window in top-to-bottom order.
"""

from campy.graphics.gobjects import GRect, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: I like salmon sashimi

    I REALLY like salmon sashimi!
    """
    window = GWindow(width=500, height=475, title='I like salmon sashimi')

    bg = GRect(500, 475)
    bg.filled = True
    bg.fill_color = 'white'
    window.add(bg)

    chopstick_back = GPolygon()                              # Chopstick behind the salmon sashimi
    chopstick_back.add_vertex((200, 250))
    chopstick_back.add_vertex((500, 100))
    chopstick_back.add_vertex((510, 115))
    chopstick_back.add_vertex((210, 265))
    chopstick_back.filled = True
    window.add(chopstick_back)

    salmon_top = GArc(950, 850, 0, 95)                       # Salmon sashimi's top oil(fat)
    salmon_top.filled = True
    salmon_top.fill_color = 'antiquewhite'
    salmon_top.color = 'antiquewhite'
    salmon_top.move(-125, 187)
    window.add(salmon_top)

    salmon = GArc(850, 800, 0, 95)                           # Salmon sashimi's meat
    salmon.filled = True
    salmon.fill_color = 'coral'
    salmon.color = 'coral'
    salmon.move(-100, 200)
    window.add(salmon)

    oil1 = GPolygon()                                        # oil(fat) texture 1
    oil1.add_vertex((125, 305))
    oil1.add_vertex((150, 190))
    oil1.add_vertex((160, 195))
    oil1.add_vertex((135, 310))
    oil1.filled = True
    oil1.fill_color = 'antiquewhite'
    oil1.color = 'antiquewhite'
    window.add(oil1)

    oil2 = GPolygon()                                        # oil(fat) texture 2
    oil2.add_vertex((155, 330))
    oil2.add_vertex((230, 210))
    oil2.add_vertex((239, 217))
    oil2.add_vertex((164, 337))
    oil2.filled = True
    oil2.fill_color = 'antiquewhite'
    oil2.color = 'antiquewhite'
    window.add(oil2)

    oil3 = GPolygon()                                        # oil(fat) texture 3
    oil3.add_vertex((185, 360))
    oil3.add_vertex((320, 255))
    oil3.add_vertex((327, 264))
    oil3.add_vertex((192, 369))
    oil3.filled = True
    oil3.fill_color = 'antiquewhite'
    oil3.color = 'antiquewhite'
    window.add(oil3)

    oil4 = GPolygon()                                        # oil(fat) texture 4
    oil4.add_vertex((220, 385))
    oil4.add_vertex((375, 360))
    oil4.add_vertex((380, 370))
    oil4.add_vertex((225, 395))
    oil4.filled = True
    oil4.fill_color = 'antiquewhite'
    oil4.color = 'antiquewhite'
    window.add(oil4)

    salmon_bottom = GArc(600, 600, 0, 100)                   # To create an arc shape beneath salmon sashimi
    salmon_bottom.filled = True
    salmon_bottom.fill_color = 'white'
    salmon_bottom.color = 'white'
    salmon_bottom.move(-100, 300)
    window.add(salmon_bottom)

    chopstick_front = GPolygon()                             # Chopstick in front of the salmon sashimi
    chopstick_front.add_vertex((220, 275))
    chopstick_front.add_vertex((520, 125))
    chopstick_front.add_vertex((530, 140))
    chopstick_front.add_vertex((230, 290))
    chopstick_front.filled = True
    window.add(chopstick_front)

    title = GLabel('サーモン', x=10, y=90)                    # The Japanese term for salmon sashimi
    title.font = '-60'
    window.add(title)


if __name__ == '__main__':
    main()

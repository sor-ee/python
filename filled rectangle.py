import pgzrun
def draw():
    screen.clear()
    screen.draw.filled_rect(Rect((0,0),(200,150)),(255,255,255))
    screen.draw.filled_rect(Rect((200,0),(200,150)),(0,255,0))
    screen.draw.filled_rect(Rect((0,150),(200,150)),(0,255,0))
    screen.draw.filled_rect(Rect((200,150),(200,150)),(255,255,255))
    Colors = ('orange','cyan','pink')
    for n in range(3):
        BOX = Rect((120+(n*20),100+(n*20)),(100,100))
        screen.draw.filled_rect(BOX , Colors[n])
WIDTH = 400
HEIGHT = 300
pgzrun.go()

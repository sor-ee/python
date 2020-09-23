import pgzrun
def draw():
    screen.clear()
    for n in range(1,11):
        screen.draw.line((10,10),(250,30*n),(255,255,0))
    for n in range(1,6):
        screen.draw.line((400,300),(100,50*n),'cyan')
WIDTH = 400
HEIGHT = 300
pgzrun.go()

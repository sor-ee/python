import pgzrun
def draw():
    screen.fill(BGColor)
    screen.draw.text("Show all Graphics 2d",(200,10), fontsize=30,color='blue')
    screen.draw.line((0,0),(WIDTH,HEIGHT),'red')

    screen.draw.filled_rect(Rect((400,100),(200,100)),'yellow')
    screen.draw.rect(Rect((400,100),(200,100)),(255,0,0))
    screen.draw.filled_circle((200,350),100,'yellow')
    screen.draw.circle((200,350),100,(255,0,0))
    showTriangle('orange')

def showTriangle(color):
    screen.draw.line((20,100),(20,200),color)
    screen.draw.line((20,200),(120,200),color)
    screen.draw.line((120,200),(20,100),color)
WIDTH = 640
HEIGHT = 480
BGColor = (255,255,255)
pgzrun.go()

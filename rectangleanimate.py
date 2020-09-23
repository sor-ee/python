import pgzrun

def update():
    global y1,y2
    y1 = y1+1
    if y1 > HEIGHT:
        y1 = 0
    y2 = y2-1
    if y2 < 0:
        y2 = HEIGHT
        
def draw():
    screen.fill(BGColor)
    screen.draw.text("Show Text Animate",(250,10),fontsize=28,color='blue')
    screen.draw.rect(Rect((50,y1),(50,50)),color = 'red')
    screen.draw.filled_rect(Rect((350,y2),(50,50)),color = 'green')

WIDTH = 640
HEIGHT = 480
BGColor = (255,255,255)
y1 = int(HEIGHT)/2
y2 = int(HEIGHT)/2

pgzrun.go()

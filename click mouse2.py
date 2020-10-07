import pgzrun

def draw():
    screen.fill('white')
    screen.draw.text('show press and released mouse',(200,10),color='blue')
    apple1.draw()
    apple2.draw()

def on_mouse_down(pos,button):
    global x1,y1,x2,y2
    if button == mouse.LEFT:
        (x1,y1) = pos
    elif button == mouse.RIGHT:
        (x2,y2) = pos

def on_mouse_up(pos,button):
    if button == mouse.LEFT:
        apple1.pos = pos
    elif button == mouse.RIGHT:
        apple2.pos = pos

def update():
    #update position apple1
    if apple1.x < x1:
        apple1.x +=1
    elif apple1.x > x1:
        apple1.x -=1
    if apple1.y < y1:
        apple1.y +=1
    elif apple1.y > y1:
        apple1.y -=1

    #update position apple2
    if apple2.x < x2:
        apple2.x +=1
    elif apple2.x > x2:
        apple2.x -=1
    if apple2.y < y2:
        apple2.y +=1
    elif apple2.y > y2:
        apple2.y -=1

#Main Program
WIDTH = 640
HEIGHT = 480
apple1 = Actor('apple',(WIDTH/2,HEIGHT/2))
apple2 = Actor('apple',(WIDTH/2,HEIGHT/2))
x1 = y1 = 0
x2 = WIDTH
y2 = HEIGHT
pgzrun.go()

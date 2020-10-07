import pgzrun

def draw():
    screen.fill('white')
    screen.draw.text('show press and released mouse',(200,10),color='blue')
    apple1.draw()
    apple2.draw()

def on_mouse_down(pos,button):
    apple1.pos = pos

def on_mouse_up(pos,button):
    apple2.pos = pos

WIDTH = 640
HEIGHT = 480
apple1 = Actor('apple')
apple2 = Actor('apple')
apple1.pos = (WIDTH/2,HEIGHT/2)
apple2.pos = (WIDTH/2,HEIGHT/2)
pgzrun.go()

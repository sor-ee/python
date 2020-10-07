import pgzrun
def draw():
    screen.fill('white')
    screen.draw.text("Show Animate start(P) and Stop(S)",(200,10),color='blue')
    apple.draw()
def update():
    if Play:
        apple.x += 19
        if (apple.x > WIDTH):
            apple.x = 0
def on_key_down(key,mod,unicode):
    global Play
    if (key == key.P):
        Play = True
    elif (key ==key.S):
        Play = False
def on_key_up(key,mod):
    pass
WIDTH = 640
HEIGHT = 480
apple = Actor('apple',(WIDTH/2,HEIGHT/2))
Play = False
pgzrun.go()

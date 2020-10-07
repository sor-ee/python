import pgzrun
def draw():
    screen.fill('white')
    screen.draw.text('use variable keyboard in update',(200,10),color='blue')
    apple.draw()
def update():
    if (keyboard.LEFT):
        apple.x -= 10
    elif (keyboard.RIGHT):
        apple.x += 10
    if (keyboard.UP):
        apple.y -= 10
    elif (keyboard.DOWN):
        apple.y += 10
def on_key_down(key,mod,unicode):
    pass
def on_key_up(key,mod):
    pass
WIDTH = 640
HEIGHT = 480
apple = Actor('apple',(WIDTH/2,HEIGHT/2))
pgzrun.go()

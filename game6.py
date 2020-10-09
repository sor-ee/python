import pgzrun
def draw():
    screen.fill(bgcolor)
    screen.draw.text('use variable keyboard in update',(200,20),color='blue')
    apple.draw()
    if live_bullet:
        bullet.draw()
    if live_monster:
        monster.draw()
def update():
    global live_bullet
    if (keyboard.LEFT):
        apple.x -= 10
    elif (keyboard.RIGHT):
        apple.x += 10
    if apple.x < apple.width/2:
        apple.x = apple.width/2
    elif apple.x > WIDTH - apple.width/2:
        apple.x = WIDTH - apple.width/2
    if apple.y < apple.height/2:
        apple.y = apple.height/2
    elif apple.y > HEIGHT - apple.height/2:
        apple.y = HEIGHT - apple.height/2
    if (keyboard.UP):
        apple.y -= 10
    elif (keyboard.DOWN):
        apple.y += 10
    #check bullet and move
    if (live_bullet):
        bullet.y -=10

        if bullet.y < 0:
            live_bullet = False
        left = monster.x - monster.width/2
        right = monster.x + monster.width/2

        if bullet.x >= left and bullet.x <= right:
            top = monster.y - monster.height/2
            bottom = monster.y + monster.height/2

            if bullet.y >= top and bullet.y <= bottom:
                live_bullet = False
                live_monster = False
                monster.pos = (-50,-50)
                sounds.bird.play()
def on_key_down(key,mod,unicode):
    global bgcolor,live_bullet
    if key == keys.R:
        bgcolor = (255,0,0)
    elif key == keys.B:
        bgcolor = (0,0,0)
    elif key == keys.G:
        bgcolor = (0,255,0)
    elif key == keys.W:
        bgcolor = (255,255,255)
    if key == keys.SPACE and live_bullet == False:
        live_bullet = True
        bullet.pos = apple.pos
def on_key_up(key,mod):
    pass
WIDTH = 640 
HEIGHT = 480
apple = Actor('apple',(WIDTH/2,HEIGHT/2))
bullet = Actor('pic',(-50,-50))
live_bullet = False
monster = Actor('apple',(WIDTH/2,40))
live_monster = True
bgcolor = (255,255,255)
pgzrun.go()

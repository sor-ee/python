import pgzrun

def draw():
    #bg.draw()
    screen.blit('df',(0,0))
    #screen.fill('white')
    screen.draw.text('Change Position and Display',topleft=(150,80),color='blue')
    screen.draw.text('Rotation Angle : '+str(apple.angle),(50,200),color='blue') 
    logo.draw()
    apple.draw()
    apple1.draw()

def update():
    if (logo.x < WIDTH):
        logo.x +=1
    if (logo.y < HEIGHT):
        logo.y +=1
    apple.angle +=1
    if (apple.angle == 360):
        apple.angle = 0

WIDTH = 400
HEIGHT = 300
logo = Actor('it_logo',(0,0))
apple = Actor('apple')
apple1 = Actor('apple')
df = Actor('df')
apple.pos = (WIDTH/2,HEIGHT/2)
apple.anchor = (apple.width,apple.height)
apple1.angle = -90
pgzrun.go()

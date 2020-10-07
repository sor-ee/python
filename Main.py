import pgzrun

def draw():
    screen.fill('white')
    logo.draw()
    screen.draw.text('load and Display Image',(150,270),fontsize=28,color='red')
    screen.draw.text('Image width : %d' %logo.width,(250,150),fontsize=24,color='blue')
    screen.draw.text('Image height : %d' %logo.height,(250,200),fontsize=24,color='blue')

#main Program
WIDTH = 400
HEIGHT = 300
logo = Actor('it_logo')
pgzrun.go()

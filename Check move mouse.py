import pgzrun

def draw():
          screen.fill('white')
          screen.draw.text('Show move mouse to move image',(200,10),color ='blue')
          apple.draw()

def on_mouse_move(pos,rel,buttons):
          print(rel)
          apple.pos = pos
          if mouse.LEFT in buttons:
                    print('Left')
#Main program
WIDTH =640
HEIGHT =480
apple = Actor('apple',(WIDTH/2,HEIGHT/2))
pgzrun.go()

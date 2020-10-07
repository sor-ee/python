import pgzrun
import random

def draw():
                
                screen.clear();
                screen.fill("White");
                screen.draw.text(IP1,topleft=(10,y1),fontsize=30,color=('Pink'))
                screen.draw.text(IP2,topleft=(200,y2),fontsize=30,color=('Pink'))
                screen.draw.text(IP3,topleft=(400,y3),fontsize=30,color=('Pink'))
                screen.draw.text(IP4,topleft=(600,y4),fontsize=30,color=('Pink'))
                screen.draw.text(IP5,topleft=(820,y5),fontsize=30,color=('Pink'))
def update():
                global y1,y2,y3,y4,y5
                y1 = y1 + random.randint(1,4)
                if y1 >HEIGHT:
                                y1 = 0
                y2 = y2 + random.randint(1,4)
                if y2 >HEIGHT:
                                y2 = 0
                y3 = y3 + random.randint(1,4)
                if y3 >HEIGHT:
                                y3 = 0
                y4 = y4 + random.randint(1,4)
                if y4 >HEIGHT:
                                y4 = 0
                y5 = y5 + random.randint(1,4)
                if y5 >HEIGHT:
                                y5 = 0


WIDTH= 900
HEIGHT = 800
IP1 = input("Enter text 1 : ")
IP2 = input("Enter text 2 : ")
IP3 = input("Enter text 3 : ")
IP4 = input("Enter text 4 : ")
IP5 = input("Enter text 5 : ")
y1 = int(HEIGHT)
y2 = int(HEIGHT)
y3 = int(HEIGHT)
y4 = int(HEIGHT)
y5 = int(HEIGHT)
pgzrun.go()

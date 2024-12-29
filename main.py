import pixels
from pixels import *
import animations
#import connect4


print("\nWelcome to da blinkenlights 2 ")

#animations.welcome()

#for i in range(7):
#   for j in range(7):
#        pixels.onXY(i,j,pixels.randTupel())
x = 0
y = 0
c = 0
#while True:
while y < 8:
    while x < 8:
        onXY(x,y,animations.colorSpectrum(c,10))
        x = x + 1
        c = (c + 0.01)%1
        wait(0.1)
    y = y + 1
    x =0
   # y=0
def reihe(reihe,color):
    l=[(i,j) for i in range(8) for j in range(8) if i + j==reihe and j<9 and i<9]
    for led in l:
        pixels.setXY(led[0],led[1],color)
    pixels.show()


for x in range(15):
    reihe(x,animations.colorSpectrum((x*0.11)%1,10))
    wait(1)

#connect4.Game(2)

#def f(x,y,f):
#    if x %2 is 0:
#        if y %2 is 0:
#            return (0,f%15,0)
#    return (f%15,0,0)
#
#def f2(x,y,f):
#    if f%3 is 0:
#        return (10,0,0)
#    return (0,0,0)
#
#animCallback(f2, 60)


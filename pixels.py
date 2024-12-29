import machine, neopixel, time, random
import json

PIN=4
WIDTH=8
HEIGHT=WIDTH

NBR_PIX=WIDTH*HEIGHT
np = neopixel.NeoPixel(machine.Pin(PIN), NBR_PIX)

RED = (10,0,0)
GREEN = (0,10,0)
BLUE = (0,0,10)
YELLOW = (10,10,0)
CYAN = (0,10,10)
MAGENTA = (10,0,10)
WHITE = (10,10,10)
BLACK = (0,0,0)

primCol = CYAN 

def animCallback(cb, fps=5, frameNumber=-1):
    curFrame=0
    while curFrame is not frameNumber:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                c = cb(x,y,curFrame)
                if c is not None:
                    setXY(x,y,c)
        curFrame = curFrame+1
        show()
        wait(1/fps)

def forAll(cb):
    for i in range(np.n):
        cb(i)

def setI(i, c):
    np[i] = c

def unsetI(i):
    np[i] = (0,0,0)

def getIFrom(x,y):
    x %= WIDTH 
    y %= HEIGHT
    if y%2 == 0:
        return WIDTH-1-x + y*WIDTH
    else: 
        return x + y*WIDTH

def setXY(x,y,c):
    i = getIFrom(x,y)
    setI(i,c)

def unsetXY(x,y):
    i = getIFrom(x,y)
    setI(i,BLACK)

def onXY(x,y,c=primCol):
    i = getIFrom(x,y)
    setI(i, c)
    show()

def offXY(x,y):
    i = getIFrom(x,y)
    unset(i)
    show()

def clear():
    np.fill((0,0,0))
    show()

def randVal(a,b):
    return int(random.getrandbits(32))%(b-a) + a

def randTupel(a,b):
    return randVal(a,b),randVal(a,b),randVal(a,b)

def brightnessUpdate(f):
    for i in range(len(np.buf)):
        if(np.buf[i]):
            np.buf[i] = int(np.buf[i]*f)

def darken(f=1.1):
    brightnessUpdate(1/f)

def lighten(f=1.1):
    brightnessUpdate(f)

def shiftBuffer(i):
    i = i%np.n
    corLen = np.n*3
    amount = i*3
    lastBytes = np.buf[corLen-amount:corLen]
    np.buf[amount:corLen] = np.buf[0:corLen-amount]
    np.buf[0:amount] = lastBytes

def show():
    np.write()

def wait(secs):
    time.sleep_ms(int(secs*1000))




from pixels import * 

def runnerXY():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            darken()
            onXY(x,y)
            show()

def quads(sleep = .2):
    for s in range(WIDTH/2):
        c = randTupel(1,10)
        for x in range(s, WIDTH-s):

            setXY(x,s,c)
            setXY(WIDTH-1-x,WIDTH-1-s,c)

            setXY(s,x,c)
            setXY(WIDTH-1-s,WIDTH-1-x,c)

            wait(sleep)
            show()

def offquads(sleep = .2):
    for s in range(WIDTH/2):
        c = BLACK
        for x in range(s, WIDTH-s):

            setXY(x,s,c)
            setXY(WIDTH-1-x,WIDTH-1-s,c)

            setXY(s,x,c)
            setXY(WIDTH-1-s,WIDTH-1-x,c)

            wait(sleep)
            show()

def _fillNShow(c):
    np.fill(c)
    show()

def colorShift(maxCv=20):
    r = maxCv
    g = 0
    b = 0
    for g in range(maxCv):
        _fillNShow((r,g,b))
    for r in range(maxCv-1,0,-1):
        _fillNShow((r,g,b))
    for b in range(maxCv):
        _fillNShow((r,g,b))
    for g in range(maxCv-1,0,-1):
        _fillNShow((r,g,b))
    for r in range(maxCv):
        _fillNShow((r,g,b))
    for b in range(maxCv-1,0,-1):
        _fillNShow((r,g,b))

def _applyDirection(pos, direction):
    direction %= 4
    if direction == 0: 
        pos[0] += 1
    if direction == 1: 
        pos[1] += 1
    if direction == 2: 
        pos[0] -= 1
    if direction == 3: 
        pos[1] -= 1
    return pos

def drawBorder(color = RED):
    for i in range(WIDTH):
        setXY(i,0, color)
        setXY(i,HEIGHT-1, color)
        setXY(0,i, color)
        setXY(WIDTH-1,i, color)

def _applyDirection(pos, direction):
    direction %= 4
    x, y = pos
    if direction == 0: 
        x += 1
    if direction == 1: 
        y += 1
    if direction == 2: 
        x -= 1
    if direction == 3: 
        y -= 1
    return x,y

def snakes(number=5, sleepV=.05, darkenV=1.1, keepAlive=3, border=True):
    if border:
        drawBorder()

    pos = [[randVal(1,WIDTH-2),randVal(1,HEIGHT-1)] for i in range(number)]
    direction = [randVal(0,4) for i in range(number)]
    color = [randTupel(3,12) for i in range(number)]
    alive = [True for i in range(number)]
    keepAliveForRounds = keepAlive

    while True: 
        aliveCount = 0
        for e in alive:
            if e:
                aliveCount += 1
        if aliveCount <= 1: 
            keepAliveForRounds -= 1

        if keepAliveForRounds == 0: 
            break

        
        for i in range(randVal(1,8)):
            for r in range(number):
                nextPos = _applyDirection(pos[r],direction[r])
                nextPosColor = np[getIFrom(nextPos[0],nextPos[1])]

                tries = 3
                while nextPosColor[0] != 0 or nextPosColor[1] != 0 or nextPosColor[2] != 0:
                    if tries <= 0:
                        alive[r] = False
                        break

                    # use different strategy in 50% (left or right)
                    if(r%2==0):
                        direction[r] -= tries
                    else:
                        direction[r] += tries

                    nextPos = _applyDirection(pos[r],direction[r])
                    nextPosColor = np[getIFrom(nextPos[0],nextPos[1])]
                    tries -= 1

                if(alive[r]):
                    setXY(nextPos[0], nextPos[1], color[r])
                pos[r] = nextPos

            darken(darkenV)
            show()
            if border:
                drawBorder()
            wait(sleepV)

        for r in range(number):
            newDirection = randVal(0,4)
            if direction[r]%2 != newDirection%2: 
                direction[r] = newDirection

def welcome():
    while True:
        drawHi()
        wait(2)
        drawSmile()
        wait(3)
        colorRange(repeat=200, sleepV=.02)
        wait(1)
        quads()
        for i in range(10):
            snakes(4)
        wait(3)

def drawHi(color=RED):
    smile_matrix = [
        [0,0,0,0,0,0,0,0],
        [0,1,0,0,1,0,0,0],
        [0,1,0,0,1,0,1,0],
        [0,1,0,0,1,0,0,0],
        [0,1,1,1,1,0,1,0],
        [0,1,0,0,1,0,1,0],
        [0,1,0,0,1,0,1,0],
        [0,0,0,0,0,0,0,0],
    ]
    clear()

    for y in range(len(smile_matrix)):
        for x in range(len(smile_matrix[y])):
            if smile_matrix[y][x] == 1:
                setXY(x,y,color)
    show()


def drawSmile(color=RED):
    smile_matrix = [
        [0,0,0,0,0,0,0,0],
        [0,1,1,0,0,1,1,0],
        [0,1,1,0,0,1,1,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,1,1,0,0,0],
        [0,1,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0],
    ]
    clear()

    for y in range(len(smile_matrix)):
        for x in range(len(smile_matrix[y])):
            if smile_matrix[y][x] == 1:
                setXY(x,y,color)
    show()


def rainBow(maxV=30, fps=5, spread=1):
    animCallback(lambda x,y,frame: rainBowRows(x,y,frame,maxV=maxV,spread=spread), fps)

def rainBowRows(x,y,frame,maxV=30,spread=1):
    rowStep = 1/(spread*HEIGHT)
    rgb=colorSpectrum((y+frame)*rowStep, maxV)
    return rgb


def colorSpectrum(r=0, maxV=50):
    # the rgb values can go from 0 to maxV
    # the alg will start from (0,0,maxV)
    # it will then add the value by first going up to (maxV,0,maxV)
    # after that it will reduce the r value to (maxV,0,0)
    # after that to (maxV,maxV,0)
    # so for each color which is currently going up we have maxV*2 values
    # since we have 3 colors the overall valueRange is maxV*2*3
    result = [0,0,0]
    if r==0:
        return (0,0,maxV)
    valueRange = maxV*2*3
    appliedR = int(valueRange*r)

    currentUpGoingColorIndex = (appliedR // (valueRange//3)%3)
    appliedR = appliedR % (valueRange//3)
    #setting current color up
    if(appliedR < maxV):
        result[currentUpGoingColorIndex] = appliedR
        result[(currentUpGoingColorIndex+2)%3] = maxV
    else: 
        result[currentUpGoingColorIndex] = maxV
        result[(currentUpGoingColorIndex+2)%3] = maxV-(appliedR-maxV)
    
    return (result[0], result[1], result[2])

def colorRange(repeat=-1, sleepV=0.1):
    for i in range(NBR_PIX):
        c = colorSpectrum(maxV=5, r=(1/NBR_PIX)*i)
        setI(i,c)
    show()
    count=0
    while count<repeat:
        shiftBuffer(1)
        show()
        wait(sleepV)
        if repeat>0:
            count=count+1











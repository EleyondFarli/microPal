def turnOnCol():
    global aux
    aux = col[currCol]
    while aux <= 5:
        led.plot(currCol, aux)
        aux = aux + 1
def startClass():
    global gameIsOn, totalTime, menu
    gameIsOn = 1
    basic.clear_screen()
    basic.show_string("Start")
    for index in range(5):
        randomTime()
        basic.pause(generatedTime)
        playGame()
        totalTime = totalTime - generatedTime
    basic.pause(totalTime)
    basic.show_string("Gata ora!!")
    basic.show_string("Exporta codul!")
    menu = 0

def on_button_pressed_a():
    global lastAnswer, currVal, currentState
    lastAnswer = -1
    if setCode == 1:
        if currVal == 0:
            basic.clear_screen()
            currVal = 5
        else:
            currVal = currVal - 1
        col[currCol] = currVal
        turnOnCol()
    elif menu == 0 or menu == 1:
        if currentState == 0:
            currentState = 3
        else:
            currentState = currentState - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def turnOnDimCol():
    global aux
    aux = col[currCol]
    while aux <= 5:
        led.plot_brightness(currCol, aux, 130)
        aux = aux + 1
def playGame():
    global lastAnswer, letter, expectedAns, someTIme, points
    basic.clear_screen()
    lastAnswer = 0
    letter = Math.random_boolean()
    if letter:
        basic.show_arrow(ArrowNames.WEST)
        expectedAns = -1
    else:
        basic.show_arrow(ArrowNames.EAST)
        expectedAns = 1
    someTIme = 5000
    while lastAnswer == 0 and someTIme > 0:
        basic.pause(10)
        someTIme = someTIme - 10
    if lastAnswer == expectedAns:
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        basic.clear_screen()
        points = points + 10
    elif lastAnswer != 0:
        basic.show_icon(IconNames.NO)
        basic.pause(500)
        basic.clear_screen()
    else:
        points = points - 10
        basic.clear_screen()
def Login():
    global setCode, currCol, currVal, col
    basic.clear_screen()
    setCode = 1
    currCol = 0
    currVal = 5
    col = [5, 5, 5, 5, 5]
def flash():
    global currCol
    for index2 in range(3):
        basic.clear_screen()
        basic.pause(300)
        for index3 in range(5):
            currCol = index3
            turnOnCol()
        basic.pause(500)

def on_button_pressed_ab():
    global lastAnswer, setCode, currentState, menu, totalTime
    lastAnswer = 2
    if setCode == 1:
        setCode = 0
        flash()
        basic.show_icon(IconNames.YES)
        currentState = 0
        menu = 0
    else:
        if menu == 0:
            if currentState == 0:
                Login()
                menu = 10
            elif currentState == 1:
                currentState = 0
                menu = 1
            elif currentState == 2:
                secretPoints = 0
                codify()
                serial.write_number(secretPoints)
            elif currentState == 3:
                menu = 3
        elif menu == 1:
            menu = 2
            totalTime = (currentState + 1) * 15000
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def setTime():
    global timeState
    timeState = 0
    while menu == 1:
        if currentState == 0:
            basic.show_leds("""
                # # . . .
                # . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        if currentState == 1:
            basic.show_leds("""
                . . . # #
                . . . . #
                . . . . .
                . . . . .
                . . . . .
                """)
        if currentState == 2:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . #
                . . . # #
                """)
        if currentState == 3:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                # # . . .
                """)
def randomTime():
    global generatedTime
    if currentState == 0:
        generatedTime = randint(60000, 180000)
    elif currentState == 1:
        generatedTime = randint(60000, 360000)
    elif currentState == 2:
        generatedTime = randint(60000, 540000)
    else:
        generatedTime = randint(60000, 720000)

def on_button_pressed_b():
    global lastAnswer, currCol, currVal, currentState
    lastAnswer = 1
    if setCode == 1:
        turnOnDimCol()
        if currCol == 4:
            currCol = 0
            turnOnCol()
        else:
            currCol = currCol + 1
            turnOnCol()
        currVal = 5
    elif menu == 0 or menu == 1:
        if currentState == 3:
            currentState = 0
        else:
            currentState = currentState + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def codify():
    pass
def setOption():
    while menu == 0:
        if currentState == 0:
            basic.show_leds("""
                # # . . .
                # # . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        if currentState == 1:
            basic.show_leds("""
                . . . # #
                . . . # #
                . . . . .
                . . . . .
                . . . . .
                """)
        if currentState == 2:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . # #
                . . . # #
                """)
        if currentState == 3:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                # # . . .
                # # . . .
                """)
timeState = 0
someTIme = 0
expectedAns = 0
letter = False
currVal = 0
lastAnswer = 0
totalTime = 0
generatedTime = 0
currCol = 0
col: List[number] = []
aux = 0
points = 0
setCode = 0
gameIsOn = 0
currentState = 0
menu = 0
serial.redirect_to_usb()
menu = 0
currentState = 0
gameIsOn = 0
setCode = 0
points = 50

def on_forever():
    if menu == 0:
        setOption()
    if menu == 1:
        setTime()
    if menu == 2:
        startClass()
    elif menu == 3:
        basic.show_string("Tutorial: Stanga sus = Login ")
        basic.show_string("Dreapta sus = setare timp (15/30/45/60 min)")
        basic.show_string("Dreapta jos = generare cod")
        basic.show_string("Stanga jos = Tutorial ")
        serial.write_line("Tutorial: Stanga sus = Login ")
        serial.write_line("Dreapta sus = setare timp (15/30/45/60 min)")
        serial.write_line("Dreapta jos = generare cod")
        serial.write_line("Stanga jos = Tutorial ")
        control.reset()
basic.forever(on_forever)

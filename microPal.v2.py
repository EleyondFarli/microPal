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
    menu = 0

def on_button_pressed_a():
    global lastAnswer, currVal, currentState
    lastAnswer = -1
    if setCode == 1:
        currVal = currVal + 1
    else:
        if menu == 0 or menu == 1:
            if currentState == 0:
                currentState = 3
            else:
                currentState = currentState - 1
        else:
            pass
input.on_button_pressed(Button.A, on_button_pressed_a)

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
    currVal = 0
    while currCol != 5:
        pass
    col = [0, 0, 0, 0, 0]
    basic.show_icon(IconNames.HEART)

def on_button_pressed_ab():
    global lastAnswer, currentState, menu, totalTime
    lastAnswer = 2
    if menu == 0:
        if currentState == 1:
            currentState = 0
            menu = 1
        else:
            if currentState == 0:
                Login()
            elif currentState == 2:
                secretPoints = 0
                codify()
                serial.write_number(secretPoints)
            else:
                basic.show_string("Tutorial: Stanga sus = Login ")
                basic.show_string("Dreapta sus = setare timp (15/30/45/60 min)")
                basic.show_string("Dreapta jos = generare cod")
                basic.show_string("Stanga jos = Tutorial ")
    else:
        if menu == 1:
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
    global lastAnswer, currCol, currentState
    lastAnswer = 1
    if setCode == 1:
        currCol = currCol + 1
    else:
        if menu == 0 or menu == 1:
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
col: List[number] = []
currCol = 0
someTIme = 0
expectedAns = 0
letter = False
currVal = 0
lastAnswer = 0
totalTime = 0
generatedTime = 0
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
    setOption()
    if menu == 1:
        setTime()
    if menu == 2:
        startClass()
basic.forever(on_forever)

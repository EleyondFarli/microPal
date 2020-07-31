def toText():
    global textstr, digit, index4, keyText, index2
    textstr = ""
    while index4 <= len(str2) - 1:
        digit = str2.char_at(index4)
        if digit == convert_to_text(0):
            textstr = "" + textstr + "L"
        elif digit == convert_to_text(1):
            textstr = "" + textstr + "M"
        elif digit == convert_to_text(2):
            textstr = "" + textstr + "N"
        elif digit == convert_to_text(3):
            textstr = "" + textstr + "O"
        elif digit == convert_to_text(4):
            textstr = "" + textstr + "P"
        elif digit == convert_to_text(5):
            textstr = "" + textstr + "Q"
        elif digit == convert_to_text(6):
            textstr = "" + textstr + "R"
        elif digit == convert_to_text(7):
            textstr = "" + textstr + "S"
        elif digit == convert_to_text(8):
            textstr = "" + textstr + "T"
        else:
            textstr = "" + textstr + "U"
        index4 += 1
    keyText = ""
    while index2 <= len(keyword) - 1:
        digit = keyword.char_at(index2)
        if digit == convert_to_text(0):
            keyText = "" + keyText + "L"
        elif digit == convert_to_text(1):
            keyText = "" + keyText + "M"
        elif digit == convert_to_text(2):
            keyText = "" + keyText + "N"
        elif digit == convert_to_text(3):
            keyText = "" + keyText + "O"
        elif digit == convert_to_text(4):
            keyText = "" + keyText + "P"
        elif digit == convert_to_text(5):
            keyText = "" + keyText + "Q"
        index2 += 1
def generateComponents():
    global keyword, pointsword, str2
    keyword = "" + convert_to_text(key[0]) + convert_to_text(key[1]) + convert_to_text(key[2]) + convert_to_text(key[3]) + convert_to_text(key[4])
    pointsword = convert_to_text(points)
    str2 = "" + convert_to_text(key[0]) + ("" + pointsword) + convert_to_text(key[1]) + ("" + pointsword) + convert_to_text(key[2]) + ("" + pointsword) + convert_to_text(key[3]) + ("" + pointsword) + convert_to_text(key[4])
def turnOnCol():
    global aux
    aux = key[currCol]
    while aux <= 5:
        led.plot(currCol, aux)
        aux = aux + 1
def startClass():
    global gameIsOn, totalTime, menu
    gameIsOn = 1
    basic.clear_screen()
    basic.show_string("Start")
    for index3 in range(5):
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
        currVal = key[currCol]
        if currVal == 0:
            turnOffCol()
            currVal = 5
        else:
            currVal = currVal - 1
        key[currCol] = currVal
        turnOnCol()
    elif menu == 0 or menu == 1:
        if currentState == 0:
            currentState = 3
        else:
            currentState = currentState - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def turnOnDimCol():
    global aux
    aux = key[currCol]
    while aux <= 5:
        led.plot_brightness(currCol, aux, 130)
        aux = aux + 1
def getValue(i: number):
    global c1, c2, v1, v2
    c1 = textstr.char_at(i)
    c2 = finalKey.char_at(i)
    if c1 == "L":
        v1 = 76
    elif c1 == "M":
        v1 = 77
    elif c1 == "N":
        v1 = 78
    elif c1 == "O":
        v1 = 79
    elif c1 == "P":
        v1 = 80
    elif c1 == "Q":
        v1 = 81
    elif c1 == "R":
        v1 = 82
    elif c1 == "S":
        v1 = 83
    elif c1 == "T":
        v1 = 84
    else:
        v1 = 85
    if c2 == "L":
        v2 = 76
    elif c2 == "M":
        v2 = 77
    elif c2 == "N":
        v2 = 78
    elif c2 == "O":
        v2 = 79
    elif c2 == "P":
        v2 = 80
    else:
        v2 = 81
    return (v1 + v2) % 26 + 65
def turnOffCol():
    global aux
    aux = key[currCol]
    while aux <= 5:
        led.unplot(currCol, aux)
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
    global setCode, currCol, currVal, key
    basic.clear_screen()
    setCode = 1
    currCol = 0
    currVal = 5
    key = [5, 5, 5, 5, 5]
def flash():
    global currCol
    for index32 in range(3):
        basic.clear_screen()
        basic.pause(100)
        for index5 in range(5):
            currCol = index5
            turnOnCol()
        basic.pause(500)

def on_button_pressed_ab():
    global lastAnswer, setCode, currentState, hasLoggedIn, menu, totalTime
    lastAnswer = 2
    if setCode == 1:
        setCode = 0
        flash()
        basic.show_icon(IconNames.YES)
        currentState = 0
        hasLoggedIn = 1
        menu = 0
    elif menu == 0:
        if currentState == 0:
            Login()
            menu = 10
        elif currentState == 1:
            currentState = 0
            if hasLoggedIn == 1:
                menu = 1
            else:
                basic.show_icon(IconNames.NO)
        elif currentState == 2:
            secretPoints = 0
            currentState = 0
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
def cipherText():
    global solution
    solution = ""
    index = 0
    while index <= len(textstr) - 1:
        solution = "" + solution + String.from_char_code(getValue(index))
        index += 1

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

def getKey():
    global x, i, finalKey
    x = len(textstr)
    i = 0
    finalKey = ""
    while len(finalKey) != len(textstr):
        if x == i:
            i = 0
        finalKey = "" + finalKey + keyText.char_at(i)
        i += 1
def codify():
    generateComponents()
    toText()
    getKey()
    cipherText()
    if len(solution) == 9:
        serial.write_line("00000000" + solution)
    else:
        if len(solution) == 13:
            serial.write_line("0000" + solution)
        else:
            serial.write_line("" + (solution))
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
i = 0
x = 0
solution = ""
timeState = 0
someTIme = 0
expectedAns = 0
letter = False
v2 = 0
v1 = 0
finalKey = ""
c2 = ""
c1 = ""
currVal = 0
lastAnswer = 0
totalTime = 0
generatedTime = 0
currCol = 0
aux = 0
pointsword = ""
key: List[number] = []
keyword = ""
index2 = 0
keyText = ""
digit = ""
str2 = ""
index4 = 0
textstr = ""
hasLoggedIn = 0
points = 0
setCode = 0
gameIsOn = 0
currentState = 0
menu = 0
finishedClass = 0
serial.redirect_to_usb()
menu = 0
currentState = 0
gameIsOn = 0
setCode = 0
points = 50
hasLoggedIn = 0

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

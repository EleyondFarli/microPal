# Write your code here :-)
from microbit import *
display.scroll("Hello!")

correct = Image.YES
incorrect = Image.NO

firstName = "firstName"
lastName = "lastName"
gender = "gender"
classNumber = "classNumber"
classLetter = "classLetter"

optionA = Image("99000:"
                "99000:"
                "00000:"
                "00000:"
                "00000:")

optionB = Image("00099:"
                "00099:"
                "00000:"
                "00000:"
                "00000:")

optionC = Image("00000:"
                "00000:"
                "00000:"
                "00099:"
                "00099:")

optionD = Image("00000:"
                "00000:"
                "00000:"
                "99000:"
                "99000:")

timeOptionA = Image("99000:"
                    "90000:"
                    "00000:"
                    "00000:"
                    "00000:")

timeOptionB = Image("00099:"
                    "00009:"
                    "00000:"
                    "00000:"
                    "00000:")

timeOptionC = Image("00000:"
                    "00000:"
                    "00000:"
                    "00009:"
                    "00099:")

timeOptionD = Image("00000:"
                    "00000:"
                    "00000:"
                    "90000:"
                    "99000:")

menu = [optionA, optionB, optionC, optionD]
menuTime = [timeOptionA, timeOptionB, timeOptionC, timeOptionD]

# Collection of images
images = [Image.SNAKE, Image.UMBRELLA, Image.SKULL, Image.GIRAFFE,
          Image.SWORD, Image.GHOST, Image.STICKFIGURE, Image.BUTTERFLY,
          Image.TORTOISE, Image.HOUSE, Image.DUCK, Image.ROLLERSKATE,
          Image.TSHIRT, Image.TARGET, Image.PACMAN, Image.XMAS,
          Image.PITCHFORK, Image.RABBIT, Image.DIAMOND,
          Image.HEART, Image.HEART_SMALL]

def switchLeft(currentNumber):
    if currentNumber == 0:
        currentNumber = 3
    else:
        currentNumber -= 1
    return currentNumber

def switchRight(currentNumber):
    if currentNumber == 3:
        currentNumber = 0
    else:
        currentNumber += 1
    return currentNumber


def Logare():
    with open('loginInfo.txt') as login:
        content = login.read()
        words = content.split()
        firstName = words[0]
        lastName = words[1]
        gender = words[2]
        classNumber = words[3]
        classLetter = words[4]
    with open('loginExit.txt') as exit:
        exit.write(firstName + ' ' + lastName + '\n' + gender + '\n'
                   + classNumber + ' ' + classLetter)

def selectTime():
    currentOption = timeOptionA
    currentNumber = 0
    while True:
        display.show(currentOption)

        if button_a.is_pressed() and button_b.is_pressed():
            display.show(correct)
            break
        elif button_a.is_pressed():
            currentNumber = switchLeft(currentNumber)
            currentOption = menuTime[currentNumber]
            sleep(600)
        elif button_b.is_pressed():
            currentNumber = switchRight(currentNumber)
            currentOption = menuTime[currentNumber]
            sleep(600)
    pass

def classStarted():
    pass

def Export():
    pass

def Tutorial():
    pass

def playSelected(currentOption):
    if currentOption == optionA:
        Logare()
    elif currentOption == optionB:
        selectTime()
        classStarted()
    elif currentOption == optionC:
        Export()
    elif currentOption == optionD:
        Tutorial()

def main():
    currentOption = optionA
    currentNumber = 0
    while True:
        display.show(currentOption)

        if button_a.is_pressed() and button_b.is_pressed():
            playSelected(currentOption)
            break
        elif button_a.is_pressed():
            currentNumber = switchLeft(currentNumber)
            currentOption = menu[currentNumber]
            sleep(600)
        elif button_b.is_pressed():
            currentNumber = switchRight(currentNumber)
            currentOption = menu[currentNumber]
            sleep(600)

            # with open('hello.txt', 'w') as hello:
            #    hello.write("Hello, World!")
            #    display.scroll("Write")
            #    sleep(2000)
            # with open('hello.txt') as hello2:
            #    content = hello2.read()
            #    display.scroll("Read")
            # print(content)
        # display.show(correct)
        # Sleep for random time between 1 and 10 minutes
        # sleep(random.randint(60000, 600000))
main()
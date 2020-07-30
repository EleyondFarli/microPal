# Write your code here :-)
from microbit import *
display.scroll("Hello!")

correct = Image.YES
incorrect = Image.NO

optionA = Image("99000:"
                "99000:"
                "00000:"
                "00000:"
                "00000:")

optionB = Image("99000:"
                "99000:"
                "00000:"
                "00000:"
                "00000:")

optionC = Image("99000:"
                "99000:"
                "00000:"
                "00000:"
                "00000:")

optionD = Image("99000:"
                "99000:"
                "00000:"
                "00000:"
                "00000:")

menu = [optionA, optionB, optionC, optionD]

while True:
    if button_a.is_pressed():
        with open('hello.txt', 'w') as hello:
            hello.write("Hello, World!")
            display.scroll("Write")
            sleep(2000)
        with open('hello.txt') as hello2:
            content = hello2.read()
            display.scroll("Read")
        print(content)
    display.show(correct)
    #Sleep for random time between 1 and 10 minutes
    #sleep(random.randint(60000, 600000))
#! /usr/bin/env
import random
def int_input(randomNumber):
    i = int(raw_input("How many sides do you want to your dice has"))
    j = int(raw_input("How many dices do you want?")
            if i < 2:
                return "the side of dice is wrong"
    randomNumber = random.randint(1,i)
    return randomNumber
print int_input(0)
            #ask user how many dices
            #ask them how many sides
import random
def int_input(randomNumber):
    i = int(raw_input("How many sides do you want to your dice has"))
    randomNumber = random.randint(1,i)
    return randomNumber
print int_input(0)
import random

tries = 0
options = []
for i in range(1000):#filling in the options array with 99 numbers
    options.append(i + 1)

gues = 0
random_number = random.choice(options)#choosing the number
while gues != random_number:
    gues = options[round(len(options) / 2)]#picking the number in the middle
    tries += 1

    if gues > random_number:
        a = 0
        for i in range(len(options)):#deleting all the numbers in teh options array that are bigger then the gues
            if options[a] >= gues:
                del options[a]
                a -= 1
            a += 1

    if gues < random_number:
        a = 0
        for i in range(len(options)):#deleting all the numbers in teh options array that are smaller then the gues
            if options[a] <= gues:
                del options[a]
                a -= 1
            a += 1



print("Randomly generated number: ", random_number)
print("Number of tries: ", tries)

from words import words #from file words.py import the words array
from random import *
import time

No_of_words = int(input("Number of words: "))

#wait for input to start
input("Start")

list = ""
for i in range(No_of_words):#making the list of random words

    random_word = words[randint(0, 1523)]

    list = list + random_word + " "


print(list)
time.sleep(2)
start = time.time()
user_input = input("Write: ")#user writing
finish = time.time()


total_time = round(finish - start)

wpm = (round(60 / (total_time / No_of_words)))#counting words per minute
print(list)
print(user_input)
print(total_time, " Seconds")
print(wpm, "WPM")


mistakes = 0
count = 0
for i in range(len(user_input)):#counting %
    if user_input[count] != list[count]:
        mistakes += 1
    count += 1

acuracy = round(100 - (mistakes / len(user_input) * 100))#calculating acuracy

print(f"Acuracy: {acuracy}%")
print(f"Number or errors: {mistakes}")

import string
import random
from time import sleep
import colorama

colorama.init()
up = colorama.Cursor.UP
right = colorama.Cursor.FORWARD

in_string = 'Hello'
ran_num = 50
delay_time = 0.01
ignore_space = False
list_string = list(in_string)
char_pos = 0
for i in list_string:
    if ignore_space:
        if i == ' ':
            char_pos += 1
            continue
    ran = random.choice(string.ascii_letters)
    if char_pos == 0:
        print(right(char_pos) + ran)
    else:
        print(up() + right(char_pos) + ran)
    for j in range(1, ran_num):
        ran2 = random.choice(string.ascii_letters)
        print(up() + right(char_pos) + ran2)
        sleep(delay_time)
    print(up() + right(char_pos) + i)
    char_pos += 1

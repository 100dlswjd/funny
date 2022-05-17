import random

number = [x for x in range(1,46)]
random.shuffle(number)

win = number[0:6]
win.sort()
print(win)
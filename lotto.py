import random

numbers = [num for num in range(1,46)]
random.shuffle(numbers)

win = numbers[0:6]
win.sort()
print(win)
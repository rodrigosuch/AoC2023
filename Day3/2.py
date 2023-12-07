import re

power = 0

def getGear(line):
    gears = []
    for idx in range(len(line)):
        if line[idx] == "*":
            gears.append(idx)
    return gears

def getNumbers(line):
    is_num = False
    num = ""
    numbers = []
    for idx in range(len(line)):
        if line[idx].isnumeric():
            num += line[idx]
            if is_num == False:
                is_num = True
                num_start = idx
        else:
            if is_num:
                num_end = idx-1
                numbers.append(dict(number = num, start = num_start, end = num_end))
            is_num = False
            num = ""
    return numbers

def find_adjacent_num(gear_pos, num1):
    adjacents = []
    total = 0
    for gear in gear_pos:
        for num in num1:
            if gear >= num["start"] - 1 and gear <= num["end"] + 1:
                adjacents.append(int(num["number"]))
        if len(adjacents) == 2:
            total += adjacents[0]*adjacents[1]
        adjacents.clear()
    return total

prev_1line = ""
prev_2line = ""
total = 0
for line in open("test.txt"):
    num_prev1 = getNumbers(prev_1line)
    num_prev2 = getNumbers(prev_2line)
    num_line = getNumbers(line)
    gears = getGear(prev_1line)
    total += find_adjacent_num(gears, num_prev1 + num_prev2 + num_line)

    prev_2line = prev_1line
    prev_1line = line

num_prev1 = getNumbers(prev_1line)
num_prev2 = getNumbers(prev_2line)
num_line = getNumbers(line)
gears = getGear(prev_1line)
for gear in gears:
    total += find_adjacent_num(gears, num_prev1, num_prev2, num_line)

print(total)






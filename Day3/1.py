import re
regex_game = 'Game \d+'
regex_color = '\d+ [a-zA-Z]+'

power = 0

def getSymbols(line):
    symbols = []
    for idx in range(len(line)):
        if line[idx].isnumeric() == False and line[idx] != "." and line[idx] != "\n":
            symbols.append(idx)
    return symbols

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

def find_num_in_list(num_start, num_end, list):
    for symb_pos in list:
        if symb_pos >= num_start - 1 and symb_pos <= num_end + 1:
            return True
    return False

prev_1line = ""
prev_2line = ""
total = 0
for line in open("test.txt"):
    symb_prev1 = getSymbols(prev_1line)
    symb_prev2 = getSymbols(prev_2line)
    symb_line = getSymbols(line)
    numbers = getNumbers(prev_1line)
    for number in numbers:
        if find_num_in_list(number["start"], number["end"], symb_prev1):
            total += int(number["number"])
            continue
        if find_num_in_list(number["start"], number["end"], symb_prev2):
            total += int(number["number"])
            continue
        if find_num_in_list(number["start"], number["end"], symb_line):
            total += int(number["number"])
            continue

    prev_2line = prev_1line
    prev_1line = line

symb_prev1 = getSymbols(prev_1line)
symb_prev2 = getSymbols(prev_2line)
symb_line.clear()

numbers = getNumbers(prev_1line)

for number in numbers:
    if find_num_in_list(number["start"], number["end"], symb_prev1):
        total += int(number["number"])
        continue
    if find_num_in_list(number["start"], number["end"], symb_prev2):
        total += int(number["number"])
        continue
    if find_num_in_list(number["start"], number["end"], symb_line):
        total += int(number["number"])
        continue
print(total)






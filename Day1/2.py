numbers = (('zero', 0), ('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine',9))
def get_first_and_last(str):
    first = -1
    last = -1
    for idx in range(len(str)):
        curr_str = str[idx:]
        value = -1
        if curr_str[0] in "0123456789":
            value = int(curr_str[0])
        for number in numbers:
            if curr_str.startswith(number[0]) == True:
                value = number[1]
        if value != -1:
            if first == -1:
                first = value
            last = value
    return 10*first + last

total = 0
for line in open('test_file.txt', 'r'):
    total += get_first_and_last(line)
print(total)

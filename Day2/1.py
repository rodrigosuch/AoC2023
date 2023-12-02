import re
regex_game = 'Game \d+'
regex_color = '\d+ [a-zA-Z]+'

total = 0
for line in open('input1.txt'):
    game_number = re.findall(regex_game, line)[0].split(" ")[1]
    color = re.findall(regex_color, line)
    possible = True
    for item in color:
        if item.split(" ")[1] == 'blue' and int(item.split(" ")[0]) > 14:
            possible = False
        if item.split(" ")[1] == 'red' and int(item.split(" ")[0]) > 12:
            possible = False
        if item.split(" ")[1] == 'green' and int(item.split(" ")[0]) > 13:
            possible = False
    if possible:
        total += int(game_number)

print(total)






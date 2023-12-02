import re
regex_game = 'Game \d+'
regex_color = '\d+ [a-zA-Z]+'

power = 0

for line in open('input1.txt'):
    game_number = re.findall(regex_game, line)[0].split(" ")[1]
    color = re.findall(regex_color, line)
    blue = 0
    green = 0
    red = 0
    for item in color:
        if item.split(" ")[1] == 'blue' and int(item.split(" ")[0]) > blue:
            blue = int(item.split(" ")[0])
        if item.split(" ")[1] == 'red' and int(item.split(" ")[0]) > red:
            red = int(item.split(" ")[0])
        if item.split(" ")[1] == 'green' and int(item.split(" ")[0]) > green:
            green = int(item.split(" ")[0])
    power += red * blue * green

print(power)






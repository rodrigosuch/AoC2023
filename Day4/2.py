import re

total = 0
line_idx = 1
num_cards = []

def find_matches(winners, my_nums):
    num_match = 0
    for winner in winners:
        if winner in my_nums:
            num_match += 1

    return num_match

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

num_lines = file_len("test.txt")
cards =[1]*num_lines

for line in open("test.txt"):
    winners, my_nums = line.split(":")[1].split("|")
    winners = re.findall(r'\d+', winners)
    my_nums = re.findall(r'\d+', my_nums)
    matches = find_matches(winners, my_nums)
    for idx in range(matches):
        if line_idx + idx >= num_lines or line_idx-1 >= num_lines:
            continue
        cards[line_idx + idx] += cards[line_idx-1]
    line_idx += 1

for idx in range(num_lines):
    total += cards[idx]

print(total)
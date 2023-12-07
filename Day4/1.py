num_points = 0
import re

def find_matches(winners, my_nums):
    num_match = 0
    for winner in winners:
        if winner in my_nums:
            num_match += 1

    if num_match >= 1:
        return (1 << (num_match-1))
    return 0

total = 0
count = 1
for line in open("test.txt"):
    winners, my_nums = line.split(":")[1].split("|")
    winners = re.findall(r'\d+', winners)
    my_nums = re.findall(r'\d+', my_nums)
    matches = find_matches(winners, my_nums)
    print(matches)
    total += matches
    count += 1

print(total)
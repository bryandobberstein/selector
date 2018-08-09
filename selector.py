import csv
import sys
from random import choice


with open(sys.argv[1], 'r', newline='') as file:
    temp_csv = csv.reader(file)
    contestant_list = [line for line in temp_csv]

winner = choice(contestant_list)

contestant_list.remove(winner)

with open(sys.argv[1], 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    for line in contestant_list:
        writer.writerow(line)

print(winner[0])

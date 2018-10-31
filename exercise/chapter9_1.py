#__author:iruyi
#date:2018/10/31
import sys

# Find the different bird types observed.
birds = set()

infile = open("../data/birds.txt", 'r')
for line in infile:
    name = line.strip()
    birds.add(name)
infile.close()

# Print the birds.
for b in birds:
    print(b)
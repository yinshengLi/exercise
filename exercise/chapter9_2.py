#__author:iruyi
#date:2018/10/31

# Find all the birds
birds = []

infile = open('../data/birds.txt', 'r')

# For each bird, find its entry and increment the count.
for line in infile:
    name = line.strip()
    found = False
    for entry in birds:
        if entry[0] == name:
            entry[1] += 1
            found = True
    if not found:
        birds.append([name,1])
infile.close()

# Print
for (name, count) in birds:
    print(name,count)
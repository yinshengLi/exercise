#__author:iruyi
#date:2018/10/31

scientists = {'Newton': 1642, 'Darwin': 1809, 'Turing': 1912}
print(scientists.get('Newton'))
print('Specified', scientists.get('Newton2', 1500)) # if key does not exist in dict ,return the designated value
print(scientists['Newton'])
print('items:', scientists.items())

temp = {'Curie': 1867, 'Hopper': 1906, 'Franklin': 1920}
scientists.update(temp) # copy temp to scientists
print(scientists)

for (key, value) in scientists.items():
    print('key=', key, ' value=', value)



scientists.clear()
print('after clear:', scientists)

print("-------------use dictionary to store data----------------")
infile = open('../data/birds.txt', 'r')
count = {}
for line in infile:
    name = line.strip()
    if name in count:
        count[name] = count[name] + 1
    else:
        count[name] = 1
infile.close()

for b in count:
    print(b, ' ', count[b])


#优化
print('----------optimize-------------')
infile2 = open('../data/birds.txt', 'r')
count2 = {}
for line in infile2:
    name = line.strip()
    count2[name] = count2.get(name, 0) + 1
infile2.close()

for b in count2:
    print(b, ' ', count2[b])

print('----------optimize2-- change key to value and value to key--------------')
infile3 = open('../data/birds.txt', 'r')
count3 = {}
for line in infile3:
    name = line.strip()
    count3[name] = count3.get(name, 0) + 1
infile3.close()
print('count3:', count3)
# Invert the dictionary
freq = {}
for (name, times) in count3.items():
    if times in freq:
        freq[times].append(name)
    else:
        freq[times] = [name]

# Print.
print('freq:', freq)
for key in sorted(freq):
    print(key)
    for name in freq[key]:
        print(' ', name)
#__author:iruyi
#date:2018/10/29

list1 = [4, 12, 20, 38, 56, 88]
alkaline_earth_metals = list1

print(list1[5])
print(list1[-1])

print(len(alkaline_earth_metals))
print(max(alkaline_earth_metals))

print(' a')
tt = ' a',
print(tt)
print("--------------------")
country_populations = [1295, 23, 3, 47]
for i in country_populations:
    print(i, end=",")

total = 0
for i in country_populations:
    total += i
print(total)

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
print(temps)
count = 0
for i in range(len(temps)):
    if temps[i] > 20:
        count = i
        break

cool_temps = temps[0:count]
warm_temps = temps[count:]
print("cool_temps", cool_temps)
print("warm_temps:",warm_temps)

temps_in_celsius = cool_temps + warm_temps
print("new_list:", temps_in_celsius)
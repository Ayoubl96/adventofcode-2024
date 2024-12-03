import re

with open("test.txt", "r") as file:
    file_open = file.read()

array = file_open.strip()
print(array)

regex = r"mul\((\d{1,3}),(\d{1,3})\)"


numeri = re.findall(regex, array)

print(numeri)

total = 0
for x,y in numeri:
    total = total + int(x) * int(y)
print(total)
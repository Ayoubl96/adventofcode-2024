
file = open("data.txt", "r")
file_open = file.read()

array = file_open.split()
col1 = []
col2 = []
i = 0

for n in array:
    n = int(n)
    if (i % 2 == 0):
        col1.append(array[i])
    elif (i == 0):
        col1.append(array[i])
    else:
        col2.append(array[i])
    i = i + 1

col1 = sorted(col1)
col2 = sorted(col2)

sum = 0
i = 0
for n in col1:
    col2_number = int(col2[i])
    n = int(n)
    sum = sum + abs(n - col2_number)
    i = i + 1

print(sum)

total_score = 0    
for n in col1:
    score = 0
    for number in col2:
        if n == number:
            total_score = total_score + 1 * int(n)

print(total_score)
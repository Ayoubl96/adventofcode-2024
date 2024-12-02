
safe = 0
for line in lines:
    score = 0
    type = ""
    if int(line[0]) - int(line[1]) < 0:
        type = "inc"
    elif int(line[0]) - int(line[1]) > 0:
        type = "dec"
    else:
        type = "null"
    line_len = len(line)
    for n in range(1, line_len):
        number_one = int(line[n - 1])
        number_two = int(line[n])
        if type == "inc":
            if number_one - number_two == -3 or number_one - number_two == -2 or number_one - number_two == -1:
                score = score + 1
        if type == "dec":
            if number_one - number_two == 3 or number_one - number_two == 2 or number_one - number_two == 1:
                score = score + 1
    if score == line_len - 1:
        safe = safe + 1

print(safe)

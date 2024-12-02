with open("data.txt", "r") as file:
    file_open = file.read()

array = file_open.strip().split("\n")

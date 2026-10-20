n = int(input("Enter number of lines: "))

with open("sample.txt", "r") as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line, end="")
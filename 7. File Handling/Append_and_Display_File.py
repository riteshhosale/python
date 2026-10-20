f = open("sample.txt", "a")
f.write("\nWelcome to Python")
f.close()

f = open("sample.txt", "r")
print(f.read())
f.close()
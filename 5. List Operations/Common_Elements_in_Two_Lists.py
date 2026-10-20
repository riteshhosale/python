a = [1, 2, 3, 4]
b = [5, 6, 3, 8]

common = any(x in b for x in a)
print(common)
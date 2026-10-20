def length(value):
    count = 0
    for item in value:
        count += 1
    return count

print(length("Python"))
print(length([10, 20, 30, 40]))
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

result = [x for i, x in enumerate(a)
          if i not in (0, 2, 4, 5)]

print(result)
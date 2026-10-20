d = {'A': 30, 'B': 10, 'C': 20}

print("Ascending:",
      dict(sorted(d.items(), key=lambda x: x[1])))

print("Descending:",
      dict(sorted(d.items(),
                  key=lambda x: x[1], reverse=True)))
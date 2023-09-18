x = [0, 1, 1, 0]
y = [0, 0, 1, 1]

n = len(x)
area = 0

# Process all vertices one by one
for i in range(n):
    area += x[i]* (y[(i + 1) % n] - y[(i - 1 + n) % n])

print(0.5 * area)
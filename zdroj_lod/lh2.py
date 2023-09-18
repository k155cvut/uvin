def LH(X,Y):
    n = len(X)
    area = 0
    for i in range(n):
        area += X[i]* (Y[(i + 1) % n] - Y[(i - 1 + n) % n])
    return 0.5 * area

X = [0, 1, 1, 0]
Y = [0, 0, 1, 1]

area = LH(X,Y)
print(area)

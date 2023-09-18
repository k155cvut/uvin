def findMinMax(X):
    xmin = X[0]
    xmax = X[0]
    for x in X:
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
    return xmin, xmax

X = [10, -27, 3, 48, 0, 95]
xmin, xmax = findMinMax(X)
print("max = " + str(xmax) + ", min = " + str(xmin))
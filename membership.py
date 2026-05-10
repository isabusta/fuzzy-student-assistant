def triangular(x, a, b, c):
    if x == b:
        return 1.0
    if x <= a or x >= c:
        return 0.0
    if x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)

def trapezoidal(x, a, b, c, d):
    if b <= x <= c:
        return 1.0
    if x <= a or x >= d:
        return 0.0
    if a < x < b:
        return (x - a) / (b - a)
    return (d - x) / (d - c)

import math


# Треугольники
def getTriangleSquare(a, b, c):
    p = (a + b + c)/2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def isTriangleExist(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        return False
    return True


def isTriangleRight(a, b, c):
    l = [a, b, c]
    m = max(a, b, c)
    l.remove(m)
    if (l[0]**2 + l[1]**2)**0.5 == m:
        return True
    return False


# Окружность
def getRoundSquare(r):
    return math.pi * r ** 2


def checkRound(r):
    if r < 0:
        return False
    return True


def getFlatSquare(*args) -> float:
    if len(args) == 1:  # является кругом
        if not checkRound(args[0]):
            raise ValueError('r below zero')
        return getRoundSquare(args[0])
    if len(args) == 3:  # является треугольником
        if isTriangleExist(*args):
            return getTriangleSquare(*args)
        raise ValueError('invalid values')

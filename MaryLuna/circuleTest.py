import math

def circleArea(radio):
    if radio > 10:
        return math.pi * radio ** 2

def sumar(n):
    end_of_series = n if n < 35 else 35
    return end_of_series * (end_of_series + 1) / 2

area = 50
print(f"Area of circle of radio {area} is", circleArea(area))

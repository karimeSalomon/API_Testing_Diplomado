import math

def area_of_circle(r):
    if r > 10:
        return math.pi * r**2
        
def sum_to(n):
    end_of_series = n if n < 35 else 35
    return end_of_series * (end_of_series + 1) / 2

a = 11
print(f"Area of circle of radio {a} is", area_of_circle(a))
a = 10
print(f"Area of circle of radio {a} is", area_of_circle(10))
print(f"Sum of first {a} integers is", sum_to(a))
a = 34
print(f"Sum of first {a} integers is", sum_to(a))
a = 35
print(f"Sum of first {a} integers is", sum_to(a))
a = 40
print(f"Sum of first {a} integers is", sum_to(a))
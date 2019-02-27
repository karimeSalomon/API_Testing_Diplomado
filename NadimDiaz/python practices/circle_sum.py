import math

def area_of_circle(r):
    if r > 10:
        result = math.pi * r**2
        return result
        
def sum_to(n):
    end_of_series = n if n < 35 else 35
    return end_of_series * (end_of_series + 1) / 2

def main():
    #area of circle
    print("area of 4:", area_of_circle(4))
    print("area of 6:", area_of_circle(6))
    
    #sume of first elements
    print("Sum of first elements until 34", sum_to(34))
    print("Sum of first elements until 40", sum_to(40))
    print("Sum of first elements until 40", sum_to(45))
main()
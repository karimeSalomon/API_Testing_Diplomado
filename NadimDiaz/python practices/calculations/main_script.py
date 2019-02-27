import radius_circle
import perimeter_circle

def get_data():
    radius = int(input("Which is the radius of your circle?: "))
    
    print("Calculate a radius of circle with radius = 3", radius_circle.calculate_radius(radius))
    print("Calculate a perimeter of circle with radius = 4", radius_circle.calculate_radius(radius)) 

get_data()
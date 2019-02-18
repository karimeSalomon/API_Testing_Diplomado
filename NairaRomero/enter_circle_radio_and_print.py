import calculate_perimeter_circle as perimeter
import calculate_radius_circle as radius


def enter_radio_and_perimeter():
    rad = input("Enter a radius circle")
    print("Area:", (perimeter.calculate_perimeter_circle(int(rad))))
    print("Perimeter:", (radius.calculate_radius_circle(int(rad))))

enter_radio_and_perimeter()
import Area
import Perimeter


def show_circle_calculations():
    radio = int(input("Enter the radio of the circle: "))
    area = Area.area_of_circle(radio)
    perimeter = Perimeter.perimeter_of_circle(radio)
    print('The area of the circle is: ', area)
    print('The perimeter of the circle is: ', perimeter)


show_circle_calculations()

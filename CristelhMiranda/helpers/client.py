from CristelhMiranda.helpers.area_calc import circle_area
from CristelhMiranda.helpers.perimeter_calc import circle_per

radio = float(input("Enter circle's radio: "))

area = circle_area.get_area(radio)
perimeter = circle_per.get_perimeter(radio)

print(f'{"Area or radio:"} {radio} {"is:"} {area}')
print(f'{"Perimeter or radio:"} {radio} {"is:"} {area}')

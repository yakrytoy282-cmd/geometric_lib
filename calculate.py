from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter

def calculate_area(shape, *args):
    if shape == 'circle':
        return circle_area(*args)
    elif shape == 'square':
        return square_area(*args)
    else:
        return None

import math

def solve_quadratic_equation(a, b, c):
    """Находит корни квадратного уравнения вида ax^2 + bx + c = 0."""
    # Вычисляем дискриминант.
    discriminant = b**2 - 4*a*c

    # Если дискриминант меньше 0, корней нет.
    if discriminant < 0:
        return []

    # Если дискриминант равен 0, есть только один корень.
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]

    # Если дискриминант больше 0, есть два корня.
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
       

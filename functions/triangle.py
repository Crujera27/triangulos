def triangle_type(sides):
    sides.sort()
    a, b, c = sides

    if a + b <= c:
        return "IMPOSIBLE"
    elif a ** 2 + b ** 2 == c ** 2:
        return "RECTANGULO"
    elif a ** 2 + b ** 2 < c ** 2:
        return "OBTUSANGULO"
    else:
        return "ACUTANGULO"

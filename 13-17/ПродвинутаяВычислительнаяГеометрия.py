from typing import List, Tuple #Импортируем типы для аннотаций:List - тип для списков Tuple - тип для кортежей

def polygon_area(points: List[Tuple[float, float]]) -> float:
    # Вычисляет площадь простого многоугольника по формуле shoelace.
    # points: список вершин (x, y) в порядке обхода (по или против часовой стрелки).
    n = len(points)
    if n < 3:
        return 0.0  # так как это не многоугольник

    S = 0.0
    i = 0
    while i < n:
        x_i, y_i = points[i]
        j = (i + 1) % n  # индекс следующей вершины (% n - операция модуля обеспечивает "зацикливание": 
                         # для последней вершины следующей будет первая.
        x_j, y_j = points[j]
        S += x_i * y_j - x_j * y_i
        i += 1
    A = abs(S) / 2.0
    return A

if __name__ == "__main__":
    polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print("Площадь многоугольника:", polygon_area(polygon))


from typing import List, Tuple

def linear_regression_gd(
    data: List[Tuple[float, float]],
    lr: float = 0.01,
    epochs: int = 1000
) -> Tuple[float, float]:
    # Линейная регрессия y = a*x + b с использованием градиентного спуска.
    # data: список пар (x, y)
    # lr: шаг обучения
    # epochs: число итераций
    # Возвращает (a, b).
    a = 0.0  # начальное значение наклона
    b = 0.0  # начальное значение смещения
    n = len(data)

    for _ in range(epochs):
        # Вычисляем градиенты по a и b
        da = 0.0
        db = 0.0
        for x, y in data:
            y_pred = a * x + b #Прогноз
            error = y_pred - y #Ошибка
            da += error * x #Накопление градиентов
            db += error
        da /= n #Усреднение градиентов по всем точкам данных
        db /= n

        # Обновляем параметры в направлении уменьшения ошибки
        a -= lr * da
        b -= lr * db

    return a, b
if __name__ == "__main__":
    points = [(1, 2), (2, 3), (3, 4), (4, 5)]
    a, b = linear_regression_gd(points, lr=0.05, epochs=1000)
    print(f"Найденная модель: y ≈ {a:.3f} * x + {b:.3f}")
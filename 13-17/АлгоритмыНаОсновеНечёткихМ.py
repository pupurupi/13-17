from typing import List, Tuple
import numpy as np
# --- Функции принадлежности для температуры ---
def mu_low_temp(x: float) -> float:
    # Низкая температура: 1 при 0, линейно до 0 при 20, дальше 0.
    if x <= 0:
        return 1.0
    if 0 < x < 20:
        return (20 - x) / 20.0
    return 0.0
def mu_high_temp(x: float) -> float:
    # Высокая температура: 0 до 20, линейно до 1 при 40, дальше 1.
    if x <= 20:
        return 0.0
    if 20 < x < 40:
        return (x - 20) / 20.0
    return 1.0
# --- Выходные термы (мощность вентилятора) ---
def triangle(y: float, a: float, b: float, c: float) -> float:
    # Треугольная функция принадлежности с вершиной в b.
    if y <= a or y >= c:
        return 0.0
    if a < y < b:
        return (y - a) / (b - a)
    if b <= y < c:
        return (c - y) / (c - b)
    return 0.0
def mu_low_power(y: float) -> float:
    # Малая мощность (центр около 20).
    return triangle(y, 0, 20, 40)
def mu_high_power(y: float) -> float:
    # Большая мощность (центр около 80).
    return triangle(y, 60, 80, 100)
# --- Нечеткий вывод Мамдани ---
def mamdani_fan_power(temp: float) -> float:
    # Вход: температура temp (0..40).
    # Выход: чёткое значение мощности вентилятора (0..100).
    # Правила:
    #   1) ЕСЛИ температура низкая, ТО мощность малая.
    #   2) ЕСЛИ температура высокая, ТО мощность большая.
    # 1. Фаззификация входа
    mu_low = mu_low_temp(temp)
    mu_high = mu_high_temp(temp)
    # 2. Степени срабатывания правил
    alpha1 = mu_low       # правило 1
    alpha2 = mu_high      # правило 2
    # 3–4. Формирование и агрегация выходных нечетких множеств
    ys = np.linspace(0, 100, 501)   # дискретизируем ось мощности
    aggregated = np.zeros_like(ys)
    for i, y in enumerate(ys):
        # Нечёткие заключения от каждого правила (обрезка по степени срабатывания)
        mu1_out = min(alpha1, mu_low_power(y))    # «малая мощность»
        mu2_out = min(alpha2, mu_high_power(y))   # «большая мощность»
        # Агрегация правил (max)
        aggregated[i] = max(mu1_out, mu2_out)
    # 5. Дефаззификация методом центра тяжести
    if aggregated.sum() == 0:
        return 0.0
    crisp_power = float((ys * aggregated).sum() / aggregated.sum())
    return crisp_power
if __name__ == "__main__":
    t = float(input("Введите температуру (0..40): "))
    power = mamdani_fan_power(t)
    print(f"Рекомендуемая мощность вентилятора: {power:.2f}")


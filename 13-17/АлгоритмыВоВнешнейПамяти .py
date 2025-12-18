def build_index(filename):
    # Построение индекса по файлу.
    # Файл должен содержать записи вида: <ключ> <значение> (в одной строке).
    # Возвращает словарь: ключ -> позиция в файле.
    index = {}   # Создать пустой индекс
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            pos = f.tell()  # Запомнить позицию перед чтением строки
            line = f.readline() # Считать строку
            if not line: # Есть ещё строки? (нет — конец файла)
                break
            line = line.strip()
            if not line:
                continue # Пропускаем пустые строки
            parts = line.split(maxsplit=1)
            key = parts[0] # Извлечь ключ
            index[key] = pos # Добавить ключ и позицию в индекс
    return index


def indexed_search(filename: str, index: dict, search_key: str):
    # Поиск значения по ключу с использованием индекса.
    # Возвращает значение (строка после ключа) или "не найдено", если не найдено.
    # Ключ есть в индексе?
    if search_key not in index:
        return 'не найдено'                 # Не найдено

    with open(filename, 'r', encoding='utf-8') as f:
        # Перейти к позиции из индекса
        f.seek(index[search_key])
        line = f.readline()  # Считать строку
        line = line.strip()
        if not line:
            return None
        parts = line.split(maxsplit=1)
        if len(parts) == 1:
            return ""  # Ключ есть, но значения нет
        value = parts[1] # Извлечь значение
        return value


if __name__ == "__main__":
    # --- Пример использования ---
    # 1. Создадим тестовый файл с записями
    filename = "data.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write("1 apple\n")
        f.write("2 banana\n")
        f.write("3 cherry\n")

    # 2. Построим индекс по файлу
    index = build_index(filename)
    print("Индекс:", index)

    # 3. Выполним поиск по ключу
    search_key = input("Введите ключ для поиска: ")

    value = indexed_search(filename, index, search_key)
    print(f"Значение для ключа {search_key}: {value}")

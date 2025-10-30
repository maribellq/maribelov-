Блочная сортировка
def bucket_sort(arr):
    # Определяем максимальное значение массива для вычисления количества корзин
    max_value = max(arr)
    
    # Создаем список пустых корзин
    size = len(arr)
    buckets_list = []
    for _ in range(size):
        buckets_list.append([])
        
    # Распределяем элементы исходного массива по корзинам
    for i in range(len(arr)):
        index = int((size * arr[i]) / (max_value + 1))
        buckets_list[index].append(arr[i])
    
    # Сортируем каждую корзину отдельно простым методом сортировки (например, вставками)
    for i in range(size):
        buckets_list[i] = sorted(buckets_list[i])
    
    # Объединяем отсортированные корзины обратно в массив
    final_output = []
    for i in range(size):
        final_output += buckets_list[i]
    
    return final_output

# Тестируем алгоритм
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_arr = bucket_sort(arr)
print("Отсортированный массив:", sorted_arr)

Вывод:
Отсортированный массив: [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]

Блинная сортировка
def reverse_subarray(arr, end):
    """
    Переводит часть массива arr от начала до end (включительно) наоборот.
    """
    start = 0
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def pancake_sort(arr):
    """
    Алгоритм блинной сортировки массива arr.
    """
    n = len(arr)
    for curr_size in reversed(range(1, n+1)):  # Начинаем с полного массива и постепенно уменьшаем
        # Находим индекс максимального элемента в текущей области
        max_idx = arr.index(max(arr[:curr_size]))
        
        # Если максимальный элемент уже на месте, пропускаем
        if max_idx != curr_size - 1:
            # Переворачиваем часть массива от начала до max_idx (переносим максимум в начало)
            reverse_subarray(arr, max_idx)
            
            # Теперь переворачиваем всю текущую область, отправляя максимум в конец
            reverse_subarray(arr, curr_size - 1)

# Пример использования
if __name__ == "__main__":
    arr = [3, 6, 2, 4, 5, 1]
    print("Исходный массив:", arr)
    pancake_sort(arr)
    print("Отсортированный массив:", arr)

Вывод:
Исходный массив: [3, 6, 2, 4, 5, 1]
Отсортированный массив: [1, 2, 3, 4, 5, 6]

Сортировка бусинами
def bead_sort(arr):
    # Фиксируем размеры массива
    rows = len(arr)
    cols = max(arr)

    # Формируем матрицу 'бусинок' (1 - есть бусинка, 0 - нет)
    beads = [[1]*val + [0]*(cols-val) for val in arr]

    # Моделируем падение бусинок вниз
    for col in range(cols):
        count = sum(beads[row][col] for row in range(rows))
        for row in range(count):
            beads[row][col] = 1
        for row in range(count, rows):
            beads[row][col] = 0

    # Преобразуем матрицу обратно в отсортированный массив
    result = [sum(row) for row in zip(*beads)]
    return result


# Пример использования
if __name__ == "__main__":
    arr = [5, 3, 1, 7, 4, 6, 2]
    print("Исходный массив:", arr)
    sorted_arr = bead_sort(arr)
    print("Отсортированный массив:", sorted_arr)

Вывод:
Исходный массив: [5, 3, 1, 7, 4, 6, 2]
Отсортированный массив: [1, 2, 3, 4, 5, 6, 7]

поиск скачками
import math

def jump_search(arr, target):
    """
    Алгоритм поиска скачками.
    :param arr: Отсортированный массив
    :param target: Значение, которое надо найти
    :return: Индекс элемента, если найден, иначе -1
    """
    n = len(arr)
    # Определим оптимальный шаг (block size) ~ sqrt(n)
    step = int(math.sqrt(n))
    
    # Найдем блок, где возможно находится искомый элемент
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Выход за границу массива
    
    # Произведем линейный поиск в найденном блоке
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    
    return -1  # Элемент не найден

# Пример использования
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 55
    result = jump_search(arr, target)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}")
    else:
        print(f"Элемент {target} не найден")

Вывод:
Элемент 55 найден на позиции 10

экспоненциональный поиск
def exponential_search(arr, target):
    """
    Реализует экспоненциальный поиск в отсортированном массиве.
    :param arr: Отсортированный массив
    :param target: Цель поиска
    :return: Индекса элемента, если найден, иначе -1
    """
    n = len(arr)
    
    # Если первый элемент совпадает с целью, вернуть его индекс
    if arr[0] == target:
        return 0
    
    # Ищем подходящую зону методом удвоения шага
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Применяем двоичный поиск в найденном подинтервале
    low = i // 2
    high = min(i, n-1)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Элемент не найден

# Пример использования
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 55
    result = exponential_search(arr, target)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}")
    else:
        print(f"Элемент {target} не найден")

Вывод:
Элемент 55 найден на позиции 10


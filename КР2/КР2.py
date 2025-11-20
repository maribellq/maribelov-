def greedy_coloring(adj_list):
    n = len(adj_list)
    colors = [-1] * n  # -1 означает, что цвет не назначен
    for v in range(n):
        # Собрать используемые цвета соседей
        used = set()
        for neighbor in adj_list[v]:
            if colors[neighbor] != -1:
                used.add(colors[neighbor])
        # Назначить минимальный доступный цвет
        color = 0
        while color in used:
            color += 1
        colors[v] = color
    return colors

# Основная часть программы для ручного ввода через консоль
if __name__ == "__main__":
    # Ввод количества вершин
    n = int(input("Введите количество вершин (n): "))
    
    # Инициализация списка смежности
    adj_list = [[] for _ in range(n)]
    
    # Ввод количества рёбер
    m = int(input("Введите количество рёбер (m): "))
    
    print("Введите рёбра в формате 'u v' (вершины от 0 до n-1, по одному ребру на строку):")
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)  # Поскольку граф неориентированный
    
    # Вызов функции раскраски
    colors = greedy_coloring(adj_list)
    
    # Вывод результата
    print("\nРаскраска вершин:")
    for v in range(n):
        print(f"Вершина {v}: цвет {colors[v]}")
    



Вывод в консоль:

Введите количество вершин (n): 3
Введите количество рёбер (m): 3
Введите рёбра в формате 'u v' (вершины от 0 до n-1, по одному ребру на строку):
0 1
1 2
0 2

Раскраска вершин:
Вершина 0: цвет 0
Вершина 1: цвет 1
Вершина 2: цвет 2

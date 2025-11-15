import random
import math

# Функция цели
def objective_function(x):
    return (x - 7)**2 + 5

# Параметры отжига
initial_temperature = 1000       # начальная высокая температура
final_temperature = 1            # конечная низкая температура
alpha = 0.98                    # коэффициент снижения температуры
max_iterations_per_temp = 10     # количество итераций на каждой температуре

# Шаг 1: Генерируем начальное решение
current_solution = random.uniform(0, 20)
best_solution = current_solution
min_value = objective_function(best_solution)

temperature = initial_temperature

while temperature > final_temperature:
    for _ in range(max_iterations_per_temp):
        # Шаг 2: Генерация нового кандидата (случайный сдвиг около текущего решения)
        new_candidate = current_solution + random.uniform(-1, 1)
        
        # Ограничиваем диапазон новых кандидатов внутри интервала [0, 20]
        if new_candidate < 0 or new_candidate > 20:
            continue
            
        # Вычисляем изменение функции
        delta_f = objective_function(new_candidate) - objective_function(current_solution)
    
        # Принятие лучшего решения
        if delta_f <= 0:
            current_solution = new_candidate
            if objective_function(new_candidate) < min_value:
                best_solution = new_candidate
                min_value = objective_function(best_solution)
        else:
            # Вероятностное принятие ухудшения
            prob_acceptance = math.exp(-delta_f / temperature)
            if random.random() < prob_acceptance:
                current_solution = new_candidate
                
    # Понижение температуры
    temperature *= alpha

print(f'Минимум функции: {min_value:.4f}, координата x: {best_solution:.4f}')


Вывод в консоль:
Минимум функции: 5.0000, координата x: 7.0000
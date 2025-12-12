### Задание 6: CNN для классификации изображений (Fashion-MNIST)
Задача: создать сверточную нейронную сеть (CNN) для классификации элементов 
одежды из Fashion-MNIST.
Требования:
Архитектура: Conv2D(32) → MaxPooling → Conv2D(64) → MaxPooling → 
Dense(128) → Dense(10)
Использовать ReLU активацию для скрытых слоёв
Data augmentation (случайные повороты, сдвиги)
Dropout для регуляризации
Код-заготовка (Python):
import tensorflow as tf
from tensorflow import keras
import numpy as np
class FashionMNISTCNN:
 def __init__(self):
  TODO: Создать модель с conv2d и maxpooling слоями
  Архитектура:
  - Conv2D(32, kernel_size=3, padding='same')
  - MaxPooling2D(2)
 - Conv2D(64, kernel_size=3, padding='same')
  - MaxPooling2D(2)
  - Flatten()
  - Dense(128, activation='relu')
  - Dropout(0.5)
  - Dense(10, activation='softmax')
 self.model = None
 
 def load_and_preprocess_data(self):
  TODO: Загрузить Fashion-MNIST
  Нормализовать пиксели на диапазон [0, 1]
  Добавить размерность канала: (28, 28) -> (28, 28, 1)
 pass
 
 def create_data_augmentation(self):
  TODO: Создать pipeline data augmentation
 - RandomRotation(0.1)
 - RandomZoom(0.1)
 - RandomTranslation(0.1, 0.1)
 pass
43
 
 def compile_model(self):
 TODO: Скомпилировать модель
 Optimizer: Adam
  Loss: categorical_crossentropy
Metrics: accuracy
 pass
 
 def train(self, X_train, y_train, epochs=10, batch_size=32):
 TODO: Обучить модель с augmentation
 Использовать validation_split=0.2
 pass
 
 def evaluate(self, X_test, y_test):
 TODO: Оценить точность на тестовой выборке
 pass
 Что нужно дополнить:
1. Создание слоёв Conv2D и MaxPooling2D
2. Pipeline аугментации данных
3. Компиляцию и обучение модели
4. Визуализацию predictions и ошибок
5. Анализ характеристик фильтров (filters visualization)




# Алгоритм работы нейронной сети по блокам:

АЛГОРИТМ РАБОТЫ CNN ДЛЯ CLASSIFICATION FASHION-MNIST:

1. ВХОДНЫЕ ДАННЫЕ:
   - Изображение 28x28 пикселей, 1 канал (grayscale)
   - Пиксели нормализованы [0, 1]

2. DATA AUGMENTATION (ПРЕДОБРАБОТКА):
   - RandomRotation: случайный поворот ±10%
   - RandomZoom: случайное увеличение/уменьшение ±10%
   - RandomTranslation: случайный сдвиг по осям X и Y ±10%

3. БЛОК 1: СВЕРТОЧНЫЙ СЛОЙ 1
   - Conv2D с 32 фильтрами 3x3
   - Padding='same' (сохранение размерности)
   - Функция активации: ReLU
   - Вычисление: ∑(фильтр * входной патч) + bias
   - Результат: 32 карты признаков размером 28x28

4. БЛОК 2: POOLING СЛОЙ 1
   - MaxPooling2D с окном 2x2
   - Операция: выбор максимального значения в окне
   - Цель: уменьшение размерности, инвариантность к смещениям
   - Результат: 32 карты признаков размером 14x14

5. БЛОК 3: СВЕРТОЧНЫЙ СЛОЙ 2
   - Conv2D с 64 фильтрами 3x3
   - Padding='same'
   - Активация: ReLU
   - Обнаружение более сложных признаков
   - Результат: 64 карты признаков размером 14x14

6. БЛОК 4: POOLING СЛОЙ 2
   - MaxPooling2D с окном 2x2
   - Результат: 64 карты признаков размером 7x7

7. БЛОК 5: ВЫПРЯМЛЕНИЕ (FLATTEN)
   - Преобразование 3D-тензора в 1D-вектор
   - Размер: 7 * 7 * 64 = 3136 элементов

8. БЛОК 6: ПОЛНОСВЯЗНЫЙ СЛОЙ
   - Dense с 128 нейронами
   - Активация: ReLU
   - Обучение высокоуровневых признаков

9. БЛОК 7: DROPOUT
   - Отключение 50% случайных нейронов
   - Цель: предотвращение переобучения

10. БЛОК 8: ВЫХОДНОЙ СЛОЙ
    - Dense с 10 нейронами (по числу классов)
    - Активация: softmax
    - Вычисление вероятностей для каждого класса

11. ОБУЧЕНИЕ:
    - Оптимизатор: Adam (adaptive moment estimation)
    - Функция потерь: categorical crossentropy
    - Метрика: accuracy

12. ОБРАТНОЕ РАСПРОСТРАНЕНИЕ:
    - Вычисление градиентов через chain rule
    - Обновление весов: w = w - η * ∇L(w)
<img width="1522" height="805" alt="image" src="https://github.com/user-attachments/assets/7abd6dfa-6954-4240-9439-49ead81a1dd6" />
<img width="1605" height="550" alt="image" src="https://github.com/user-attachments/assets/9164786a-344b-41dc-9651-b8efc2c89359" />
<img width="1372" height="489" alt="image" src="https://github.com/user-attachments/assets/fb56f914-422d-4378-975d-62ce8bd67111" />
<img width="1354" height="494" alt="image" src="https://github.com/user-attachments/assets/824678f1-f2a0-44e1-9300-9b576ae8cdbc" />
<img width="788" height="701" alt="image" src="https://github.com/user-attachments/assets/6a50cf3a-18ff-486f-b3f3-b524183c6981" />

Визуализация фильтров первого сверточного слоя:
<img width="1478" height="788" alt="image" src="https://github.com/user-attachments/assets/fa9b5ab3-6143-41aa-892b-c399c77c8dbb" />
<img width="1478" height="789" alt="image" src="https://github.com/user-attachments/assets/0f753a33-7b43-4a40-99b2-973e3c9492ab" />
<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/1564fa65-4e41-48d6-a226-73a8878faf04" />




### 6. Почему алгоритмы во внешней памяти измеряют сложность в операциях I/O, а 
не в сравнениях?
Алгоритмы во внешней памяти (например, работающие с данными на диске) измеряют сложность в операциях ввода-вывода (I/O), а не в сравнениях, по ключевым причинам:

1. **Доминирующая задержка** — операции с диском (чтение/запись) на порядки медленнее операций в памяти (сравнений, вычислений). Время доступа к диску измеряется миллисекундами, тогда как операции в памяти — наносекундами.
2. **Блочный доступ** — данные считываются блоками (страницами), поэтому одна операция I/O переносит много данных за раз. Важнее минимизировать количество обращений к диску, а не отдельные сравнения внутри уже загруженного блока.
3. **Иерархия памяти** — цель в том, чтобы эффективно использовать быструю оперативную память (кеш) и минимизировать обращения к медленной внешней памяти.

Таким образом, **операции I/O становятся узким местом**, и их количество — главный критерий эффективности таких алгоритмов (например, в B-деревьях, внешней сортировке слиянием).

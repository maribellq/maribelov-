Задание 6: CNN для классификации изображений (Fashion-MNIST)
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
 # TODO: Создать модель с conv2d и maxpooling слоями
 # Архитектура:
 # - Conv2D(32, kernel_size=3, padding='same')
 # - MaxPooling2D(2)
 # - Conv2D(64, kernel_size=3, padding='same')
 # - MaxPooling2D(2)
 # - Flatten()
 # - Dense(128, activation='relu')
 # - Dropout(0.5)
 # - Dense(10, activation='softmax')
 self.model = None
 
 def load_and_preprocess_data(self):
 # TODO: Загрузить Fashion-MNIST
 # Нормализовать пиксели на диапазон [0, 1]
 # Добавить размерность канала: (28, 28) -> (28, 28, 1)
 pass
 
 def create_data_augmentation(self):
 # TODO: Создать pipeline data augmentation
 # - RandomRotation(0.1)
 # - RandomZoom(0.1)
 # - RandomTranslation(0.1, 0.1)
 pass
43
 
 def compile_model(self):
 # TODO: Скомпилировать модель
 # Optimizer: Adam
 # Loss: categorical_crossentropy
 # Metrics: accuracy
 pass
 
 def train(self, X_train, y_train, epochs=10, batch_size=32):
 # TODO: Обучить модель с augmentation
 # Использовать validation_split=0.2
 pass
 
 def evaluate(self, X_test, y_test):
 # TODO: Оценить точность на тестовой выборке
 pass
# Что нужно дополнить:
# 1. Создание слоёв Conv2D и MaxPooling2D
# 2. Pipeline аугментации данных
# 3. Компиляцию и обучение модели
# 4. Визуализацию predictions и ошибок
# 5. Анализ характеристик фильтров (filters visualization)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

class FashionMNISTCNN:
    def __init__(self):
        # Создание модели CNN
        self.model = keras.Sequential([
            # Первый сверточный блок
            layers.Conv2D(32, kernel_size=3, padding='same', activation='relu', 
                         input_shape=(28, 28, 1)),
            layers.MaxPooling2D(2),
            
            # Второй сверточный блок
            layers.Conv2D(64, kernel_size=3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            
            # Полносвязные слои
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(10, activation='softmax')
        ])
        
        self.data_augmentation = None
        self.history = None
        
    def load_and_preprocess_data(self):
        """Загрузка и предобработка данных Fashion-MNIST"""
        # Загрузка данных
        (X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
        
        # Нормализация пикселей [0, 255] -> [0, 1]
        X_train = X_train.astype('float32') / 255.0
        X_test = X_test.astype('float32') / 255.0
        
        # Добавление размерности канала: (28, 28) -> (28, 28, 1)
        X_train = X_train.reshape(-1, 28, 28, 1)
        X_test = X_test.reshape(-1, 28, 28, 1)
        
        # One-hot encoding меток
        y_train = keras.utils.to_categorical(y_train, 10)
        y_test = keras.utils.to_categorical(y_test, 10)
        
        return (X_train, y_train), (X_test, y_test)
    
    def create_data_augmentation(self):
        """Создание pipeline для аугментации данных"""
        self.data_augmentation = keras.Sequential([
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
            layers.RandomTranslation(0.1, 0.1),
        ])
        return self.data_augmentation
    
    def compile_model(self):
        """Компиляция модели"""
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
    def train(self, X_train, y_train, epochs=10, batch_size=32):
        """Обучение модели с аугментацией данных"""
        # Создание генератора данных с аугментацией
        train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
        
        def augment_data(x, y):
            x = self.data_augmentation(x, training=True)
            return x, y
        
        train_dataset = train_dataset.map(
            augment_data, 
            num_parallel_calls=tf.data.AUTOTUNE
        )
        
        train_dataset = train_dataset.shuffle(10000).batch(batch_size).prefetch(tf.data.AUTOTUNE)
        
        # Разделение на обучающую и валидационную выборки
        val_size = int(0.2 * len(X_train))
        X_val = X_train[:val_size]
        y_val = y_train[:val_size]
        X_train_final = X_train[val_size:]
        y_train_final = y_train[val_size:]
        
        # Обучение модели
        self.history = self.model.fit(
            train_dataset,
            validation_data=(X_val, y_val),
            epochs=epochs
        )
        
        return self.history
    
    def evaluate(self, X_test, y_test):
        """Оценка модели на тестовой выборке"""
        test_loss, test_acc = self.model.evaluate(X_test, y_test, verbose=0)
        print(f"Test accuracy: {test_acc:.4f}")
        print(f"Test loss: {test_loss:.4f}")
        
        # Получение предсказаний
        y_pred = self.model.predict(X_test)
        y_pred_classes = np.argmax(y_pred, axis=1)
        y_true_classes = np.argmax(y_test, axis=1)
        
        return test_loss, test_acc, y_pred_classes, y_true_classes
    
    def visualize_predictions(self, X_test, y_test, num_images=10):
        """Визуализация предсказаний модели"""
        # Получение предсказаний
        predictions = self.model.predict(X_test[:num_images])
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y_test[:num_images], axis=1)
        
        # Названия классов Fashion-MNIST
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                      'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        
        # Визуализация
        plt.figure(figsize=(15, 5))
        for i in range(num_images):
            plt.subplot(2, 5, i + 1)
            plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
            plt.title(f"True: {class_names[true_classes[i]]}\nPred: {class_names[predicted_classes[i]]}")
            plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def visualize_errors(self, X_test, y_test):
        """Визуализация ошибок классификации"""
        predictions = self.model.predict(X_test)
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y_test, axis=1)
        
        # Поиск ошибок
        errors = np.where(predicted_classes != true_classes)[0]
        
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                      'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        
        # Визуализация первых 10 ошибок
        plt.figure(figsize=(15, 5))
        for i, idx in enumerate(errors[:10]):
            plt.subplot(2, 5, i + 1)
            plt.imshow(X_test[idx].reshape(28, 28), cmap='gray')
            plt.title(f"True: {class_names[true_classes[idx]]}\nPred: {class_names[predicted_classes[idx]]}")
            plt.axis('off')
        plt.suptitle("Примеры ошибок классификации", fontsize=14)
        plt.tight_layout()
        plt.show()
        
        # Матрица ошибок
        cm = confusion_matrix(true_classes, predicted_classes)
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=class_names, yticklabels=class_names)
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()
    
    def visualize_filters(self, layer_index=0):
        """Визуализация фильтров сверточного слоя"""
        # Получение весов первого сверточного слоя
        conv_layer = self.model.layers[layer_index]
        filters, biases = conv_layer.get_weights()
        
        # Нормализация фильтров для визуализации
        f_min, f_max = filters.min(), filters.max()
        filters = (filters - f_min) / (f_max - f_min)
        
        # Визуализация всех 32 фильтров
        n_filters = 32
        fig, axes = plt.subplots(4, 8, figsize=(15, 8))
        axes = axes.ravel()
        
        for i in range(n_filters):
            ax = axes[i]
            # Берем первый канал фильтра (т.к. вход черно-белый)
            ax.imshow(filters[:, :, 0, i], cmap='viridis')
            ax.axis('off')
            ax.set_title(f'Filter {i+1}')
        
        plt.suptitle(f'Фильтры слоя {layer_index} (Conv2D с 32 фильтрами)', fontsize=14)
        plt.tight_layout()
        plt.show()
        
        # Визуализация признаков на примере изображения
        self.visualize_feature_maps(X_sample=None, layer_index=layer_index)
    
    def visualize_feature_maps(self, X_sample=None, layer_index=0):
        """Визуализация карт признаков"""
        if X_sample is None:
            # Загружаем одно изображение для примера
            (X_train, _), _ = keras.datasets.fashion_mnist.load_data()
            X_sample = X_train[0:1].astype('float32') / 255.0
            X_sample = X_sample.reshape(-1, 28, 28, 1)
        
        # Создаем модель для получения выходов промежуточного слоя
        intermediate_model = keras.Model(
            inputs=self.model.inputs,
            outputs=self.model.layers[layer_index].output
        )
        
        # Получаем карты признаков
        feature_maps = intermediate_model.predict(X_sample)
        
        # Визуализация карт признаков
        n_maps = min(32, feature_maps.shape[-1])  # Показываем первые 32 карты
        fig, axes = plt.subplots(4, 8, figsize=(15, 8))
        axes = axes.ravel()
        
        for i in range(n_maps):
            ax = axes[i]
            ax.imshow(feature_maps[0, :, :, i], cmap='viridis')
            ax.axis('off')
            ax.set_title(f'Map {i+1}')
        
        plt.suptitle(f'Карты признаков слоя {layer_index} для примерного изображения', fontsize=14)
        plt.tight_layout()
        plt.show()
    
    def plot_training_history(self):
        """Визуализация истории обучения"""
        if self.history is None:
            print("Модель еще не обучена")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        # График точности
        axes[0].plot(self.history.history['accuracy'], label='Train Accuracy')
        axes[0].plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        axes[0].set_title('Model Accuracy')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True)
        
        # График потерь
        axes[1].plot(self.history.history['loss'], label='Train Loss')
        axes[1].plot(self.history.history['val_loss'], label='Validation Loss')
        axes[1].set_title('Model Loss')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss')
        axes[1].legend()
        axes[1].grid(True)
        
        plt.tight_layout()
        plt.show()

# Пример использования:
def main():
    # Создание и настройка модели
    cnn = FashionMNISTCNN()
    
    # Загрузка данных
    (X_train, y_train), (X_test, y_test) = cnn.load_and_preprocess_data()
    
    # Создание аугментации данных
    cnn.create_data_augmentation()
    
    # Компиляция модели
    cnn.compile_model()
    
    # Обучение модели
    print("Начало обучения...")
    history = cnn.train(X_train, y_train, epochs=15, batch_size=64)
    
    # Оценка модели
    print("\nОценка на тестовой выборке:")
    test_loss, test_acc, y_pred, y_true = cnn.evaluate(X_test, y_test)
    
    # Визуализация результатов
    print("\nВизуализация результатов:")
    
    # История обучения
    cnn.plot_training_history()
    
    # Примеры предсказаний
    cnn.visualize_predictions(X_test, y_test)
    
    # Ошибки классификации
    cnn.visualize_errors(X_test, y_test)
    
    # Визуализация фильтров
    print("Визуализация фильтров первого сверточного слоя:")
    cnn.visualize_filters(layer_index=0)
    
    # Отчет классификации
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=class_names))
    
    # Анализ характеристик фильтров
    print("\nАНАЛИЗ ХАРАКТЕРИСТИК ФИЛЬТРОВ:")
    print("1. Первый Conv2D слой: 32 фильтра 3x3")
    print("2. Каждый фильтр обучается обнаруживать различные низкоуровневые признаки:")
    print("   - Градиенты яркости (edges)")
    print("   - Текстуры ткани")
    print("   - Углы и контуры")
    print("3. Второй Conv2D слой: 64 фильтра 3x3")
    print("   - Комбинирует низкоуровневые признаки в высокоуровневые")
    print("   - Обнаруживает паттерны: карманы, воротники, манжеты и т.д.")

if __name__ == "__main__":

    main()

import numpy as np

# Функция активации (сигмоида)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Производная функции активации
def sigmoid_derivative(x):
    return x * (1 - x)

# Входные данные
input_data = np.array([[0,0,1],
                       [0,1,1],
                       [1,0,1],
                       [1,1,1]])

# Ожидаемые выходные данные
expected_output = np.array([[0],
                            [1],
                            [1],
                            [0]])

np.random.seed(1)

# Инициализация весов случайными значениями
synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Случайные начальные веса: ')
print(synaptic_weights)

# Обучение
for iteration in range(20000):
    
    # Прямое распространение
    input_layer = input_data
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    
    # Обратное распространение
    error = expected_output - outputs
    adjustments = error * sigmoid_derivative(outputs)
    
    # Корректировка весов
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Веса после обучения: ')
print(synaptic_weights)

print('Результат после обучения: ')
print(outputs)

# Тестирование
new_input = np.array([1,1,0])
prediction = sigmoid(np.dot(new_input, synaptic_weights))
print('Предсказание для нового входа [1,1,0]: ')
print(prediction)
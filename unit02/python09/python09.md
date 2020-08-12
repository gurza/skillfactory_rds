# PYTHON-9. Возможности библиотеки Numpy для работы с данными


**Содержание**
1. О чём этот модуль
1. О массивах NumPy
1. Индексирование массивов NumPy


## 9.1 О чём этот модуль
Модуль NumPy (Numerical Python) — 
один из наиболее важных пакетов для выполнения высокопроизводительных научных расчётов.

Он позволяет эффективно работать с числами, одномерными и многомерными массивами:
вычислять стандартные математические функции,
реализовывать алгоритмы линейной алгебры,
работать с генераторами случайных чисел.

Особенность NumPy — выполнение действий с высокой скоростью и потребление небольшого количества ресурсов компьютера.
NumPy — низкоуровневный модуль Python, на его основе построен Pandas.
NumPy не содержит средств высокоуровневого анализа данных, но позволяет ускорить и упростить решение многих базовых
задач, связанных с преобразованием матриц, получением базовой статистики, извлечением индексов элементов.

```python
import numpy as np
```


## 9.2 О массивах NumPy
NumPy — это модуль, предназначенный для эффективных математических действий с разными объектами.
Основным объектом модуля является ndarray (N-dimensional array), или N-мерный массив.

**Создание массива**

Функция array() преобразует вложенные элементы в массив.
Важная особенность массивов NumPy — все хранящиеся в них данные должны относиться только к одному типу. 

```python
import numpy as np


arr1 = np.array([1,2,3,4])

arr2 = np.array([5,6,7,8], dtype = float)
print(arr2.dtype)

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.shape(arr3))  # размерность массива
```

**Массив из Pandas**

В процессе анализа данных возникают ситуации, когда требуется выполнить с данными,
хранящимися в Pandas DataFrame, сложные математические операции. 

```python
import numpy as np
import pandas as pd

df = pd.DataFrame()
x = df.values
print(type(x))
# > numpy.ndarray

my_series = pd.Series([5, 6, 7, 8, 9, 10])
x = my_series.values
print(type(x))
# > array([5,6,7,8,9,10], dtype = int64)
```


**Другие способы создания массива**

```python
import numpy as np

np.empty(5) # одномерный массив из пяти элементов, память для которого выделена, но не инициализирована
np.zeros((10, 7)) # массив размером 10x7, заполненный нулями 
np.ones((3,3,3)) # массив размером 3х3х3, заполненный единицами 
np.eye(3) # единичная матрица (элементы главной диагонали равны 1, остальные — 0) размера 3х3
np.full((3, 5), 3.14)  # массив 3x5 заполненный числом 3.14
np.arange(0, 21, 7)  # одномерный массив, заполненный числами в диапазоне от 0 до 20 с шагом 7
np.linspace(0, 1, 5)  # массив из пяти чисел, равномерно распределённых в интервале между 0 и 1 включительно
np.random.randint(0, 10, (3, 3))  # массив размера 3х3, заполненный случайными числами из диапазона от 0 до 9 (включительно)
```

## 9.3 Индексирование массивов NumPy
Массивы, как и другие итерируемые объекты Python,
позволяют обращаться к отдельным своим элементам с помощью индексов и срезов.

Основные правила:

- индекс первого элемента массива равен 0;
- для обращения к элементу массива по индексу необходимо указать имя переменной,
в которой хранится массив, и индекс в квадратных скобках;
- допускается использование отрицательных индексов;
- для обращения к нескольким идущим подряд элементам массива создаётся срез,
в котором указывается индекс первого элемента среза и индекс элемента, следующего за последним, разделённые двоеточием;
- при создании среза возможно задание шага, в этом случае в срез будут включены не все элементы,
а только отстоящие друг от друга на величину шага.

```python
import numpy as np

# Примеры использования индексов при работе с одномерным массивом
my_array = np.array([x for x in range(10)])
print(my_array[5])
print(my_array[-1])
print(my_array[3:6])
print(my_array[1:8:3])
```

Индексация двумерных массивов имеет следующие особенности

- при указании только одного индекса из массива будет выделена вся строка, соответствующая указанному индексу;
- можно указывать несколько индексов или срезов для каждой из осей.

```python
import numpy as np

# Пример работы с двумерными массивами
my_array = np.array([[1,2,3,4], [10,11,12,13], [45,46,47,48]])
print(my_array[1][2])
print(my_array[1,2])
print(my_array[1:, 1:3])
```

**Важно**

Важное отличие массивов NumPy от списков Python — при изменении среза или отдельных элементов
все изменения касаются не только самого среза, но и падают в исходный массив,
даже если перед внесением изменений срез был сохранён в виде отдельной переменной.
Изначально NumPy проектировался для работы с большими массивами данных,
поэтому при бесконтрольном копировании фрагментов массивов возникли бы проблемы с быстродействием и памятью.

Во всех заданиях используется массив, сгенерированный следующим образом.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])
```

Используйте цикл с параметром для организации вычислений.

**Задание 1**

Чему равна сумма элементов последнего столбца массива? Ответ округлите до двух цифр после запятой:

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

s = 0
for x in big_secret[:,-1]:
    s += x
print(round(s, 2))
# > 3154.33
```

**Задание 2**

Выделите из каждой строки массива big_secret первые 5 элементов.
Чему равна сумма элементов главной диагонали получившейся матрицы?
Округлите ответ до двух цифр после запятой.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

matrix = big_secret[:, :5]
s = 0
for i in range(5):
    s += matrix[i,i]
print(round(s, 2))
#> 121.37
```

**Задание 3**

Выделите из каждой строки массива big_secret последние 5 элементов.
Чему равно произведение элементов главной диагонали получившейся матрицы?
Введите полученный результат без изменений и округлений.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

matrix = big_secret[:, -5:]
res = 1
for i in range(5):
    res *= matrix[i,i]
print(res)
# > 341505315559.2347
```

Продолжим работать с массивом big_secret.
Замените на 1 все элементы, у которых оба индекса нечётные, и на -1 все элементы, у которых оба индекса чётные.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

for i in range(big_secret.shape[0]):
    for j in range(big_secret.shape[1]):
        if i % 2 and j % 2:
            big_secret[i, j] = 1
        if i % 2 == 0 and j % 2 == 0:
            big_secret[i, j] = -1
```

**Задание 4**

Выделите из каждой строки обновлённого массива big_secret первые 5 элементов.
Чему равна сумма элементов главной диагонали получившейся матрицы?
Введите полученный ответ без изменений и округлений.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

for i in range(big_secret.shape[0]):
    for j in range(big_secret.shape[1]):
        if i % 2 and j % 2:
            big_secret[i, j] = 1
        if i % 2 == 0 and j % 2 == 0:
            big_secret[i, j] = -1

matrix = big_secret[:, :5]
s = 0
for i in range(5):
    s += matrix[i, i]
print(s)
# > -1.0
```

**Задание 5**

Выделите из каждой строки обновлённого массива big_secret последние 5 элементов.
Чему равно произведение элементов главной диагонали получившейся матрицы?
Введите полученный результат без изменений и округлений.

```python
import numpy as np

first_line = [x*y for x in range(2, 100, 6) for y in range (7, 1, -2)]
second_line = [x ** 0.5 for x in range(1000, 1101, 2)]
third_line = [x**2 for x in range(51)]

big_secret = np.array([first_line, second_line, third_line, second_line, first_line])

for i in range(big_secret.shape[0]):
    for j in range(big_secret.shape[1]):
        if i % 2 and j % 2:
            big_secret[i, j] = 1
        if i % 2 == 0 and j % 2 == 0:
            big_secret[i, j] = -1

matrix = big_secret[:, -5:]
res = 1
for i in range(5):
    res *= matrix[i, i]
print(res)
# > -1.0
```

# PYTHON-5. Общее знакомство с библиотекой Pandas

Подключение нужных библиотек
```python
import pandas as pd
```


## 5.1 Основные объекты Pandas: Series
Объект Series можно рассматривать как одну колонку таблицы, это одномерный массив.
Доступ к элементам осуществляется с использованием `.loc()` или `.iloc()`.
1. .loc() принимает определённые метки из индекса. В него можно передать как один указатель, так и массив.
1. .loc можно опустить и напрямую писать `data["Первый"]` или `data[["Первый", "Третий"]]`.
1. .iloc принимает на вход порядковые номера элементов Series. В него также можно передавать как одно число, так и массив чисел. 

```python
import pandas as pd


data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
                 index = ["Первый", "Второй", "Третий", "Четвёртый"])

print(data.loc["Первый"])
print(data["Первый"])
print(data.iloc[0])

print(data.loc[["Первый", "Третий"]])
print(data[["Первый", "Третий"]])
print(data.iloc[[0, 2]])
```


# 5.2 Основные объекты Pandas: DataFrame
Объект DataFrame лучше всего представлять себе в виде обычной таблицы.
Столбцами в объекте DataFrame выступают объекты Series, строки которых являются их непосредственными элементами.

```python
import pandas as pd

df_from_dict = pd.DataFrame({
    'col1': [1, 2],
    'col2': [3, 4],
})
df_from_list = pd.DataFrame([[1,2], [3,4]],
                            columns=['col1', 'col2'],
                            index=[0, 1])
```


# 5.3 Основные объекты Pandas: read_csv
Функция `read_csv()` позволяет прочитать csv файл, возвращает объект DataFrame.

Дополнительные полезные параметры функции `read_csv()`
1. sep — разделитель данных, по умолчанию ',',
1. decimal — разделитель числа на целую и дробную часть, по умолчанию '.',
1. names — список с названиями колонок,
1. skiprows — если файл содержит системную информацию, можно просто её пропустить.

См. [официальную документацию](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
```


## 5.4 Получение информации о датафрейме: head и tail
Методы `.head()` или `.tail()` объекта DataFrame показывают первые или последние n строк таблицы, по умолчанию n=5.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
print(football.head(10))
```


## 5.5 Получение информации о датафрейме: info
Метод `.info()` объекта DataFrame возвращает детальную информацию о колонках.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
print(football.info())
```


## 5.6 Получение информации о датафрейме: describe
Метод `describe()` объекта DataFrame показывает основные статистические характеристики данных по каждому числовому признаку (типы int64 и float64):
1. count - число ненулевых (not None) значений,
1. mean - среднее,
1. std - стандартное отклонение,
1. min, max - диапазон,
1. 50% - медиану (0.50 квартиль),
1. 25%, 75% - 0.25 и 0.75 квартили.

По нечисловым признакам, например, по строчным (object) или булевым (bool), метод `describe()` возвращает
1. count - число ненулевых (not None) значений,
1. unique - число уникальных значений,
1. top - самое частое значение,
1. freq - частота самого частого значения.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')

print(football.describe())

# stats for strings properties
print(football.describe(include=['object']))
```

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

Получить доступ к колонке можно следующими способами:
1. `df['column_name']`
1. `df.column_name`


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


## 5.7 Индексация и извлечение данных: статистические методы
Статистические методы объектов DataFrame, Series
1. `max()` - максимальное значение,
1. `min()` - минимальное значение,
1. `mean()` - среднее значение,
1. `sum()` - сумма элементов,
1. `count()` - количество ненулевых элементов,
1. `std()` - стандартное отклонение.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
print(football.std())
print(football['Wage'].std())
```


## 5.8 Извлекаем данные по условиям
Чтобы выбрать данные из объекта DataFrame по определённому условию, нужно передать в квадратных скобках список (объект Siries), состоящий из True, False элементов. 
```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
# Footballers which age > 20
print(football[football.Age > 20])

# Footballers which age > mean
print(football[football.Age > football.Age.mean()])

# Footballers which age < mean or footballers from "FC Barcelona"
print(football[(football.Age < football.Age.mean()) | (football.Club == 'FC Barcelona')])
```

### Задания
**Задание 1**

Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых выше среднего? Ответ округлите до сотых.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
speed = football[football.Wage > football.Wage.mean()].SprintSpeed.mean()
print(round(speed, 2))
# > 67.57
```

**Задание 2**
  
Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых ниже среднего? Ответ округлите до сотых.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
speed = football[football.Wage < football.Wage.mean()].SprintSpeed.mean()
print(round(speed, 2))
# > 62.41
```

**Задание 3**
  
Какую позицию (Position) занимает футболист с самой высокой зарплатой (Wage)?

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
position = football[football.Wage == football.Wage.max()].Position[0]
print(position)
# > RF
```

**Задание 4**
  
Сколько пенальти (Penalties) забили бразильские (Nationality, Brazil) футболисты за период, данные о котором
представлены в датасете?

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
penalties = football[football.Nationality == "Brazil"].Penalties.sum()
print(penalties)
# > 22789
```

**Задание 5**

Укажите средний возраст (Age) игроков, у которых точность удара головой (HeadingAccuracy) > 50.
Ответ округлите до сотых.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
age = football[football.HeadingAccuracy > 50].Age.mean()
print(round(age, 2))
# > 25.59
```

**Задание 6**

Укажите возраст (Age) самого молодого игрока, у которого хладнокровие (Composure) и реакция (Reactions) превышают 90%
от максимального значения, представленного в датасете.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
max_composure = football.Composure.max()
max_reactions = football.Reactions.max()
age = football[(football.Composure > 0.9*max_composure) & (football.Reactions > 0.9*max_reactions)].Age.min()
print(round(age, 2))
# > 24
```

**Задание 7**

Определите, насколько средняя реакция (Reactions) самых взрослых игроков (т.е. игроков, чей возраст (Age) равен
максимальному) больше средней реакции самых молодых игроков. Ответ округлите до сотых.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
mature_reactions = football[football.Age == football.Age.max()].Reactions.mean()
young_reactions = football[football.Age == football.Age.min()].Reactions.mean()
print(round(mature_reactions - young_reactions, 2))
# > 22.64
```

**Задание 8**

Из какой страны (Nationality) происходит больше всего игроков, чья стоимость (Value) превышает среднее значение?

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')
nationalities = football[football.Value > football.Value.mean()].Nationality.value_counts()
print(nationalities.index[0])
# > Spain
```

**Задание 9**

Определите, во сколько раз средняя зарплата (Wage) голкипера (Position, GK) с максимальным значением показателя
"Рефлексы" (GKReflexes) выше средней зарплаты голкипера с максимальным значением  показателя "Владение мячом"
(GKHandling).
Ответ округлите до сотых.

```python
import pandas as pd


football = pd.read_csv('data_sf.csv')

wage1 = football[(football.Position == 'GK') & (football.GKReflexes == football.GKReflexes.max())].Wage.mean()
wage2 = football[(football.Position == 'GK') & (football.GKHandling == football.GKHandling.max())].Wage.mean()
print(round(wage1/wage2, 2))
# > 2.77
```

**Задание 10**

Определите, во сколько раз средняя сила удара (ShotPower) самых агрессивных игроков (игроков с максимальным значением
показателя "Агрессивность" (Aggression)) выше средней силы удара игроков с минимальной агрессией.
Ответ округлите до сотых.

```python
import pandas as pd

football = pd.read_csv('data_sf.csv')
power1 = football[football.Aggression == football.Aggression.max()].ShotPower.mean()
power2 = football[football.Aggression == football.Aggression.min()].ShotPower.mean()
print(round(power1/power2, 2))
# > 2.08
```

# PYTHON-8. Очистка данных

**Содержание**

1. О чём этот модуль
1. Букмекерская контора
1. Введение в блок
1. Разбираемся с log.csv
1. Колонки
1. Формат данных
1. Очистка данных


## 8.1 О чём этот модуль
Как работать с «сырыми» данными, сохраненными в неудобном формате, со странными кодировками и ошибками.


## 8.2 Букмекерская контора
Файлы с данными:
- [log.csv](log.csv)
- [users.csv](users.csv)


## 8.3 Введение в блок
Полезные параметры функции `read_csv()`:

- header = None — загрузить без строки с заголовком,
- skiprows = n — пропустить n строк (часто у документов бывает техническая «шапка»),
- encoding — загрузить в конкретной кодировке,
- na_values — список значений, который нужно заменить на NaN (специальный объект, обозначающий пропущенное значение).


## 8.4 Разбираемся с log.csv
**Задание 1. Разбираемся с log.csv**

Какие данные у нас есть?

```python
import pandas as pd

log = pd.read_csv('log.csv')
log.head()
```

- Идентификатор пользователя
- Время посещения
- Дата посещения
- Размер ставки
- Размер выигрыша
- Простая фильтрация

**Задание 2**

Сделаем так, чтобы Pandas не считал первую строку заголовком.

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None)
log.head()
```


## 8.5 Колонки
Дополниетльный датасет: [sample.csv](sample.csv).

```python
import pandas as pd

df = pd.read_csv('sample.csv')
# Read columns:
print(df.columns)

# Set column names:
df.columns = ['new_col_name1', 'new_col_name2', 'new_col_name3', 'new_col_name4']
```

**Задание 1**

Загрузите файл sample.csv в переменную sample, сохраните колонки в переменную columns.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
columns = sample.columns
```

**Задание 2**
Создайте в sample заголовки колонок так, чтобы там были только маленькие буквы.
Например, вместо 'Age' нужно сделать 'age'.

```python
import pandas as pd

sample = pd.read_csv("sample.csv")
sample.columns = [column.lower() for column in sample.columns]
```

**Задание 3**
Замените в log заголовки колонок на

- user_id
- time
- bet
- win

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
log.head()
``` 


## 8.6 Формат данных
```python
import pandas as pd

users = pd.read_csv('users.csv')
```

**Задание 1**

Посмотрите, какие параметры есть у функции read_csv: в чём может быть ошибка?  
С помощью правильных параметров read_csv загрузите датафрейм.

```python
import pandas as pd

users = pd.read_csv('users.csv', encoding='koi8-r', delimiter='\t')
users.head()
```

**Задание 2**

Прочитайте файл в переменную users. Замените в нём названия колонок на.

- user_id
- email
- geo

```python
import pandas as pd

users = pd.read_csv('users.csv', encoding='koi8-r', delimiter='\t')
users.columns = ['user_id', 'email', 'geo']
users.head()
```

## 8.7 Очистка данных
Изучим данные, а именно:

- формат представления данных,
- ошибки в данных,
- пропущенные значения,
- дубликаты,
- типы данных (числа, строки, даты).

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
print(sample['City'].unique())
print(sample.info())
```

В результате `info()` важен тип данных в колонке (Pandas определяет их автоматически)
и количество ненулевых значений, то есть количество реальных значений, не NaN.

**Задание 1**

Посмотрите все уникальные значения в sample.csv.  
Какие ошибки вы видете в колонке Name?

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
print(sample['Name'].unique())
print(sample.info())
```

- Есть пропущенные значения
- Прочерки вместо фамилии
- Есть фамилии, написанные латиницей

**Задание 2**

Посмотрите, сколько непустых значений в колонке City.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
print(len(sample['City'].unique()))
```

**Задание 3**
Поработаем с log.csv. В колонке user_id есть записи, которые содержат технические ошибки.
Укажите, что записано в поле user_id в строчках с ошибкой.

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
errors = [u for u in log['user_id'] if not u.startswith('Запись пользователя')]
print(errors)
```

## 8.8 Простая фильтрация
Мы нашли ошибки в данных — пора исправлять.

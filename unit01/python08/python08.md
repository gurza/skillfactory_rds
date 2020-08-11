# PYTHON-8. Очистка данных

**Содержание**

1. О чём этот модуль
1. Букмекерская контора
1. Введение в блок
1. Разбираемся с log.csv
1. Колонки
1. Формат данных
1. Очистка данных
1. Функция query
1. Функции str.match и str.contains
1. Преобразование данных


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

sample = pd.read_csv('sample.csv')
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

Отфильтровать датафрейм по условию
```python
import pandas as pd

df = pd.read_csv('sample.csv')
# Отфильтровать датафрейм по условию
print(df[df['column']>100])

# Если условий несколько, то к ним можно применить логические операции
print(df[(df['column_name_1']>100) & (df['column_name_2']<200)])
```

**Задание 1**

Создайте новый датафрейм sample2, в который будут входить только записи о людях в возрасте меньше 30 лет.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample2 = sample[sample['Age']<30]
```

**Задание 2**

Создайте новый датафрейм log_win, в который будут входить только записи, где пользователь выиграл.
Посчитайте, сколько таких записей, и сохраните в переменной win_count.

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id','time', 'bet','win']
log_win = log[log['win'] > 0]
win_count = len(log_win)
```

**Задание 3**

Создайте новый датафрейм sample2, в который будут входить только записи о рабочих младше 30 лет.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample2 = sample[(sample['Age']<30) & (sample['Profession']=='Рабочий')]
```


## 8.9 Функция query
Наиболее мощный и удобный способ проводить фильтрацию — использовать функцию `query()`.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
print(sample.query('Age>20'))
print(sample.query('Age==25'))
print(sample.query('City in ["Рига", "Сочи","Чебоксары", "Сургут"] & 21<Age<50 & Profession!="Менеджер"'))
```

**Задание 1**

С помощью функции query найдите тех, у кого ставка меньше 2000, а выигрыш больше 0.
Сохраните в новый датафрейм log2.

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
log2 = log.query('bet < 2000 & win > 0')
```


## 8.10 Функции str.match и str.contains
Часто приходится фильтровать значения в столбце по соответствию строке или её части.
Для этого есть две полезные функции:

- `str.match('abc')` — ищет строки, которые начинаются c abc,
- `str.contains('abc')` — ищет строки, в которых есть abc.

Обе функции не могут работать с NaN, необходимо использовать параметр `na=False`.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
print(sample.Name.str.match("К", na=False))

# Фильтрация DataFrame 
print(sample[sample.Name.str.match('К', na=False)])

# Значения из DataFrame, которые не соответствуют условию
print(sample[~sample.Name.str.match('К', na=False)])
```

**Задание 1**

Найдите записи, где в городах есть буква «о», и сохраните в переменную sample3.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample3 = sample[sample['City'].str.contains('о', na=False)]
```

**Задание 2**

Найдите записи, где в городах нет буквы "о", и сохраните в переменную sample4.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample4 = sample[~sample['City'].str.contains('о', na=False)]
```

**Задание 3**

Сохраните в переменную new_log датафрейм, из которого удалены записи с ошибкой в поле user_id.

```python
import pandas as pd

log = pd.read_csv('log.csv',header=None)
log.columns = ['user_id','time', 'bet','win']
new_log = log[~log['user_id'].str.match('#error', na=True)]
```


## 8.11 Преобразование данных
Использование функции Apply для преобразования данных.

Apply вызывает свою функцию для каждого элемента колонки. Функции, с которыми работает apply, бывают двух видов:

- лямбда-функции (можно задать внутри apply),
- обычные именные функции (определяются через def).


```python
import pandas as pd

sample = pd.read_csv('sample.csv')
# df.column_name.apply(func)
sample.Age.apply(lambda x: x**2)
```

**Задание 1**
С помощью apply и лямбда-функции увеличьте возраст во всех записях на 1 год и сохраните в sample2.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample2 = sample
sample2['Age'] = sample2['Age'].apply(lambda age: age + 1)
```

**Задание 2**

С помощью apply и lambda-функции замените все буквы в поле City на маленькие и сохраните в sample2.
Вам может понадобиться функция s.lower().

Обратите внимание: когда в столбце есть пропущенные значения, необходимо в явном виде указывать, что это str.

```python
import pandas as pd

sample = pd.read_csv('sample.csv')
sample2 = sample
sample2['City'] = sample2['City'].apply(lambda city: str(city).lower())
```

**Задание 3**

Напишите функцию profession_code, которая на вход получает строку, а на выход возвращает

- 0 — если на вход поступила строка "Рабочий",
- 1 — если на вход поступила строка "Менеджер",
- 2 — в любом другом случае.

```python
import pandas as pd


def profession_code(s):
    return {
        'Рабочий': 0,
        'Менеджер': 1,
    }.get(s, 2)


sample = pd.read_csv('sample.csv')
sample2 = sample
sample2['Profession'] = sample2['Profession'].apply(profession_code)
```

**Задание 4**

Примените функцию profession_code для того, чтобы заменить поле Profession с помощью apply.
Сохраните получившийся датафрейм в переменную sample2.

См. листинг решения задачи 3.

**Задание 5**

Напишите функцию age_category, которая на вход получает число, а на выход отдаёт:

- "молодой" — если возраст меньше 23
- "средний" — если возраст от 23 до 35
- "зрелый" — если возраст больше 35

```python
import pandas as pd


def age_category(age):
    if age < 23:
        return 'молодой'
    elif 23 <= age <= 35 :
        return 'средний'
    else:
        return 'зрелый'


sample = pd.read_csv('sample.csv')
sample2 = sample
sample2['Age'] = sample2['Age'].apply(age_category)
```

**Задание 6**

Примените функцию age_category и apply, чтобы создать новую колонку в sample под названием 'Age_category'.
Не забудьте загрузить датафрейм.

```python
import pandas as pd


def age_category(age):
    if age < 23:
        return 'молодой'
    elif 23 <= age <= 35 :
        return 'средний'
    else:
        return 'зрелый'


sample = pd.read_csv('sample.csv')
sample['Age_category'] = sample['Age'].apply(age_category)
```

**Задание 7**

Преобразуем поле user_id в датафрейме log, оставив только идентификатор пользователя.
Например, вместо "Запись пользователя № — user_974" должно остаться только "user_974".

На месте записей с ошибками в user_id должна быть пустая строка "".
Сделайте это через apply и новую функцию, которую вы создадите. Результат сохраните в log.

```python
import pandas as pd


def clear_user_id(s: str):
    prefix = 'Запись пользователя № - '
    clear = s.replace(prefix, '')
    if clear != s:
        return clear
    return ''


log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id','time','bet','win']
log['user_id'] = log['user_id'].apply(clear_user_id)
```

**Задание 8**

Загрузите log.csv в log. Удалите квадратную скобку из первой строки в столбце time,
чтобы привести его к более привычному формату: t равен log.time[0].
Сохраните результат в t.

```python
import pandas as pd

log = pd.read_csv('log.csv', header=None) 
log.columns = ['user_id','time','bet','win']
t = log.time[0]
t = t[1:]
```

**Задание 9**

Уберите ненужную скобку "[" из поля в time. Результат сохраните в log.

```python
import pandas as pd


def clear_time(s):
    if not isinstance(s, str):
        return s
    return s[1:]


log = pd.read_csv('log.csv', header=None)
log.columns = ['user_id','time','bet','win']
log.time = log.time.apply(clear_time)
```

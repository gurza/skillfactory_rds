# PYTHON-6. Методы группировки данных

## 6.1 Что такое группировка данных
Данные можно представить себе как последовательность каких-то единичных наблюдений.
В нашем датасете (data_sd.csv) наблюдение - это конкретный футболист.

У каждого наблюдения есть какие-то признаки (атрибуты), они могут быть разных типов: 
1. категориальные (номинативные) — например, сборная, за которую играет футболист (признак Nationality),
1. численные (количесственные) — например, возраст футболиста (признак Age).

Решение задачи группировки предполагает разделение данных по некоторому признаку (атрибуту),
после чего к каждому элементу этих разделенных данных мы можем применить агрегирующую операцию.
Затем мы можем оценить, как отличаются эти показатели в зависимости от признака,
по которому было осуществлено разделение.
Такое разделение называется **группировкой данных**.


## 6.2 Подсчет количества по группам
Возьмем небольшой фрагмент из исходного датафрейма

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
small_df = df[df.columns[1:8]].head(25)
```

Больше в этом разделе ничего делать не будем.


## 6.3 Функция value_counts
Функция `value_counts()` (метод Series) подсчитывает для каждого значения в серии количество раз,
которое это значение встречается.
Возвращаемое значение - серия.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
small_df = df[df.columns[1:8]].head(25)
s = small_df['Nationality'].value_counts()

print('Сборная, у которой больше всего футболистов, - это', s.index[0])
print('Кол-во национальностей, которые встречаются в датасете small_df, -', len(s.index))
print('Кол-во футболистов из сборной Германии -', s.loc['Germany'])
print('Кол-во футболистов из сборной Германии -', s['Germany'])
print('Сборные, в которых больше одного футболиста:', s.loc[s>1], sep='\n')
print('Сборные, в которых больше одного футболиста:', s[s>1], sep='\n')
```

### Задания
**Задание 1**

Сколько футбольных клубов представлено в датасете?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
clubs = df['Club'].value_counts()
print(len(clubs.index))
# > 650
```

**Задание 2**

Отметьте названия футбольных клубов, представленных в датасете наибольшим количеством игроков.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
clubs = df['Club'].value_counts()
print(clubs[clubs == clubs.max()].index)
# > Index(['Shonan Bellmare', 'V-Varen Nagasaki'], dtype='object')
```

**Задание 3**

Как называется футбольный клуб, представленный наименьшим количеством игроков в датасете?  
Данные о скольких игроках этого клуба имеются в датасете?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
clubs = df['Club'].value_counts()
print(clubs.index[-1])
print(clubs[clubs.index[-1]])
# > Atlético Mineiro
# > 6
```

## 6.4 Подсчет количества значений в процентах и по численным признакам
Можно посчитать количество значений не в абсолютных числах, а в процентах от общего числа в серии.
Для этого надо вызвать метод `value_counts()` с параметром `normalize=True`.

Параметр `bins` метода `value_counts()` удобно использовать, когда мы хотим сгруппировать данные
не по категориальному признаку (каким, например, является национальность),
а по численному признаку (например, по возрасту).
Параметр `bins` позволяет разбить диапазон значений на равные промежутки.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
print(df['Nationality'].value_counts(normalize=True))

# Разобьем весь возможный диапазон зарплат на 4 равных промежутка
s = df['Wage'].value_counts(bins=4)
print(s)
# > Name: Nationality, Length: 156, dtype: float64
# > (435.999, 142000.0]     12818
# > (142000.0, 283000.0]       61
# > (283000.0, 424000.0]       16
# > (424000.0, 565000.0]        2
# Футболисты, которые получают самую большую зарплату (=входят в 3-ий промежуток)
print(df.loc[(df['Wage'] > s.index[3].left) & (df['Wage'] <= s.index[3].right)])
# > Name: Wage, dtype: int64
# >    Unnamed: 0       Name  Age Nationality          Club      Value  ...  SlidingTackle GKDiving  GKHandling  GKKicking  GKPositioning  GKReflexes
# > 0           0   L. Messi   31   Argentina  FC Barcelona  110500000  ...             26        6          11         15             14           8
# > 7           7  L. Suárez   31     Uruguay  FC Barcelona   80000000  ...             38       27          25         31             33          37
# > 
# > [2 rows x 42 columns]
```

## Задания
**Задание 1**

Данные об игроках каких позиций (Position) занимают более 10% датасета?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
positions = df['Position'].value_counts(normalize=True)
print(positions[positions>0.10].index)
# > Index(['GK', 'ST', 'CB'], dtype='object')
```

**Задание 2**

Данные об игроках каких позиций (Position) занимают менее 1% датасета?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
positions = df['Position'].value_counts(normalize=True)
print(positions[positions<0.01].index)
# > Index(['LS', 'RS', 'RWB', 'LWB', 'CF', 'LF', 'RF', 'LAM', 'RAM'], dtype='object')
```

**Задание 3**

В каких пределах находятся худшие 20% показателей точности ударов ногой (FKAccuracy)?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
fk_accuracy = df['FKAccuracy'].value_counts(bins=5, sort=False)
print(fk_accuracy.index[0].left, fk_accuracy.index[0].right)
```

**Задание 4**

Какие показатели точности ударов ногой демонстрирует большинство футболистов?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
fk_accuracy = df['FKAccuracy'].value_counts(bins=5)
print(fk_accuracy.index[0].left, fk_accuracy.index[0].right)
```

# 6.5 Функции unique и nunique и преобразование серии value_counts в датафрейм
Метод `unique()` объекта Series возвращает список уникальных элементов из серии.
Метод `nunique()` объекта Series возвращает количество уникальных значений в серии.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
# Список сборных
print(df['Nationality'].unique())
# > ['Argentina' 'Portugal' 'Brazil' ... 'Indonesia' 'Botswana']

# Количество сборных
print(len(df['Nationality'].unique()))
print(df['Nationality'].nunique())
# > 156
```

Иногда бывает полезно преобразовать серию, получившуюся в результате работы функции value_counts, в датафрейм.
Для этого нужно у получившейся серии вызвать метод `reset_index()`.
```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df['Nationality'].value_counts()
s_df = s.reset_index()
print(type(s_df))
# > <class 'pandas.core.frame.DataFrame'>
print(s_df)
# >                     index  Nationality
# > 0                 England         1368
# > 1                 Germany          919
# > 2                   Spain          671
# > 3                  France          614
# > 4               Argentina          574
# > ..                    ...          ...
# > 151           Philippines            1
# > 152                Jordan            1
# > 153  Central African Rep.            1
# > 154              St Lucia            1
# > 155              Ethiopia            1
# > 
# > [156 rows x 2 columns]

s_df.columns = ['Nationality','Players Count']  # переименовать столбцы
print(s_df)
# >      Nationality  Players Count
# > 0        England           1368
# > 1        Germany            919
# > 2          Spain            671
# > 3         France            614
# > 4      Argentina            574
# > ..           ...            ...
# > 151     Botswana              1
# > 152     Ethiopia              1
# > 153      Grenada              1
# > 154     St Lucia              1
# > 155  South Sudan              1
# > 
# > [156 rows x 2 columns]
```
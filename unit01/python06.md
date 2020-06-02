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

### Задания
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


## 6.6 Задачи
**Задача 1**

У какого процента испанских специалистов (Nationality = 'Spain') зарплата (Wage) находится в пределах 25% минимума
от наблюдаемого уровня зарплат?
Ответ дайте в виде целого числа (округлите полученный результат) без знака %.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.loc[df['Nationality'] == 'Spain']['Wage'].value_counts(normalize=True, bins=4, sort=False)
print(int(round(s[s.index[0]]*100, 0)))
# > 97
```

**Задача 2**

Укажите количество уникальных сборных (Nationality), к которым относятся футболисты,
выступающие за клуб (Club) "Manchester United".

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
result = df.loc[df['Club'] == 'Manchester United']['Nationality'].nunique()
print(result)
# > 13
```

**Задача 3**

С помощью функции unique определите двух футболистов из Бразилии (Nationality = 'Brazil'),
выступающих за клуб (Club) 'Juventus'.
Перечислите их имена (Name, как в датафрейме) через запятую в алфавитном порядке.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
names = df.loc[(df['Nationality'] == 'Brazil') & (df['Club'] == 'Juventus')]['Name'].unique()
print(sorted(names))
# > Alex Sandro,Douglas Costa
```

**Задача 4**

Укажите, какой из клубов (Club) насчитывает большее количество футболистов возрастом (Age) старше 35 лет.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.loc[df['Age'] > 35]['Club'].value_counts()
print(s.index[0])
# > Club Atlético Huracán
```

**Задача 5**

С помощью функции value_counts с параметром bins разбейте всех футболистов сборной (Nationality) Аргентины ('Argentina')
на 4 равные группы.
Укажите, сколько футболистов в возрасте от 34.75 до 41 года в сборной Аргентины.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.loc[df['Nationality'] == 'Argentina']['Age'].value_counts(bins=4)
i = pd.Interval(left=34.75, right=41.0)
print(s[i])
# > 49
```

**Задача 6**

Сколько процентов футболистов из Испании (Nationality = 'Spain') имеют возраст (Age) 21 год?
Введите с точностью до 2 знаков после запятой без указания знака % (например, 12.35).

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
cnt_spain = df.loc[df['Nationality'] == 'Spain']['Name'].count()
cnt_spain_21 = df.loc[(df['Nationality'] == 'Spain') & (df['Age'] == 21)]['Name'].count()
print(round(cnt_spain_21/cnt_spain*100, 2))
# > 11.77
```


## 6.7 Функция groupby
Перед нами стоит задача посчитать сумму зарплат по клубам, чтобы найти клуб с самой высокой зарплатой.
Для решения будем использовать метод `group_by()` объектов DataFrame и Siries.

На вход функции `groupby()` подается список с названием колонкок, по которым будет осуществляться группировка.
Функция `group_by()` возвращает объект группировки, который хранит в себе информацию о том,
какие строки датафрейма (по индексным номерам) соответствуют определенной группе.

К объекту группировки можно применить агрегирующие функции.
В результате получится датафрейм:
* строки (index) - группы,
* столбцы (column) - агрегированное значения параметров, к которым можно было применить агрегирующую функцию.  
 
```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
grouped_df = df.groupby(['Club']).sum()
print(grouped_df)
# >                        Unnamed: 0  Age     Value    Wage  Crossing  ...  GKDiving  GKHandling  GKKicking  GKPositioning  GKReflexes
# > Club                                                                ...                                                            
# >  SSV Jahn Regensburg       129124  609  15195000   90000      1104  ...       405         406        368            409         424
# > 1. FC Heidenheim 1846      117834  473  18290000   76000       961  ...       335         317        287            335         306
# > 1. FC Kaiserslautern       167351  544  11195000   33000      1106  ...       392         373        348            368         356
# ...
# [650 rows x 38 columns]

grouped_df = df.groupby(['Club'])['Wage'].sum()
print(type(grouped_df))
# > <class 'pandas.core.series.Series'>
print(grouped_df)
# > Club
# >  SSV Jahn Regensburg      90000
# > 1. FC Heidenheim 1846     76000
# > 1. FC Kaiserslautern      33000
# > 1. FC Köln                92000
# > 1. FC Magdeburg           84000
# >                           ...  
# > Zagłębie Sosnowiec        27000
# > Çaykur Rizespor          118000
# > Örebro SK                 36000
# > Östersunds FK             39000
# > Śląsk Wrocław             50000
# > Name: Wage, Length: 650, dtype: int64

grouped_df = df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)
print(grouped_df.head(5))
# > Club
# > Real Madrid          4138000
# > FC Barcelona         3967000
# > Manchester City      3097000
# > Manchester United    2357000
# > Juventus             2335000
# > Name: Wage, dtype: int64
```

### Задания
**Задание 1**

Отметьте позиции (Position), по которым общая сумма зарплат (Wage) игроков превышает 5 млн евро в год.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.groupby(['Position'])['Wage'].sum().sort_values(ascending=False)
print(s.loc[s > 5000000].index)
# > Index(['ST', 'GK', 'CB', 'CM', 'LB', 'CAM', 'LM', 'RM', 'RB'], dtype='object', name='Position')
```


## 6.8 Ещё примеры группировки
Построим такую таблицу, где сгруппируем игроков по национальностям (Nationality)
и посчитаем среднюю зарплату, средний возраст и среднюю силу удара.

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False)
print(s.head(10))
# >                             Wage        Age  ShotPower
# > Nationality                                           
# > Dominican Republic  71000.000000  23.000000  75.500000
# > Egypt               35545.454545  25.818182  59.363636
# > Gabon               28900.000000  26.400000  56.900000
# > Croatia             26722.222222  24.819444  54.305556
# > Equatorial Guinea   25666.666667  28.000000  55.333333
# > Belgium             20024.390244  24.030488  56.390244
# > Ecuador             18333.333333  24.619048  60.666667
# > Uruguay             17590.361446  26.771084  56.192771
# > Brazil              17371.158392  27.898345  58.203310
# > Algeria             15810.810811  27.027027  56.567568
```

### Задания
**Задание 1**

Посчитайте среднюю зарплату (Wage) и цену (Value) игроков разных позиций (Position).  
Представители какой позиции имеют самую высокую среднюю цену?  
Какова средняя зарплата футболистов на данной позиции?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.groupby(['Position'])[['Wage', 'Value']].mean().sort_values(['Value'], ascending=False)
print(s.index[0])
print(int(s['Wage'][s.index[0]]))
```


## 6.9 Другие агрегирующие функции
Функция `nunique()` позволяет посчитать количество уникальных значений по серии.
Её лучше всего применять к тем колонкам датафрейма, в которых хранятся категорийные данные.

Функция `count()` позволяет посчитать можно посчитать количество элементов в группе.
```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
# the same result
print(df['Club'].value_counts())
print(df.groupby(['Club'])['Name'].count().sort_values(ascending=False))
```

Функция `median()` позволяет посчитать медианное значение.

Функция `max()` позволяет посчитать максимальное значение внутри группы.

Функция `min()` позволяет посчитать максимальное минимальное внутри группы.

### Задания
**Задание 1**

Посчитайте среднюю (mean) и медианную (median) зарплату (Wage) футболистов из разных клубов (Club).
В скольких клубах средняя и медианная зарплаты совпадают?

Решение без подсказки.
```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s_mean = df.groupby(['Club'])['Wage'].mean()
s_median = df.groupby(['Club'])['Wage'].median()

cnt = 0
for club in s_mean.index:
    if s_mean[club] == s_median[club]:
        cnt += 1

print(cnt)
# > 52
```

**Подсказка**: чтобы в процессе группировки применить к данным одновременно две агрегирующие функции,
необходимо указать их как аргументы метода agg:
```python
# df.groupby(столбец_для_группировки)[столбцы_для_отображения].agg(['функция_1', 'функция_2'])
```

Решение с подсказкой.
```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.groupby(['Club'])['Wage'].agg(['mean', 'median'])
print(len(s.loc[s['mean'] == s['median']]))
# > 52
```

**Задание 2**

Продолжаем работать с клубами, в которых средняя зарплата совпадает с медианной.  
Каков максимальный размер средней зарплаты в этой группе клубов?  
Как называется клуб, где игроки получают такую зарплату?

```python
import pandas as pd


df = pd.read_csv('data_sf.csv')
s = df.groupby(['Club'])['Wage'].agg(['mean', 'median'])
s =  s.loc[s['mean'] == s['median']]
club = s.sort_values(['mean'], ascending=False).index[0]
print(int(s['mean'][club]))
print(club)
# > 13000
# > Cruzeiro
```

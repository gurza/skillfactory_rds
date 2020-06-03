# PYTHON-7. Объединение таблиц

## 7.1 Цели и ожидаемые результаты
В этом модуле мы познакомимся с объединением датафреймов и работой с множеством файлов.
На практике источники данных редко ограничиваются одной таблицей.  Что делать, если надо объединить несколько?

1. merge - аналог SQL Join, позволяет аналогичным образом объединять датафреймы, используя для объединения один
или несколько общих столбцов таблиц.
1. Python имеет простые и удобные инструменты для обхода папок и импорта выгрузок в единый датафрейм,
что существенно облегчает работу с данными 


## 7.2 С какими данными работаем
**ratings.csv** - данные о выставленных оценках фильмов.
* userId — идентификатор пользователя, который поставил фильму оценку,
* movieId — идентификатор фильма,
* rating — выставленная оценка,
* timestamp — время (в формате unix time), когда была выставлена оценка.

**movies.csv** - расшифровка идентификаторов фильмов.
* movieId — идентификатор фильма,
* title — название фильма,
* genres — список жанров, к которым относится фильм.


## 7.3 Тестовые вопросы
```python
import pandas as pd


df_ratings = pd.read_csv('ratings.csv')
print('Количество строк в файле рейтингов:', df_ratings['rating'].count())
print('Минимальная оценка:', df_ratings['rating'].min())
print('Максимальная оценка:', df_ratings['rating'].max())
```


## 7.4 Структура и требования
Полезные ссылки:
1. [Пример режимов склейки таблиц](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)
1. [Документация по методу merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)
1. [Объяснение SQL объединений JOIN: LEFT/RIGHT/INNER/OUTER](http://www.skillz.ru/dev/php/article-Obyasnenie_SQL_obedinenii_JOIN_INNER_OUTER.html)


# 7.5 Зачем хранить информацию в разных таблицах
1. Часто данные формируются несколькими независимыми процессами, каждый из которых хранит данные в своей таблице.
Например, данные для отчета по продажам могут состоять из списка банковских транзакций, курсов валют от Центробанка
и планов отдела продаж из внутренней CRM. 
1. Хранить все данные в одной таблице часто очень накладно для ёмкости диска.
Например, названия фильмов в наших данных хранятся в отдельной небольшой таблице. А в логах, которые могут
растягиваться на многие миллионы строк, вместо названия фильма стоит его идентификатор. Числовой идентификатор фильма
занимает на диске гораздо меньше места, чем длинное название.


## 7.6 Информация про данные
```python
import pandas as pd


df_movies = pd.read_csv('movies.csv')
print('Количество фильмов в таблице movies:', df_movies['movieId'].count())
```


## 7.7 Объединяем таблицы
У датафреймов ratings и movies есть общий столбец movieId.
Мы можем объединить эти датафреймы в одну таблицу по этому столбцу. 

```python
import pandas as pd


ratins = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
joined = ratins.merge(movies, on='movieId', how='left')
print(joined)
```

Схематично `joined = left_df.merge(right_df, on='', how='')`

**how** - параметр объединения записей. Он может иметь четыре значения: left, right, inner и outer.  
При значении left берем все записи (movieId) из "левого" датафрейма (ratings) и ищем их соответствия в "правом" (movies).
В итоговом датафрейме останутся только те значения, которым были найдены соответствия, то есть только значения из ratings.
Аналогично при параметре right остаются только значения из "правого" датафрейма.
Если совпадений между таблицами нет, то ставим нулевое значение.
Значение inner оставляет только те записи (movieId), которые есть в обоих датафреймах, outer объединяет все варианты movieId в обоих датафреймах.


## 7.8 Трудности объединения датафреймов
Объединение датафреймов с помощью метода merge имеет особенности, аналогичные SQL JOIN.
Если точнее, есть ситуации, которые приводят к дублированию строк в конечном результате.


## 7.9 Дубликаты строк
Для удаления дубликатов в датафрейме (таблице) используется метод `drop_duplicates()`.
Рассмотрим его параметры.
* **subset** - один или несколько столбцов, по комбинации которых хотим удалить дубликаты,
* **keep** - указываем, какой из встречающихся дубликатов оставить, например, первый или последний,
* **inplace** - True - если изменения нужно сохранить в датафрейме, к которому применяется метод.

```python
import pandas as pd


movies = pd.read_csv('movies.csv')
movies.drop_duplicates(subset='movieId', keep='first', inplace=True)
```


## 7.10 Задания
В этой серии заданий мы разберемся с данными новых поступлений интернет-магазина.

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)
```

**Задание 1**

Объедините получившиеся датафреймы по столбцу item_id с типом outer.  
Определите, модель с каким item_id есть в статистике продаж purchase_df, но не учтена на складе.
Введите ответ в виде целого числа.

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)

joined = items_df.merge(purchase_df, on='item_id', how='outer')
items_na = joined.loc[joined['stock_count'].isna()]['item_id']
for item_id in items_na:
    print(item_id)
# > 103845
```

**Задание 2**

Решите обратную задачу: модель с каким item_id есть на складе, но не имела ни одной продажи?
Введите ответ в виде целого числа.

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)

joined = items_df.merge(purchase_df, on='item_id', how='outer')
items_na = joined.loc[joined['purchase_id'].isna()]['item_id']
for item_id in items_na:
    print(item_id)
# > 312394
```

**Задание 3**

Сформируйте датафрейм merged, в котором в результате объединения purchase_df и items_df останутся модели,
которые учтены на складе и имели продажи.
Сколько всего таких моделей?

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)

merged = items_df.merge(purchase_df, on='item_id', how='inner')
print(len(merged))
# > 9
```

**Задание 4**

Посчитайте объем выручки для каждой модели, которую можно получить, распродав все остатки на складе.
Модель с каким item_id имеет максимальное значение выручки после распродажи остатков?
Ответ дайте в виде целого числа.

Примечание: перемножение столбцов датафрейма можно производить разными способами,
но самый простой - перемножение "в лоб" вида df['col1'] = df['col2'] * df['col3'].
Для присоединения новых данных к датафрейму тоже можно использовать различные методы, включая функцию .append(),
которая позволяет присоединять к датафрейму другой датафрейм, серии или словари.

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)

merged = items_df.merge(purchase_df, on='item_id', how='inner')
merged['revenue'] = merged['stock_count'] * merged['price']
print(merged.loc[merged['revenue'] == merged['revenue'].max()]['item_id'].iloc[0])
# > 382043
```

**Задание 5**

Посчитайте итоговую выручку из прошлого задания по всем моделям. Ответ дайте в виде целого числа.

```python
import pandas as pd


items_dict = {
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
}
items_df = pd.DataFrame(items_dict)

purchase_log = {
    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
}
purchase_df = pd.DataFrame(purchase_log)

merged = items_df.merge(purchase_df, on='item_id', how='inner')
merged['revenue'] = merged['stock_count'] * merged['price']
print(merged['revenue'].sum())
# > 19729490
```


## 7.11 Объединяем выгрузки
Объединить набор файлов в один датафрейм будем с помощью библиотеки **os**.

```python
import os


files = os.listdir('data')
print(files)
# > ['ratings_8.txt', 'ratings_9.txt', 'ratings_10.txt', 'ratings_7.txt', 'ratings_6.txt', 'ratings_4.txt', 'ratings_5.txt', 'ratings_1.txt', 'ratings_2.txt', 'ratings_3.txt']
```


## 7.12 Выгрузка из вложенных файлов
Если бы в папке 'data' содержались вложенные папки, то получить их имена отдельно от названий файлов можно было бы
с помощью метода walk.

```python
import os


for root, dirs, files in os.walk('data'):
    print(root, dirs, files)
# > data ['subdata'] ['ratings_8.txt', 'ratings_9.txt', 'ratings_10.txt', 'ratings_7.txt', 'ratings_6.txt', 'ratings_4.txt', 'ratings_5.txt']
# > data/subdata [] ['ratings_1.txt', 'ratings_2.txt', 'ratings_3.txt']
```


## 7.13 Склеивание датафреймов
Функция `concat()` библиотеки Pandas используется для объединения нескольких датафреймов в один.

```python
import pandas as pd

df1 = pd.read_csv('data/ratings_1.txt')
df2 = pd.read_csv('data/ratings_2.txt')
total_df = pd.concat([df1, df2])
print(total_df)

# axis=1 - чтобы склеить датафрейсы по горизонтали, если у них совпадает кол-во строк
total_df = pd.concat([df1, df2], axis=1)
print(total_df) 
```

### Задание

Напишите цикл, который собирает содержимое файлов папки data в единый датафрейм data.  
Сколько строк в датафрейме data?

```python
import os
import pandas as pd


data = pd.DataFrame(columns=['userId', 'movieId', 'rating', 'timestamp'])
for data_filename in os.listdir('data'):
    temp = pd.read_csv(os.path.join('data', data_filename), names=['userId', 'movieId', 'rating', 'timestamp'])
    data = pd.concat([data, temp])

print(len(data))
# > 100004
```


## 7.15 Тесты
Решение некоторых задач.

**Задание 3**

Сколько раз была выставлена низшая оценка 0.5 в наших рейтингах? Используйте файл ratings.csv.

```python
import pandas as pd


data = pd.read_csv('ratings.csv')
print(len(data.loc[data['rating'] == data['rating'].min()]))
# > 1370
```

**Задание 4**

Объедините датафреймы ratings и movies, используя параметр how='outer'.  
Сколько строк в получившемся датафрейме?

```python
import pandas as pd


ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
joined = ratings.merge(movies, on='movieId', how='outer')
print(len(joined))
# > 100854
```

**Задание 5**

Найдите в датафрейме movies фильм с movieId=3456.  
Какой у него год выпуска?

```python
import re
import pandas as pd


ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
joined = ratings.merge(movies, on='movieId', how='outer')

title = joined.loc[joined['movieId'] == 3456]['title'].iloc[0]
year = re.search(r'\((\d{4})\)$', title).group(1)
year = int(year)
print(year)
```

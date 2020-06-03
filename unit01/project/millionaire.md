# Проект 1. Кто хочет стать миллионером?

Notes
1. Под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма.

IMDB dataset
```python
import pandas as pd


data = pd.read_csv('data.csv')
print(data.info())
# > <class 'pandas.core.frame.DataFrame'>
# > RangeIndex: 1890 entries, 0 to 1889
# > Data columns (total 16 columns):
# >  #   Column                Non-Null Count  Dtype  
# > ---  ------                --------------  -----  
# >  0   imdb_id               1890 non-null   object 
# >  1   popularity            1890 non-null   float64
# >  2   budget                1890 non-null   int64  
# >  3   revenue               1890 non-null   int64  
# >  4   original_title        1890 non-null   object 
# >  5   cast                  1890 non-null   object 
# >  6   director              1890 non-null   object 
# >  7   tagline               1890 non-null   object 
# >  8   overview              1890 non-null   object 
# >  9   runtime               1890 non-null   int64  
# >  10  genres                1890 non-null   object 
# >  11  production_companies  1890 non-null   object 
# >  12  release_date          1890 non-null   object 
# >  13  vote_count            1890 non-null   int64  
# >  14  vote_average          1890 non-null   float64
# >  15  release_year          1890 non-null   int64  
# > dtypes: float64(2), int64(5), object(9)
# > memory usage: 236.4+ KB
# > None
```

**Вопрос 1**                                    
                                                
У какого фильма из списка самый большой бюджет?

```python
import pandas as pd


data = pd.read_csv('data.csv')
movie_biggest_budget = data.loc[data['budget'] == data['budget'].max()]
print('{title} ({id})'.format(
    title=movie_biggest_budget['original_title'].iloc[0], id=movie_biggest_budget['imdb_id'].iloc[0]))
# > The Warrior's Way (tt1032751)
```

---

**Вопрос 2**

Какой из фильмов самый длительный (в минутах)?

```python
import pandas as pd


data = pd.read_csv('data.csv')
movie_max_runtime = data.loc[data['runtime'] == data['runtime'].max()]
print('{title} ({id}) - {runtime} minutes'.format(
    title=movie_max_runtime['original_title'].iloc[0], id=movie_max_runtime['imdb_id'].iloc[0],
    runtime=movie_max_runtime['runtime'].iloc[0]))
# > Gods and Generals (tt0279111) - 214 minutes
```

---

**Вопрос 3**

Какой из фильмов самый короткий (в минутах)?

```python
import pandas as pd


data = pd.read_csv('data.csv')
movie_min_runtime = data.loc[data['runtime'] == data['runtime'].min()]
print('{title} ({id}) - {runtime} minutes'.format(
    title=movie_min_runtime['original_title'].iloc[0], id=movie_min_runtime['imdb_id'].iloc[0],
    runtime=movie_min_runtime['runtime'].iloc[0]))
# > Winnie the Pooh (tt1449283) - 63 minutes
```

---

**Вопрос 4**

Какое число ближе к средней длительности фильма в датасете?

```python
import pandas as pd


data = pd.read_csv('data.csv')
runtime_mean = data['runtime'].mean()

answers = [i for i in range(100, 125, 5)]
d = None
answer_correct = None
for answer in answers:
    if d is None or abs(runtime_mean - answer) < d:
        answer_correct = answer
        d = abs(runtime_mean - answer)
print('Mean runtime:', runtime_mean)
print('Answer:', answer_correct)
# > Mean runtime: 109.65343915343915
# > Answer: 110
```

---

**Вопрос 5**

Какое число ближе к медианной длительности фильма в датасете?

```python
import pandas as pd


data = pd.read_csv('data.csv')
runtime_median = data['runtime'].median()

answers = [106, 112, 101, 120, 115]
d = None
answer_correct = None
for answer in answers:
    if d is None or abs(runtime_median - answer) < d:
        answer_correct = answer
        d = abs(runtime_median - answer)
print('Median runtime:', runtime_median)
print('Answer:', answer_correct)
# > Median runtime: 106.5
# > Answer: 106
```

---

**Вопрос 6**

Какой самый прибыльный фильм?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movie_most_profitable = data[data['profit'] == data['profit'].max()]
print(movie_most_profitable)
print('{title} {id} - {profit}'.format(
    title=movie_most_profitable['original_title'].iloc[0], id=movie_most_profitable['imdb_id'].iloc[0],
    profit=movie_most_profitable['profit'].iloc[0]
))
# > Avatar tt0499549 - 2544505847
```

---

**Вопрос 7**

Какой фильм самый убыточный?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movie_most_unprofitable = data[data['profit'] == data['profit'].min()]
print(movie_most_unprofitable)
print('{title} {id} - {profit}'.format(
    title=movie_most_unprofitable['original_title'].iloc[0], id=movie_most_unprofitable['imdb_id'].iloc[0],
    profit=movie_most_unprofitable['profit'].iloc[0]
))
# > The Warrior's Way tt1032751 - -413912431
```

---

**Вопрос 8**

У скольких фильмов из датасета объем сборов оказался выше бюджета?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies = data.loc[data['profit'] > 0]
print(len(movies))
# > 1478
```
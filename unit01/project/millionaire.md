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

---

**Вопрос 9**

Какой фильм оказался самым кассовым в 2008 году?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies_2008 = data.loc[data['release_year'] == 2008]
movie = movies_2008.loc[movies_2008['profit'] == movies_2008['profit'].max()]
print('{title} {id} - {profit}'.format(
    title=movie['original_title'].iloc[0], id=movie['imdb_id'].iloc[0],
    profit=movie['profit'].iloc[0]
))
# > The Dark Knight tt0468569 - 816921825
```

---

**Вопрос 10**

Самый убыточный фильм за период с 2012 по 2014 гг. (включительно)?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies_selected = data.loc[(data['release_year'] >= 2012) & (data['release_year'] <= 2014)]
movie = movies_selected.loc[movies_selected['profit'] == movies_selected['profit'].min()]
print('{title} {id} - {profit}'.format(
    title=movie['original_title'].iloc[0], id=movie['imdb_id'].iloc[0],
    profit=movie['profit'].iloc[0]
))
# > The Lone Ranger tt1210819 - -165710090
```

---

**Вопрос 11**

Какого жанра фильмов больше всего?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
movies_genres = data['genres']
cnt = Counter()
for genre_str in movies_genres:
    for genre in genre_str.split('|'):
        cnt[genre] += 1
genre_most_common = cnt.most_common(1)[0]
print('{genre} - {cnt}'.format(genre=genre_most_common[0], cnt=genre_most_common[1]))
# > Drama - 782
```

---

**Вопрос 12**

Какого жанра среди прибыльных фильмов больше всего?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies_genres = data.loc[data['profit'] > 0]['genres']
cnt = Counter()
for genre_str in movies_genres:
    for genre in genre_str.split('|'):
        cnt[genre] += 1
genre_most_common = cnt.most_common(1)[0]
print('{genre} - {cnt}'.format(genre=genre_most_common[0], cnt=genre_most_common[1]))
# > Drama - 560
```

---

**Вопрос 13**

Кто из режиссеров снял больше всего фильмов?

```python
import pandas as pd


data = pd.read_csv('data.csv')
directors = data['director'].value_counts()
print('{name} - {cnt}'.format(name=directors.index[0], cnt=directors.iloc[0]))
# > Steven Soderbergh - 13
```

---

**Вопрос 14**

Кто из режиссеров снял больше всего прибыльных фильмов?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
directors = data.loc[data['profit'] > 0]['director'].value_counts()
print('{name} - {cnt}'.format(name=directors.index[0], cnt=directors.iloc[0]))
# > Ridley Scott - 12
```

---

**Вопрос 15**

Кто из режиссеров принес больше всего прибыли?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
directors = data.groupby(['director'])['profit'].sum().sort_values(ascending=False)
print('{name} - {cnt}'.format(name=directors.index[0], cnt=directors.iloc[0]))
# > Peter Jackson - 5202593685
```

---

**Вопрос 16**

Какой актер принес больше всего прибыли?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
cnt = Counter()
for movie in data[['cast', 'profit']].values:
    for actor in movie[0].split('|'):
        cnt[actor] += movie[1]
actor_most_profitable = cnt.most_common(1)[0]
print('{name} - {profit}'.format(name=actor_most_profitable[0], profit=actor_most_profitable[1]))
# > Emma Watson - 6666245597
```

---

**Вопрос 17**

Какой актер принес меньше всего прибыли в 2012 году?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies_selected = data.loc[data['release_year'] == 2012][['cast', 'profit']]
cnt = Counter()
for movie in movies_selected.values:
    for actor in movie[0].split('|'):
        cnt[actor] += movie[1]
actor_most_unprofitable = cnt.most_common()[-1]
print('{name} - {profit}'.format(name=actor_most_unprofitable[0], profit=actor_most_unprofitable[1]))
# > Kirsten Dunst - -68109207
```

---

**Вопрос 18**

Какой актер снялся в большем количестве высокобюджетных фильмов?
Примечание: в фильмах, где бюджет выше среднего по данной выборке.

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
selected = data.loc[data['budget'] > data['budget'].mean()]['cast']
cnt = Counter()
for cast_str in selected:
    for actor in cast_str.split('|'):
        cnt[actor] += 1
actor_most_common = cnt.most_common(1)[0]
print('{name} - {cnt}'.format(name=actor_most_common[0], cnt=actor_most_common[1]))
# > Matt Damon - 18
```

---

**Вопрос 19**

В фильмах какого жанра больше всего снимался Nicolas Cage?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
selected = data.loc[data['cast'].str.contains('Nicolas Cage')]['genres']
cnt = Counter()
for genre_str in selected:
    for genre in genre_str.split('|'):
        cnt[genre] += 1
genre_most_common = cnt.most_common(1)[0]
print('{genre} - {cnt}'.format(genre=genre_most_common[0], cnt=genre_most_common[1]))
# > Action - 17
```

---

**Вопрос 20**

Какая студия сняла больше всего фильмов?
```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
production_companies = data['production_companies']
cnt = Counter()
for companies_str in production_companies:
    for company in companies_str.split('|'):
        cnt[company] += 1
company_most_common = cnt.most_common(1)[0]
print('{company} - {cnt}'.format(company=company_most_common[0], cnt=company_most_common[1]))
# > Universal Pictures - 173
```

---

**Вопрос 21**

Какая студия сняла больше всего фильмов в 2015 году?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
production_companies = data.loc[data['release_year'] == 2015]['production_companies']
cnt = Counter()
for companies_str in production_companies:
    for company in companies_str.split('|'):
        cnt[company] += 1
company_most_common = cnt.most_common(1)[0]
print('{company} - {cnt}'.format(company=company_most_common[0], cnt=company_most_common[1]))
# > Warner Bros. - 12
```

---

**Вопрос 22**

Какая студия заработала больше всего денег в жанре комедий за все время?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
selected = data.loc[data['genres'].str.contains('Comedy')][['production_companies', 'profit']]
cnt = Counter()
for row in selected.values:
    for company in row[0].split('|'):
        cnt[company] += row[1]
company_most_common = cnt.most_common(1)[0]
print('{company} - {profit}'.format(company=company_most_common[0], profit=company_most_common[1]))
# > Universal Pictures - 8961545581
```

---

**Вопрос 23**

Какая студия заработала больше всего денег в 2012 году?

```python
from collections import Counter
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
selected = data.loc[data['release_year'] == 2012][['production_companies', 'profit']]
cnt = Counter()
for row in selected.values:
    for company in row[0].split('|'):
        cnt[company] += row[1]
company_most_common = cnt.most_common(1)[0]
print('{company} - {profit}'.format(company=company_most_common[0], profit=company_most_common[1]))
# > Columbia Pictures - 2501406608
```

---

**Вопрос 24**

Самый убыточный фильм от Paramount Pictures?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
movies_paramount = data.loc[data['production_companies'].str.contains('Paramount Pictures')]
print(movies_paramount['production_companies'])
movie_most_unprofitable = movies_paramount.loc[movies_paramount['profit'] == movies_paramount['profit'].min()].iloc[0]
print('{title} {id} - {profit}'.format(
    title=movie_most_unprofitable['original_title'], id=movie_most_unprofitable['imdb_id'],
    profit=movie_most_unprofitable['profit']))
# > K-19: The Widowmaker tt0267626 - -64831034

```

---

**Вопрос 25**

Какой самый прибыльный год (в какой год студии заработали больше всего)?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
selected = data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
year_most_profitable = selected.index[0]
print(year_most_profitable)
# > 2015
```

---

**Вопрос 26**

Какой самый прибыльный год для студии Warner Bros?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['profit'] = data['revenue'] - data['budget']
selected = data.loc[data['production_companies'].str.contains('Warner Bros')].groupby(['release_year'])['profit'].sum()\
    .sort_values(ascending=False)
print(selected)
year_most_profitable = selected.index[0]
print(year_most_profitable)
# > 2014
```

---

**Вопрос 27**

В каком месяце за все годы суммарно вышло больше всего фильмов?

```python
import datetime
import pandas as pd


data = pd.read_csv('data.csv')
data['release_month'] = data['release_date'].apply(lambda dt: datetime.datetime.strptime(dt, "%m/%d/%Y").month)

selected = data['release_month'].value_counts()
month = selected.index[0]
print(datetime.date(1900, month, 1).strftime('%B'))
# > September
```

**Вопрос 28**

Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

```python
import datetime
import pandas as pd


data = pd.read_csv('data.csv')
data['release_month'] = data['release_date'].apply(lambda dt: datetime.datetime.strptime(dt, "%m/%d/%Y").month)

movies_sum = len(data.loc[data['release_month'].isin([6, 7, 8])])
print(movies_sum)
# > 450
```

---

**Вопрос 29**

Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?

```python
import datetime
import pandas as pd


data = pd.read_csv('data.csv')
data['release_month'] = data['release_date'].apply(lambda dt: datetime.datetime.strptime(dt, "%m/%d/%Y").month)

director = data.loc[data['release_month'].isin([11, 12, 1])]['director'].value_counts().head(1)
print('{name} - {cnt}'.format(name=director.index[0], cnt=director.iloc[0]))
# > Peter Jackson - 8
```

---

**Вопрос 31**

Названия фильмов какой студии в среднем самые длинные по количеству символов?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['original_title_length'] = data['original_title'].apply(lambda s: len(s))

selected = data[['production_companies', 'original_title_length']]
temp_list = list()
for movie in selected.values:
    for studio in movie[0].split('|'):
        temp_list.append([studio, movie[1]])
temp = pd.DataFrame(temp_list, columns=['studio', 'original_title_length'])
grouped = temp.groupby(['studio'])['original_title_length'].mean().sort_values(ascending=False)
print('{studio} - {length}'.format(studio=grouped.index[0], length=grouped.iloc[0]))
# > Four By Two Productions - 83.0
```

---

**Вопрос 32**

Названия фильмов какой студии в среднем самые длинные по количеству слов?

```python
import pandas as pd


data = pd.read_csv('data.csv')
data['original_title_words_cnt'] = data['original_title'].apply(lambda s: len(s.split()))

selected = data[['production_companies', 'original_title_words_cnt']]
temp_list = list()
for movie in selected.values:
    for studio in movie[0].split('|'):
        temp_list.append([studio, movie[1]])
temp = pd.DataFrame(temp_list, columns=['studio', 'original_title_words_cnt'])
grouped = temp.groupby(['studio'])['original_title_words_cnt'].mean().sort_values(ascending=False)
print('{studio} - {words_cnt}'.format(studio=grouped.index[0], words_cnt=grouped.iloc[0]))
# > Four By Two Productions - 83.0

print(len(data.loc[data['production_companies'].str.contains('Four By Two Productions')]['original_title']))
# > 1
print(data.loc[data['production_companies'].str.contains('Four By Two Productions')]['original_title'].iloc[0])
# > Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan
```

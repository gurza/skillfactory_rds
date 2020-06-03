# Проект 1. Кто хочет стать миллионером?

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

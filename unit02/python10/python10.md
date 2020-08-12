# PYTHON-10. Методы визуализации данных

**Содержание**

1. Графические возможности Pandas


## 10.1. Графические возможности Pandas
Датасет [tips.csv](tips.csv) содержит информацию о посещениях одного из ресторанов быстрого питания в США в 90-х.

```python
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.head())
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4
```

Датасет содержит семь показателей:

- total_bill — общая сумма, уплаченная за заказ;
- tip — размер чаевых;
- sex — пол клиента;
- smoker — является ли клиент курильщиком (в 90-е годы в ресторанах США были зоны для курящих);
- day — день недели;
- time — время (обед или ужин);
- size — количество посетителей, обедавших за столом.

**Задание 1**

Сколько строк содержится в датафрейме без учёта заголовка?

```python
import pandas as pd

df = pd.read_csv('tips.csv')
print(df.info())
# > 244
```

**Задание 2**

Напишите максимальную сумму счёта в датафрейме. Ответ введите с точностью до двух цифр после запятой, например:100.55.

```python
import pandas as pd

df = pd.read_csv('tips.csv')
print(round(max(df['total_bill']), 2))
# > 50.81
```

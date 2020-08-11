# PYTHON-8. Очистка данных

**Содержание**

1. О чём этот модуль
1. Букмекерская контора
1. Введение в блок


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
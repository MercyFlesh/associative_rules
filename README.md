# Построение ассоциаотивных правил

Программа по расчету ассоциативных правил и правил последовательностей

## Установка и использование

```
git clone https://github.com/MercyFlesh/associative_rules.git
cd associative_rules
python3 main.py -P <csv_database_path> -S <min support> 
```

## Опции

```
optional arguments:
    -h, --help            show this help message and exit
    
Mendatory:
    -P PATH, --path PATH  path to database
    -S SUP, --sup SUP     minimum support

Rule sorting coefficients:
    --conf CONF           minimum confidience
    --lift LIFT           minimum lift
    --levar LEVAR         minimum levarage
    --conv CONV           minimum conviction

Output flags:
    -J, --json            write rules to json file
```

***

**Входные данные:**
Данные в формате CSV, минимум 2 столбца, один из которых — группировочное поле, для ассоциативных правил и 3 столбца для правил последовательностей (группировочное поле + поле последовательности) для обучения. Файл assseqRules.csv

**Выходные данные:**
Результат применения ассоциативных правил к второму набору данных в формате CSV.

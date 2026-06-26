# Викторов Борис Лабораторная 5.

Работа посвящена pyspark.

## Данные: OpenFoodFacts
https://huggingface.co/datasets/openfoodfacts/product-database

## Модель: KMeans

## Структура
```
.
├── config
├── data
└── src

```
Папки:

    config: Хранится yaml файл с конфигурацией pyspark.
    data: Хранится parquet с данными.
    src: Папка для кода модели.
## Запуск
Запуск предполагается из корневой папки.
Сначала загружаются данные, потом делается word count по не None строчкам колонки known_ingredients_n.
Далее делается кластеризация с помощью KMeans на 2 кластера.

    python src/main.py
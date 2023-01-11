# Асинхронный парсер [PEP](https://peps.python.org/)

## Описание:

Парсер документов [документов PEP](https://peps.python.org/) на базе фреймворка Scrapy.
- Собирает актуальную информацию о статусах PEP
- Собирает информацию по количеству каждого статуса
- Выводит информацию в виде CSV файлов

## Технологии:
[Python 3.9](https://www.python.org/downloads/release/python-390/), [Scrapy 2.5.1](https://docs.scrapy.org/en/2.5/topics/api.html)

### Как запустить проект(все команды выполняются в командной оболочке bach):

1. Клонировать репозиторий и перейти в него в командной строке.
2. Создать и активировать виртуальное окружение
3. Установить зависимости командой:
```
pip install -r requirements.txt
```
4. ЗАпустить парсер командой
```
scrapy crawl pep
```

### По итгу работы в папке results появятся два файла с результатами:
- Файл со списком PEP - pep_ДатаВремя.csv, с тремя столбцами: «Номер», «Название» и «Статус»
```
number,name,status
1,PEP Purpose and Guidelines,Active
257,Docstring Conventions,Active
4,Deprecation of Standard Modules,Active
2,Procedure for Adding New Modules,Active
272,API for Block Encryption Algorithms v1.0,Final
287,reStructuredText Docstring Format,Active
290,Code Migration and Modernization,Active
249,Python Database API Specification v2.0,Final
333,Python Web Server Gateway Interface v1.0,Final
291,Backward Compatibility for the Python 2 Standard Library,Final
248,Python Database API Specification v1.0,Final
247,API for Cryptographic Hash Functions,Final
20,The Zen of Python,Active
676,PEP Infrastructure Process,Active
13,Python Language Governance,Active
101,Doing Python Releases 101,Active
8015,Organization of the Python community,Rejected
8014,The Commons Governance Model,Rejected
8013,The External Council Governance Model,Rejected
8012,The Community Governance Model,Rejected
8011,Python Governance Model Lead by Trio of Pythonistas,Rejected
8010,The Technical Leader Governance Model,Rejected
3153,Asynchronous IO support,Superseded
3152,Cofunctions,Rejected
3145,Asynchronous I/O For subprocess.Popen,Withdrawn
3146,Merging Unladen Swallow into CPython,Withdrawn
3142,Add a “while” clause to generator expressions,Rejected
3140,"str(container) should call str(item), not repr(item)",Rejected
3136,Labeled break and continue,Rejected
3133,Introducing Roles,Rejected
3139,Cleaning out sys and the “interpreter” module,Rejected
3130,Access to Current Module/Class/Function,Rejected
3128,BList: A Faster List-like Type,Rejected
3126,Remove Implicit String Concatenation,Rejected
677,Callable Type Syntax,Rejected
3122,Delineation of the main module,Rejected
3125,Remove Backslash Continuation,Rejected
3117,Postfix type declarations,Rejected
690,Lazy Imports,Rejected
754,IEEE 754 Floating Point Special Values,Rejected
3103,A Switch/Case Statement,Rejected
3001,Procedure for reviewing and improving standard library modules,Withdrawn
666,Reject Foolish Indentation,Rejected
665,A file format to list Python dependencies for reproducibility of an application,Rejected
663,"Standardizing Enum str(), repr(), and format() behaviors",Rejected
651,Robust Stack Overflow Handling,Rejected
662,Editable installs via virtual wheels,Rejected
650,Specifying Installer Requirements for Python Projects,Withdrawn
645,Allow writing optional types as ,Withdrawn
```
- Файл со сводкой по статусам - status_summary_ДатаВремя.csv со столбцами«Статус» и «Количество». В последней строке будет общее количество полученных документов PEP.
```
"Статус","Количество"
"Active","37"
"Final","264"
"Rejected","120"
"Superseded","19"
"Withdrawn","55"
"April Fool!","1"
"Deferred","36"
"Draft","30"
"Accepted","40"
"Total","602"
```
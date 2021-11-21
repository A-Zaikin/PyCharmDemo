# PyCharmDemo
Задание от 16.11.2021. Ознакомление с IDE PyCharm

![image](./filter_profiling_result.JPG)<br>
*Время выполнения filter.py*

![image](./old_filter_profiling_result.JPG)<br>
*Время выполнения old_filter.py*

Прирост производительности в 10 раз вызван тем,
что функции из numpy значительно более оптимизированы
по сравнению с реализацией через циклы.

![image](./filter_with_filename_profiling_result.JPG)<br>
*Время выполнения filter_with_filename.py*

Для filter.py в профайлере указаны входные аргументы утилиты, поэтому прирост
производительности в filter_with_filename.py достаточно мал.

![image](./pycharm_doctest_result.JPG)<br>
*Результат выполнения доктестов в PyCharm* 
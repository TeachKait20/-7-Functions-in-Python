# -7-Functions-in-Python
## Функции в Python

Помимо встроенных функций в Python, можно создать и свою собственную. Функции позволяют объединять блоки кода, которые выполняют определенные задачи, и использовать их многократно в разных частях программы. В таком случае ключевое слово `def` используется для определения функции. <br>
Синтаксис:  <br>
```
def имя_функции(параметры):
    """Документация (опционально)"""
    # Тело функции
    # Инструкции
    return результат
```
Компоненты определения функции: <br>
* `def`: Ключевое слово, используемое для объявления новой функции.
* `имя_функции`: Имя функции, которое используется для ее вызова. Должно следовать правилам именования переменных.
* `параметры`: Переменные, которые функция принимает в качестве входных данных. Указываются в скобках. Если параметров нет, скобки остаются пустыми.
* `Документация (опционально)`: Строка, заключенная в тройные кавычки, описывающая, что делает функция.
* `Тело функции`: Блок кода, который выполняется при вызове функции. Он должен быть сдвинут вправо (используя отступы).
* `return`: Оператор, используемый для возврата значения из функции. Если return не указан, функция вернет None.

**Пример функции**
```python
def add(a, b):
    """Возвращает сумму двух чисел."""
    result  = a + b
    return result 

# Вызов функции
print(add.__doc__) # Вызов документации функции
var_summ = add(3, 5) # Передаём значения другой переменной
print(var_summ)  # Выведет: 8
print(add(10, 5)) # Напрямую вызываем функцию. Выведет: 15
```

### Где можно использовать функции?

Рассмотрим ситуацию: Есть компьютерная игра с различными персонажами и диалогами. 

| Header 1 | Header 2 |
|----------|----------|
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/magician.jpg?raw=true">   | Cell 2   |
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/archer.jpg?raw=true">   | Cell 5   |
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/enemy.jpg?raw=true" width="256">   | Cell 8   |


## Аргументы функций
Аргументов (параметров) для функции бывает несколько. Рассмотрим ещё аргументы со значениями по умолчанию.

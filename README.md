# -7-Functions-in-Python
## Функции в Python

<img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/work.gif?raw=true">

Помимо встроенных функций в Python, можно создать и свою собственную. Функции позволяют объединять блоки кода, которые выполняют определенные задачи, и использовать их многократно в разных частях программы. В таком случае ключевое слово `def` используется для определения функции. <br> <br>
Функция в Python — это самостоятельный блок кода, который выполняет определенную задачу. <br> <br>
Синтаксис:  <br>
```
def имя_функции(параметры):
    """Документация (опционально)"""
    # Тело функции
    # Инструкции
    return результат
```
Компоненты определения функции: <br>
* `def`- Ключевое слово, используемое для объявления новой функции.
* `имя_функции`- Имя функции, которое используется для ее вызова. Должно следовать правилам именования переменных.
* `параметры` или `аргументы`- Переменные, которые функция принимает в качестве входных данных. Указываются в скобках. Если параметров нет, скобки остаются пустыми.
* `Документация (опционально)`- Строка, заключенная в тройные кавычки, описывающая, что делает функция. Она может отстутствовать.
* `Тело функции`- Блок кода, который выполняется при вызове функции. Он должен быть сдвинут вправо (используя отступы).
* `return`- Оператор, используемый для возврата значения из функции. Если `return` не указан, функция вернет `None`. `return` - сохраняет результат функции, его можно заменить на `print`, но тогда функция будет только выводить результат на экран без сохранения.

## Примеры функций
### Пример 1

Программа, которая выводит сумму двух чисел:
```python
def add(a, b):
    """Возвращает сумму двух чисел."""
    result  = a + b
    return result 

# Вызов функции (несколько вариантов)
print(add.__doc__) # Вызов документации функции
var_summ = add(3, 5) # Передаём значения другой переменной
print(var_summ)  # Выведет: 8
print(add(10, 5)) # Напрямую вызываем функцию. Выведет: 15
```
Обратите внимание, что вызов функции происходит по её имени и без ключевого слова `def`

### Пример 2

Рассмотрим ситуацию: есть компьютерная игра с различными персонажами и диалогами. 

| Персонаж | Фраза |
|----------|----------|
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/magician.jpg?raw=true" width="125">   | **Mage:** I use my best spell for protection.|
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/archer.jpg?raw=true" width="125">   | **Archer:** My people are ready! What's next?|
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/enemy.jpg?raw=true" width="125">   | **Enemy:** AAAAaaarrrrrggghhhhh|

Таких диалогов (строк) может быть огромное количество. Наша задача: проверить у всех ли строк в конце есть знак препинания и не является ли строка пустой. <br>
Для начала представим всё в виде кода:
```python
Mage = "I use my best spell for protection."
Archer = "My people are ready! What's next?"
Enemy = "AAAAaaarrrrrggghhhhh"
```
Данное задание можно сделать с помощью простейших условий и применить их к каждой строке:
```python
if len(Mage) == 0:
    print("Строка пуста!")
else:
    if Mage[-1] in "!.?":
        print(True)
    else:
        print(False)

if len(Archer) == 0:
    print("Строка пуста!")
else:
    if Archer[-1] in "!.?":
        print(True)
    else:
        print(False)

if len(Enemy) == 0:
    print("Строка пуста!")
else:
    if Enemy[-1] in "!.?":
        print(True)
    else:
        print(False)
```
Но таких строк может быть гораздо больше, а код сложнее. Чтобы оптимизировать процесс, создадим функцию:
```python
# Функция для проверки строки
def exam_string(string):
    # Проверка, пуста ли строка
    if len(string) == 0:
        print("Строка пуста!")
        return None  # Возвращаем None, так как строка пуста
    else:
        # Проверка, оканчивается ли строка на любой из символов '!', '.', '?'
        if string[-1] in "!.?":
            return True
        else:
            return False

# Вызов функции для каждой строки и вывод результатов
print(exam_string(Mage))   # Ожидается: True
print(exam_string(Archer)) # Ожидается: True
print(exam_string(Enemy))  # Ожидается: False
```
Так код станет короче и проще читаемый. Данную функцию можно будет вызвать в любое время одной строкой и проверить код.

### Пример 3

| Объект | Описание |
|----------|----------|
| <img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/spaceship.gif?raw=true" width="225">   |**объект:** космический корабль <br> **класс корабля:** штурмовой <br> **работает:** да <br> **скорость:** 28000 <br> **количество пушек:** 4|

## Аргументы функций

<img src="https://github.com/TeachKait20/NoneCode/blob/main/func+python/Animais.gif?raw=true">

Аргументов (параметров) для функции бывает несколько. Различные типы аргументов в функции с реальным кодом.

Есть функция, которая приветствует пользователей и проверяет их возраст. Если пользователю меньше 16 лет, то ему отказано в доступе, иначе разрешено. На данной функции будут рассмотрены первые 3 примера.
Протестируйте программу и вызов функции с разными аргументами.
```python
def user_verification(name_user, age_user):
    print(f"Hello {name_user}! You are {age_user} years old.")
    
    if age_user < 16:
        print("Sorry, you are denied access.")
    else:
        print("Access granted!")
```

### 1. Позиционные аргументы
Передаются в функцию в определенном порядке.
```python
user_verification("Ruby", 28)
user_verification("Melissa", 15)
```

### 2. Именованные аргументы
Позволяют явно указывать имена параметров при вызове функции.
```python
user_verification(age_user=14, name_user="Ruby")
user_verification(name_user="Melissa", age_user=36)
```

### 3. Аргументы со значениями по умолчанию
Параметры могут иметь значения по умолчанию, которые используются, если аргумент не был передан. Параметры со значениями по умолчанию должны идти после обычных параметров.

Для этого примера, мы немного поменяем программу, добавив ей третий аргумент и немного дополним структуру самой функции:
```python
def user_verification(name_user, age_user, gender_user=None):
    if gender_user == None:
        print(f"Hello, {name_user}! You are {age_user} years old.")
    else:
        print(f"Hello, {name_user}! You are {age_user} years old. Gender: {gender_user}")
    
    if age_user < 16:
        approved = True
        print("Sorry, you are denied access.")
    else:
        print("Access granted!")

user_verification("Judy", 26, "female")
user_verification("Tom", 11, "male")
user_verification("Henry", 22)
```
Такой вариант добавляет возможность выбора для пользователя и исключению ошибок, если вдруг аргумент не был заполнен. Может иметь любое начальное значение с любым типом данных.

### 4. Неопределенное количество позиционных аргументов (`*args`)
Позволяет функции принимать любое количество позиционных аргументов. Аргументы передаются как кортеж.

```python
def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

# Вызов функции с разным количеством аргументов
print(add_numbers(1, 2, 3))        # Выведет: 6
print(add_numbers(5, 10, 15, 20))  # Выведет: 50
```
Или:
```python
def summ(*args):
    res = sum(args)
    print(f"Сумма: {res}")

# Вызов функции с несколькими аргументами
summ(1, 2, 3, 4)
```
### 5. Неопределенное количество именованных аргументов (`**kwargs`)
Позволяет функции принимать любое количество именованных аргументов. Они передаются в функцию в виде словаря, что позволяет обрабатывать их по ключу.
```python
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Вызов функции с разными именованными аргументами
user_info(name="Alice", age=30, gender="female")
# Выведет:
# name: Alice
# age: 30
# gender: female

user_info(name="Bob", occupation="Engineer", country="USA")
# Выведет:
# name: Bob
# occupation: Engineer
# country: USA
```

### 6. Комбинация различных типов аргументов
Можно комбинировать позиционные, `*args`, аргументы со значениями по умолчанию, `**kwargs`.
```python
def complex_function(a, b=2, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Дополнительные позиционные аргументы: {args}")
    print(f"f"Именованные аргументы: {kwargs}")

# Вызов функции с приведенными аргументами
complex_function(1, 3, 4, 5, x=10, y=20)
```

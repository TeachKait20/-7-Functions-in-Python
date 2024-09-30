# Программа для заметок
notes = {}


def new_note(name_note: str, text_note: str):
    """
    Функция для создания новой заметки.
    Аргументы:
    - name_note (str): Название заметки (должно быть непустым).
    - text_note (str): Текст заметки.

    Если заметка с таким названием уже существует, она будет перезаписана.
    """
    global notes
    if not name_note.strip():
        print("Название заметки не может быть пустым.")
        return

    if name_note in notes:
        print(f"Заметка с названием '{name_note}' уже существует и будет перезаписана.")

    notes[name_note] = text_note
    print(f"Заметка '{name_note}' успешно добавлена.")


def print_notes():
    """
    Функция для вывода всех заметок.
    Если заметок нет, выводится соответствующее сообщение.
    """
    if not notes:
        print("Нет доступных заметок.")
    else:
        for name, text in notes.items():
            print(f"Название: {name}\nТекст: {text}\n")


def delete_note(name_note: str):
    """
    Функция для удаления заметки по названию.
    Если заметка не найдена, выводится соответствующее сообщение.
    """
    global notes
    if name_note in notes:
        del notes[name_note]
        print(f"Заметка '{name_note}' удалена.")
    else:
        print(f"Заметка с названием '{name_note}' не найдена.")


# Пример использования
new_note("birthdays", "Mary - 17.09, Paul - 10.06")
new_note("VK login/password", "my number/qwerty-123")
new_note("favorite movies", "Harry Potter, Astral")

# Попытка добавить заметку без названия
new_note("", "Это тестовая заметка")

# Вывод всех заметок
print_notes()

# Удаление заметки
delete_note("favorite movies")

# Вывод после удаления
print_notes()

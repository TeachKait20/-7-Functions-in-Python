Igor_inventory = []
Maxim_inventory = ["монетка", "бутылка воды"]


def add_item(item: str, inventory: list):
    """
    Функция для добавления предмета в инвентарь.
    Аргументы:
    - item (str): Название предмета.
    - inventory (list): Инвентарь (список), в который добавляется предмет.

    Если предмет уже есть в инвентаре, возвращается сообщение.
    """
    if item not in inventory:
        inventory.append(item)
        print(f"Предмет '{item}' добавлен в инвентарь.")
    else:
        return "Предмет уже есть в инвентаре."


def del_item(item: str, inventory: list):
    """
    Функция для удаления предмета из инвентаря.
    Аргументы:
    - item (str): Название предмета.
    - inventory (list): Инвентарь (список), из которого удаляется предмет.

    Если предмета нет в инвентаре, возвращается сообщение.
    """
    if item in inventory:
        inventory.remove(item)
        print(f"Предмет '{item}' удалён из инвентаря.")
    else:
        return "Предмета нет в инвентаре."


# Пример использования
add_item("учебник по Python", Igor_inventory)
print(Igor_inventory)

del_item("монетка", Maxim_inventory)
print(Maxim_inventory)

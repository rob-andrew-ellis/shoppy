from __future__ import annotations

from pathlib import Path


def get_list(list_path: Path = Path("data/list.txt")) -> list[str]:
    """If the shopping list is saved, it is loaded, otherwise an empty list is
       returned

    Args:
        list_path: Path to saved list file

    Returns:
        A list of Strings representing the shopping list
    """
    if list_path.is_file():
        with open(list_path) as file:
            return [line.rstrip("\n") for line in file]
    else:
        return []


def add_item(my_list: list[str], item: str) -> list[str]:
    """Adds a new item to the list, only if the item is not already present

    Args:
        my_list: The shopping list
        item: The name of the item to be added

    Returns:
        The shopping list with the new item appended
    """
    if item not in my_list:
        my_list.append(item)
    else:
        print(f"{item} is already on the list, silly.")

    return my_list


def save_list(my_list: list[str], list_path: Path):
    """Saves the list to file

    Args:
        my_list: The current shopping list
    """
    with open(list_path, "w") as file:
        [file.write(item + "\n") for item in my_list]

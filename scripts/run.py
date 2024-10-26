from __future__ import annotations

from pathlib import Path

from shoppy.shopping_list import add_item, get_list, save_list

if __name__ == "__main__":
    my_list = get_list()

    print(my_list)

    my_list = add_item(my_list, input("\n Add an item to the list: "))
    save_list(my_list, Path("data/list.txt"))

    new_list = get_list()
    print(f"list now contains: {new_list}")

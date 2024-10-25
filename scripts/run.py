from __future__ import annotations

from shoppy.shopping_list import add_item, get_list

if __name__ == "__main__":
    my_list = get_list()

    print(my_list)
    print(add_item(my_list, input("\nAdd an item to the list: ")))

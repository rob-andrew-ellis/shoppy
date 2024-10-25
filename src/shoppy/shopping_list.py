from pathlib import Path


def get_list(list_path: Path = Path("data/list.txt")) -> list[str]:
    if list_path.is_file():
        with open(list_path) as f:
            return [line.rstrip("\n") for line in f]
    else:
        return []

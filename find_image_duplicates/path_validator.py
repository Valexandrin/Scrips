import os.path
from typing import List


def get_path(raw_path: str) -> str:
    return raw_path.replace('\\', '/')


def is_different(ph1: str, ph2: str, pos: int=0):
    ph1, ph2 = ph1.split('\\'), ph2.split('\\')

    while pos < len(min(ph1, ph2)):
        if ph1[pos] != ph2[pos]:
            return True
        pos += 1

    return False


def path_name_validation(paths: List[str]) -> None:
    if len(paths) == 1:
        return
    if len(paths) != 2:
        raise ValueError
    if len(set(paths)) == 1:
        raise ValueError
    if not is_different(*paths):
        raise ValueError


def path_validation(paths: List[str]) -> List[str]:
    try:
        path_name_validation(paths)
    except ValueError:
        print('Not allowed path combination')
        return

    for path in paths:
        if not os.path.isdir(path):
            print(f'Path is not exist: {path}')
            return

    return [get_path(path) for path in paths]


def main():
    path_validation([])


if __name__ == '__main__':
    main()

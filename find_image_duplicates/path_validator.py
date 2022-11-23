from pathlib import Path
from typing import List


def path_name_validation(paths: List[Path]) -> None:
    if not paths:
        raise ValueError('There are no valid directories to be processed')
    if len(paths) == 1:
        return
    if len(paths) > 2:
        raise ValueError('More than two directories cannot be processed')
    if len(set(paths)) == 1:
        raise ValueError('An attempt to compare the directory with itself')
    if paths[0].is_relative_to(paths[1]) or paths[1].is_relative_to(paths[0]):
        raise ValueError('One belongs to another')


def process_directory(paths: List[str] = []) -> List[Path]:
    validated = []
    for path in paths:
        path = Path(path)
        if not path.is_dir():
            print(f'Directory "{path}" does not not exist')
            return
        validated.append(path)

    return validated


def path_validation(paths: List[str] = []) -> List[str]:
    if paths:
        paths = process_directory(paths)
    try:
        path_name_validation(paths)
    except ValueError as err:
        print(*err.args)
        return


def main():
    path_validation()


if __name__ == '__main__':
    main()

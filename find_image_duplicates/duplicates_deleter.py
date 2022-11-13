from difPy import dif
from duplicates_list_writer import path_validation


def delete_duplicates(folder1: str, folder2: str=None) -> dict:
    dif(folder1, folder2, delete=True, silent_del=True)
    print(folder1, folder2, 'done', sep='\n')


def main():
    paths = [
        r'C:\Users\alex-\OneDrive\Изображения\vadim\камера iphone',
    ]

    validated_paths = path_validation(paths)
    if not validated_paths:
        return

    delete_duplicates(*validated_paths)


if __name__ == '__main__':
    main()

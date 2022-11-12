from duplicates_list_writer import get_path
from difPy import dif


def delete_duplicates(folder1: str, folder2: str=None) -> dict:
    dif(folder1, folder2, delete=True, silent_del=True)
    print('done')


def main():
    path = get_path(r'C:\Users\alex-\OneDrive\Изображения\vadim\камера iphone\iCloud Photos')
    delete_duplicates(path)


if __name__ == '__main__':
    main()

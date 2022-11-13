import os.path

from difPy import dif
from excel_writer import Writer
from path_validator import path_validation


def name_validation(file_name: str) -> str:
    if not os.path.isfile(file_name):
        return file_name

    split_name = file_name.split('.')
    new_name = split_name[0] + '_copy.' + split_name[1]
    return name_validation(new_name)


def write_resaults(
        search_resault: dict,
        file_name: str='find_image_duplicates/duplicates.xlsx',
    ) -> None:

    writer = Writer()

    headers = ['filename', 'location', 'duplicates']
    found_duplicates = search_resault.items()
    valid_name = name_validation(file_name)

    writer.write_excel(headers, found_duplicates, valid_name)


def search_duplicates(folder1: str, folder2: str=None) -> dict:
    search = dif(folder1, folder2)
    return search.result


def main():
    paths = [
        r'C:\Users\alex-\OneDrive\Изображения\vadim',
    ]

    validated_paths = path_validation(paths)
    if not validated_paths:
        return

    search_resault = search_duplicates(*validated_paths)
    write_resaults(search_resault)


if __name__ == '__main__':
    main()

from duplicates_size_comparer import get_cells_by_poor_resolution as cells_getter
from openpyxl import load_workbook


def delete_files(path_cells: list) -> None:
    pass


def main():
    fname = 'find_image_duplicates/duplicates_copy_copy.xlsx'
    wb = load_workbook(fname)
    ws = wb.active
    cells = cells_getter(ws)

    delete_files(cells)


if __name__ == '__main__':
    main()

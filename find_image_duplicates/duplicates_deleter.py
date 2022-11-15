import os

from duplicates_list_markup import get_cells_by_poor_resolution as cells_getter
from openpyxl import load_workbook


def delete_files(path_cells: list) -> None:
    for cell in path_cells:
        os.remove(cell.value)


def main():
    fname = '<anyfile.xlsx>'
    wb = load_workbook(fname)
    ws = wb.active
    cells = cells_getter(ws)

    delete_files(cells)


if __name__ == '__main__':
    main()

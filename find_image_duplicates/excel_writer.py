from typing import List

from openpyxl.workbook import Workbook


class Writer:
    def __init__(self) -> None:
        self.wb = Workbook()

    @staticmethod
    def get_file_name(path: str) -> str:
        res = path.split('\\')
        return res[-1]

    def __fill_col(self, col: int, values: List[str]) -> None:
        if self.headers[col] != self.headers[-1]:
            self.__fill_cell(col, values[0])
            return

        for value in values:
            self.__fill_cell(col, value)
            self.row += 1
            self.processed.add(self.get_file_name(value))

    def __fill_cell(self, col: int, value: str) -> None:
        cell = self.sheet.cell(self.row, column = col+1)
        cell.value = value

    def __write_headers(self) -> None:
        self.row = 1
        for col_num in range(len(self.headers)):
            self.__fill_cell(col_num, self.headers[col_num])

    def __write_body(self) -> None:
        self.processed = set()
        self.row = 2
        for _, val in self.body:
            if val[self.headers[0]] in self.processed:
                continue

            for col_num in range(len(self.headers)):
                content = val[self.headers[col_num]]
                values = content if isinstance(content, list) else [content]
                self.__fill_col(col_num, values)

    def write_excel(self, headers: List[str], body: dict, name:str):
        self.sheet = self.wb.active
        self.row = 1
        self.headers = headers
        self.body = body

        self.__write_headers()
        self.__write_body()

        self.wb.save(name)

from difPy import dif
import openpyxl


path_1 = r'C:\Users\alex-\OneDrive\Изображения\katya_iphone'
folder_1 = path_1.replace('\\', '/')

search = dif(folder_1)
res = search.result

wb = openpyxl.Workbook()
sheet = wb.active
cur_row = 1

headers = ['filename', 'location', 'duplicates']
for pos in range(len(headers)):
    cell = sheet.cell(row = cur_row, column = pos+1)
    cell.value = headers[pos]

cur_row += 1

duplicates = set()
for key, val in res.items():
    if val[headers[0]] in duplicates:
        continue    
    
    for col in range(len(headers)):
        content = val[headers[col]]
        values = []
        if not isinstance(content, list):
            values.append(content)
        else:
            values = content
                
        if headers[col] != 'duplicates':
            cell = sheet.cell(row = cur_row, column = col+1)
            cell.value = values[0]
            continue
        for value in values:
            val = value.split('\\')
            file_name = val[-1]
            duplicates.add(file_name)
            cell = sheet.cell(row = cur_row, column = col+1)
            cell.value = value            
            cur_row += 1
        
wb.save('duplicates.xlsx')

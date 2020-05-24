from pathlib import Path
import openpyxl as xl

import ecommerce

path = Path("c:\\users\\Gopinathan\\PycharmProjects\\HelloWorld\\ecommerce")

print(f"before {path.exists()}")

if path.exists() == False:
    print("is this is working")
    path.mkdir()

print(path.exists())

path = Path()

for file in path.glob('*.py'):
    print(file)

wb = xl.load_workbook('c:\\users\\Gopinathan\\PycharmProjects\\HelloWorld\\ecommerce\\transactions.xlsx')


sheet = wb['Sheet1']

for row in range (2,sheet.max_row+1):
    cell = sheet.cell(row,3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row,4)
    corrected_price_cell.value = corrected_price
    if row == 2:
        corrected_price_cell = sheet.cell(row-1,4)
        corrected_price_cell.value = 'Corrected Price'
wb.save('transaction_corrected.xlsx')
print('before cell value ')
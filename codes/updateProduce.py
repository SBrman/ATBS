#! python3

# updateProduce.py - Corrects costs in produce sales spreadsheet.

import openpyxl

wb = openpyxl.load_workbook(r'H:\python\files\Chapter 13\produceSales.xlsx')
sheet = wb.active

price = {'Celery': 1.19, 'Garlic': 3.07, 'Lemon': 1.27}

for row in range(2, sheet.max_row):

    productName = sheet['A'+str(row)].value
    
    if productName in price:
        sheet['B'+str(row)] = price[productName]

wb.save(r'H:\python\files\Chapter 13\produceSales_updated.xlsx')

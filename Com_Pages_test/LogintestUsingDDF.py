import xlrd




workbook = xlrd.open_workbook("F:\\EclipsePractice\\PythonSelenium\\dataFile.xlsx")

worksheet = workbook.sheet_by_name("Firstdata")

print(format(worksheet.cell(2,1).value))


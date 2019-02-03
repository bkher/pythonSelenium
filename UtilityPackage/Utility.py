import xlrd
class utility:
    
    def readExcel(self,Rownum,Colnum):
        workbook = xlrd.open_workbook("F:\\EclipsePractice\\PythonSelenium\\dataFile.xlsx")
        worksheet = workbook.sheet_by_name("Firstdata")
        return format(worksheet.cell(Rownum,Colnum).value)
       
       
       






        
    
    
    
    





    
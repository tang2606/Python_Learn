import xlrd,xlwt
excel_f = '/Users/wade/MyCode/Python_Learn/PythonExcel.xlsx'

#
# wb = xlrd.open_workbook(excel_f)
#
# teble = wb.sheet_by_index(0)
# print(str(teble.cell_value(1,1))[0:11])

new_work_book = xlwt.Workbook()

work_sheet = new_work_book.add_sheet('Mysheet')

work_sheet.write(0,2,'你大爷')

new_work_book.save('test.xlsx')


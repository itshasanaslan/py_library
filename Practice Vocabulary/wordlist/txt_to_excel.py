import openpyxl as xl
print('This script allows you to transfer your words from txt to excel.')
filename = input('Enter the excel filename: ')
txtfile= input('Enter the txt: ')
wb = xl.load_workbook(filename)
sheet = wb['Sayfa1']

c=1
d = 1
with open(txtfile,'r') as f:
	mlist = f.read().split('\n')

for a in mlist:
	cell = sheet.cell(c,1)
	cell.value = a
	c+=1

wb.save(filename)

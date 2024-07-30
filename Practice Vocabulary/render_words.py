import os
second_list = []
input('Bu script ile büyük bir txt kelime havuzundaki bilmediğim kelimeleri ayıklayıp rendered.txt dosyasına kaydediyorum.\nrendered.txt adında bir dosya oluşturmayı unutma.')
source = input('Kelime havuzunu gir: ')
with open(source,'r') as f:
	mylist = f.read().split('\n')
clear_num=0
num=1

for a in mylist:
	if len(a)==1:
		continue
	num+=1
	print(f"{num}-){a}")
	clear_num+=1
	word_in = input('>')
	if word_in=='clear':
		os.system('cls')
	if clear_num==20:
		os.system('cls')
		clear_num=0
	if word_in=='':
		continue
	elif word_in=='q':
		break
	second_list.append(a)
	print(a,'is added.')

try:
	with open('rendered.txt','a') as cc:
		for element in second_list:
			element=element+'\n'
			cc.write(element)
	input('done')
except Exception as f:
	print(f)
	input()
	print(second_list,sep='\n')
	input()
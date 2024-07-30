#dosyaları yeniden adlandırma taslağı.
import os

for f in os.listdir(): 
	if f=='izlendi' or f=='main.py':
		continue
	file = f.title() #ismi düzenle
	os.rename(f,file)
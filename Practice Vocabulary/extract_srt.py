
my = []
new_list=[]
nums =  ['0','1','2','3','4','5','6','7','8','9',':']

with open('altyazi.srt','r') as f:
	aa = f.read()
	aa = aa.split()
	for c in aa:
		if c not in my:
			my.append(c)

try:
	for a in my:
		if ':' not in a:
			if not a.isnumeric():
				new_list.append(a)
except Exception as ff:
	print(ff)
try:
	with open('extracted_words.txt','a') as f:
		for word in new_list:
			f.write(f'{word}\n')
except:
	with open('extracted_words.txt','w') as f:
		pass
	with open('extracted_words.txt','a') as f:
		for word in new_list:
			f.write(f'{word}\n')
input('Finished.')
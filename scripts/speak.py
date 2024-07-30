import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")



while True:
	a= input('Enter your word: ')
	if a=='q':
		exit()
	speak.Speak(a)
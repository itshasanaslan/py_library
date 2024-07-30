import os
clear = lambda:os.system("cls")
os.system("color 02")
os.system("title Aslan youtube-dl manager")


links = []
link="null"


def receive_links(link,links):
	if link.startswith("http"):
		links.append(link)

def print_links(links):
	print("""\n\n\n	
		***Paste a link(video or playlist) and press enter.
		***Paste one link each time
		***Type ok to download all.

					""")
	print("Added Links:",*links,sep="\n")
	print("\n")



def download(links):
	for each_link in links:
		try:
			os.system(f"youtube-dl -f best {each_link}")
			print("*Download completed\n")
			print(f"**{links.index(each_link)+1} out of {len(links)} is downloaded.")
		except Exception as ff:
			print("An error logged:",ff)

	input("Press any key to quit..")
	exit(4)


while link!="ok":
	clear()
	print_links(links)
	link = input("Enter a link: ")
	receive_links(link,links)
	
if not len(links)>0:
	input("Terminating..")
else:
	directory = input("Enter a download path. If not specified, will download in the current folder\nPath: ")
	if os.path.isdir(directory):
		os.chdir(directory)

	download(links)
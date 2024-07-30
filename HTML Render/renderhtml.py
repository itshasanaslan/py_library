import os
import re
from bs4 import BeautifulSoup
os.system('cls')
os.system('title HTML Render for Lessons')

class Content:
	def __init__(self, name, link, details, url_type):
		self.name = name
		self.link = link
		self.details = details
		self.url_type = url_type

class Parser:
	def __init__(self, title):
		self.thumbnails = {
			'video':'https://www.seekpng.com/png/detail/203-2031371_video-player-vector-logo-de-reproductor-de-video.png',
			'default': 'https://w7.pngwing.com/pngs/279/877/png-transparent-hyperlink-computer-icons-link-text-logo-number.png',
			'game':'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Fsearch%3Fq%3Dgaming&psig=AOvVaw2pAlVRTlvhwMM1CuSq8Tcg&ust=1650653375899000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKiTipXppfcCFQAAAAAdAAAAABAD',
		}
		self.contents = []
		self.main_content_open = ""
		self.main_content_close = ""
		self.init_main_content_opening(title)

	
	def init_main_content_opening(self, title):
		with open('content.txt', 'r', encoding='utf-8') as file:
			self.main_content_open = file.read()

		self.main_content_open += f"""
		<h1>{title} Materials</h1>
		</div>
		<div class="flex-container">
		"""


	def truncate(self, text):
		text_len = len(text)
		if text_len > 12:
			return text[0:12] + '...'
		else:
			return text[0:text_len - 3] + '...'

	def add(self, content):
		self.contents.append(content)

		data = self.main_content_open

		for item in self.contents:
			thumbnail = self.thumbnails.get(item.url_type)
			if not thumbnail:
				thumbnail = self.thumbnails.get('default')
			print(thumbnail)
			data += f"""
			    <div class="link-item-card">
                <img class="link-picture" src="{thumbnail}">
                <p class="title">
                  {item.name}
                </p>
                <div class="details-row">
                  <p class="details">
                    {self.truncate(item.details)}
                  </p>
                </div>
                <button class="link-button">
                    <a href="{item.link}" class="a-in-button" target="_blank">Open..</a>
                </button>
              </div>  
			"""


		data += """
		</div>
		<div class="footer"> </div>
		</body>
		</html>
		"""

		return data


filename = input("Title: ")
desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

file_path = os.path.join(desktop, filename + '.html')
p = Parser(filename)

def prompt():
	name = input("Name: ")
	url = input("Url: ")
	details = input("Details: ")
	url_type = input("Type: ")

	return Content(name, url, details, url_type)

while True:
	s = p.add(prompt())
	with open(file_path, 'w', encoding='utf-8') as file:
		file.write(s)
	print("Saved.")

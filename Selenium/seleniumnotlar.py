# chrome versiyonunu bul ve ona göre bir selenium chrome driver indir
#chrome://version/
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://instagram.com/hasanaslan7"
driver.get(url)


time.sleep(2)
driver.maximize_window()
if "Hasan Aslan" in driver.title:
	print("Correct!")
	driver.save_screenshot("deneme.png")

time.sleep(2)
driver.close()


print("Exit")


###############################################################
^^^^^^^^^^^^^^^SELECTORS^^^^^^^^^^^^^^
#selectors.html oluşturdum.


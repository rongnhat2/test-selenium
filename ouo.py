import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
import requests


for x in range(4):
	url = "https://launch.rhass.vn/api/get?status=1"
	response = requests.get(url)
	response.encoding = 'utf-8'  
	print(response.text)

	firefox_options = Options()
	# firefox_options.set_preference("browser.privatebrowsing.autostart", True)
	firefox_options.add_argument("start-maximized")
	firefox_options.add_argument("--headless")

	driver = webdriver.Firefox(options=firefox_options)

	driver.set_window_size(1920, 1080)
	driver.get(response.text)
	print("finished")
	time.sleep(5) 
	print("Clicking Button")
	time.sleep(5)
	driver.execute_script("document.getElementsByTagName('button')")
	driver.execute_script("document.getElementsByTagName('button')[0].click()")
	time.sleep(5) 
	print("running button 2")
	time.sleep(5)
	driver.execute_script("document.getElementsByTagName('button')[0].click()")
	time.sleep(5)
	print("click successful")
	time.sleep(20)
	driver.quit() 
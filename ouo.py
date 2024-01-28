import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import mouse
import requests


for x in range(3):
	url = "https://launch.rhass.vn/api/get?status=2"
	response = requests.get(url)
	response.encoding = 'utf-8'  
	print("----------------")
	print("* Loading page *")
	print(response.text)

	firefox_options = Options()
	# firefox_options.set_preference("browser.privatebrowsing.autostart", True)
	firefox_options.add_argument("start-maximized")
	firefox_options.add_argument("-private")
	firefox_options.add_argument("--headless")

	driver = webdriver.Firefox(options=firefox_options)

	driver.set_window_size(1920, 1080)
	driver.get(response.text)
	print("* Loaded *")
	time.sleep(10) 
	cloudflale = driver.find_elements(By.XPATH, '//iframe')
	
	time.sleep(600) 
	# while len(cloudflale) == 1:
	# 	time.sleep(10) 
	# 	mouse.move(600, 290, duration = 1.0)
	# 	mouse.click('left')
	# 	print("* Bypassed *")
	# 	time.sleep(10) 
		
	time.sleep(3) 
	print("* Run Button 1 *")
	time.sleep(3)
	driver.execute_script("document.getElementsByTagName('button')[0].click()")
	print("* Done btn 1   *")
	time.sleep(3) 
	print("* Run Button 2 *")
	time.sleep(3)
	driver.execute_script("document.getElementsByTagName('button')[0].click()")
	time.sleep(3)
	print("* Done btn 2   *")
	print("----------------")
	print("  ")
	time.sleep(2)
	driver.quit() 
import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
import requests


for x in range(4):
	url = "https://launch.rhass.vn/api/get?status=2"
	response = requests.get(url)
	response.encoding = 'utf-8'  
	print("Loading page")
	print(response.text)

	firefox_options = Options()
	# firefox_options.set_preference("browser.privatebrowsing.autostart", True)
	firefox_options.add_argument("start-maximized")
	firefox_options.add_argument("--headless")

	driver = webdriver.Firefox(options=firefox_options)

	driver.set_window_size(1920, 1080)
	driver.get(response.text)
	print("finished")
	# time.sleep(10) 
	# print("Clicking Button")
	# time.sleep(5)
	# print(driver.execute_script("document.querySelectorAll('html')"))
	# print(driver.execute_script("document.documentElement.innerHTML"))
	# time.sleep(15)
	# driver.execute_script("document.getElementsByTagName('button')[0].click()")
	# print("Clicking successful")
	# time.sleep(3) 
	# print("running button 2")
	# time.sleep(15)
	# driver.execute_script("document.getElementsByTagName('button')[0].click()")


	print("Adding jquery")
	driver.execute_script("var script = document.createElement('script');script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';document.getElementsByTagName('head')[0].appendChild(script);")
	time.sleep(10)
	print("Clicking Button")
	driver.execute_script("$('#btn-main').click()")
	time.sleep(5)
	print("Adding jquery page 2")
	driver.execute_script("var script = document.createElement('script');script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';document.getElementsByTagName('head')[0].appendChild(script);")
	time.sleep(10)
	print("running button 2")
	driver.execute_script("$('#btn-main').click()")
	
	time.sleep(5)
	print("click successful")
	time.sleep(20)
	driver.quit() 
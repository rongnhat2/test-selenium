import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests


for x in range(3):
	url = "https://launch.rhass.vn/api/get?status=1"
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
	time.sleep(3) 
	cloudflale = driver.find_elements(By.XPATH, '//iframe')
	
	# time.sleep(600) 
	while len(cloudflale) == 1:
		print("* Cloudflare  block *")
		time.sleep(5) 
		action = ActionChains(driver)
		action.move_by_offset(550, 380)
		action.click()
		action.perform()
		time.sleep(10) 
		# mouse.move(550, 380, duration = 1.0)
		# mouse.click('left')
		print("* Bypassed *")
		driver.get(response.text)
		print("* Reload *")
		time.sleep(5) 
		cloudflale = driver.find_elements(By.XPATH, '//iframe')
		
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
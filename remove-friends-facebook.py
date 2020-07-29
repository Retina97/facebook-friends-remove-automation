# An automatic script to delete all friends on facebook
# Hichame Aniter
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
import time

# Path to driver
PATH = "./driver/geckodriver"

# Path to profile 
profile_path = "/home/hichame/.mozilla/firefox/4s4i20bs.default-release"
profile = FirefoxProfile(profile_directory = profile_path)


browser = webdriver.Firefox(firefox_profile = profile, executable_path = PATH)

#your facebook id
facebookID = ''

listID = 'uiList _262m _4kg'
divID = 'u_h_8'
buttonID = "u_0_2r"

browser.get('https://www.facebook.com/'+ facebookID + '/friends')

#parentElement = browser.find_element_by_xpath("//ul[@class='"+listID+"']")
#elementList = parentElement.find_elements_by_xpath("./li")




while (True):

	parentElement = browser.find_element_by_xpath("//ul[@class='"+listID+"']")
	elementList = parentElement.find_elements_by_xpath("./li")
	scrol = 260	
	i=0

	for e in elementList:
		try:			
			i+=1
			if(i == 9): break
			browser.execute_script("window.scrollTo(0, "+str(scrol)+")") 
			scrol+=30
			print (e)
			temp = e.find_element_by_xpath(".//div[@class='_5t4x']/div/a")
			#temp.click()
			hover = ActionChains(browser).move_to_element(temp)
			hover.perform()
			time.sleep(0.5)	
			remove = browser.find_element_by_xpath("//span[contains(text(), 'Retirer')]")
			#hover = ActionChains(browser).move_to_element(remove)
			#hover.perform()
			remove.click()
			zero = browser.find_element_by_id('u_0_1s')
			hover = ActionChains(browser).move_to_element(zero)
			hover.perform()
			time.sleep(1.2)
		except:
			break
	
	browser.refresh();

#button = browser.find_element_by_id(buttonID)

#hover = ActionChains(browser).move_to_element(button)
#hover.perform()

#time.sleep(2)
#remove = browser.find_elements_by_xpath("//*[contains(text(), 'Retirer')]")

#remove.click()

#browser.close()

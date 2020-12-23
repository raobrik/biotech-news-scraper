
from selenium import webdriver
#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



import time 

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.genomeweb.com/")

browser = driver
browser.maximize_window()
driver.implicitly_wait(5)

#finds search bar via full xpath, else "element not interactable" 
search = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div[4]/div/div/form/div/div/div/div[1]/div/div/input")
search.click()
driver.implicitly_wait(5)

#ActionChains(driver).move_to_element(search).send_keys("microbiome").send_keys(Keys.RETURN)
#type query and hit enter
search.send_keys("microbiome")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()


import sys
import os
from selenium import webdriver

#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager

#os.environ["PATH"] += os.pathsep + os.pathsep.join([r"C:\Program Files (x86)\chromedriver.exe"])

#PATH = os.environ["PATH"]
#$PATH += [r"C:\Users\raobr\Documents\Projects\MyProjects\Python\new_biotech_scraper\repo\webdriver\chromedriver_win32\chromedriver.exe"]
#PATH = r"C:\Users\raobr\Documents\Projects\MyProjects\Python\new_biotech_scraper\repo\webdriver\chromedriver_win32\chromedriver.exe"


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.biospace.com/news/")
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from pyshadow.main import Shadow

file_path = os.getcwd()
output_file = file_path+'\\sha_values_SPA.csv'
chromedriver = os.getcwd()+'\\driver\\chrome\\chromedriver.exe'
my_url = "http://www.virustotal.com/gui/search/emotet/comments"
file_contents = []
option = Options()
option.headless = True

driver = webdriver.Chrome(options = option, service = Service(chromedriver))
shadow = Shadow(driver)
driver.get(my_url)
WebDriverWait(driver, 60).until(lambda x: shadow.find_element('p#meta'))
element = shadow.find_element('html')

# regex to filter the SHA content
file_contents = re.findall("[A-Fa-f0-9]{64}", element.text)
driver.close()

# Writing the file_contents to the output_file
file = open(output_file,'w')
for items in file_contents:
    file.writelines(f"{items}\n")
file.close()
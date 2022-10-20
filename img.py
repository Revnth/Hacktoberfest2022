import time
import os
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys



def imagedown(search, folder):
    driver = webdriver.Chrome('/Users/joshua/chromedriver')
    driver.get('https://www.google.com/imghp?hl=en')
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    box.send_keys(search)
    box.send_keys(Keys.ENTER)
    
    for i in range(21):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(folder+'-'+str(i)+'.png')
        except:
            pass
    os.chdir("../")


imagedown('Lionel Messi', 'footballer')

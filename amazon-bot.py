from selenium import webdriver
from time import sleep

class PS5Bot(url):
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def login(self):
        self.driver.get('https://www.amazon.com')
        sleep(50)

    def checkAndBuyPS5(self):
        while True:
            self.driver.get(self.url)
            sleep(1)   
            try:
                buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
                buyNow.click()
                sleep(2)
                buyNow2 = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn"]')
                buyNow2.click()
                sleep(2)
                buyNow3 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')  
                buyNow3.click()
                sleep(1)
                self.driver.close()
                break
            except Exception as e:
                print(e)
                sleep(1.5)

bot = PS5Bot('https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452')
bot.login()
bot.checkAndBuyPS5()

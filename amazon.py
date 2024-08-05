from selenium import webdriver
from selenium.webdriver.common.by import By

class AmazonSeleniumRobot:
    def __init__(self):
        pass
      
    def check_product_availablility_for(self, amazon_links):
        checked_amazon_links = []
        driver = webdriver.Chrome()

        for link in amazon_links:
            driver.get(link)
            elements = driver.find_elements(By.XPATH, '//*[@id="outOfStock"]/div/div[1]/span[1]')
            for element in elements:
                checked_amazon_links.append(element.text)
                print(checked_amazon_links)




from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/AZUREBEAUTY-Polish-White-Color-lasting/dp/B086WXC4S8?&_encoding=UTF8&tag=glowslybeauty2-20&linkCode=ur2&linkId=0697590672f78ef9777a963d4b8ea61c&camp=1789&creative=9325")
elements = driver.find_elements(By.XPATH, '//*[@id="productTitle"]')
for element in elements:
    print(element.text)







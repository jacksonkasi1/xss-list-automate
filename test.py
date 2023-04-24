from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.nasa.gov')
headlines = driver.find_elements_by_class_name("headline")
for headline in headlines:
    print(headline.text.strip())
driver.close()
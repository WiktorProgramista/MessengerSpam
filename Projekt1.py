import time
from settings import  Info
from selenium import webdriver

driver = webdriver.Firefox()

NazwaOsoby = input("Wpisz nazwę osoby: ")

if NazwaOsoby != "":
    driver.get(Info.url)
    buttons = driver.find_element_by_xpath("//button[text()='Akceptuj wszystkie']").click()
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0,600)")
    driver.find_element_by_xpath('//*[@id="email"]').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(Info.email)
    driver.find_element_by_xpath('//*[@id="pass"]').click()
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(Info.password)
    driver.find_element_by_xpath("//button[text()='Zaloguj się']").click()
    time.sleep(4)
    driver.find_element_by_xpath(f"//span[text()='{NazwaOsoby}']").click()
    while True:
        if Info.attempt < 100:
            Info.attempt += 1
            print("Ilosc: ", Info.attempt)

            text_field = driver.find_element_by_css_selector('.notranslate')
            text_field.send_keys(Info.text)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div').click()
        else:
            break

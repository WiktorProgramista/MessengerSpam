import time
from settings import  Info
from selenium import webdriver

driver = webdriver.Firefox()

class MessSpam:

    def findByXpath(xpath):
        driver.find_element_by_xpath(xpath).click()
        return xpath

    Id = int(input("Wpisz id/nazwe: "))

    url = f"https://www.messenger.com/t/{Id}"

    Tekst = input("Wpisz teskt: ")

    Ilosc = int(input("Wpisz ilosc: "))

    if Id != "":
        driver.get(url)
        buttons = driver.find_element_by_xpath("//button[text()='Akceptuj wszystkie']").click()
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0,600)")

        with open("email.txt", "r") as email_txt:
            lines1 = email_txt.readlines()
        for line1 in lines1:

            findByXpath('//*[@id="email"]')
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(line1)

        with open("pass.txt", "r") as pass_txt:
            lines2 = pass_txt.readlines()
        for line2 in lines2:

            findByXpath('//*[@id="pass"]')
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys(line2)
            findByXpath("//button[text()='Kontynuuj']")
            time.sleep(4)
            for i in range(Ilosc):
                if Ilosc != 0:

                    Info.attempt += 1
                    print("Ilosc: ", Info.attempt)
                    text_field = driver.find_element_by_css_selector('.notranslate')
                    text_field.send_keys(Tekst)
                    time.sleep(1)
                    findByXpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
                else:
                    print("Koniec!")
                    break

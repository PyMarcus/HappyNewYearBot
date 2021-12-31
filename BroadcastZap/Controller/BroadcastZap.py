from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BroadcastZap:
    site = "https://web.whatsapp.com/"

    @property
    def get_site(self) -> str:
        return BroadcastZap.site

    @classmethod
    def search_contacts(cls):
        path: Service = Service("./chromedriver.exe")
        driver = webdriver.Chrome(service=path)
        try:
            driver.get(BroadcastZap.site)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
            finally:
                time.sleep(10)
                driver.find_element(By.XPATH, "//div[@role='textbox']").click()  # clica na caixa de texto
                time.sleep(1)
                lista = []
                for n in range(0, 50, 3): #  range(0, 50, 3):
                    for x in range(n):
                        time.sleep(1.3)  # tempo para carregar o java script
                        driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(f"{Keys.DOWN}" * x)
                        classe_de_numeros = driver.find_elements(By.XPATH,
                                                                 "//div[@class='zoWT4']//span[@dir='auto']")  # captura contatos.
                        for contatos in classe_de_numeros:
                            if contatos.text in lista:
                                pass
                            else:
                                lista.append(contatos.text)
                return lista, driver
        except NoSuchElementException as e:
            print("Possivelmente, ocorreu um erro no tempo de abertura da página")
            print(e)

    @classmethod
    def send_msg(cls):
        contatos, driver = BroadcastZap.search_contacts()
        msg = "OBS: esta mensagem foi enviada por um bot que construí.No entanto, saiba que é uma mensagem sincera!\nEstou apenas me divertindo um pouco :) - e programei para enviar agora,pois vou estar off"
        for nomes in contatos:
            driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(f"{nomes}")
            time.sleep(1)
            driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(f"{Keys.ENTER}")
            mensagem = driver.find_element(By.XPATH,"//div[@id='main']//footer[@class='_2cYbV']//div[@class='_13NKt copyable-text selectable-text']")
            mensagem.click()
            time.sleep(0.3)
            mensagem.send_keys(msg)
            time.sleep(1)
            time.sleep(0.3)
            mensagem.send_keys(Keys.ENTER)
            time.sleep(2)


if __name__ == '__main__':
   # BroadcastZap.search_contacts()
   BroadcastZap.send_msg()
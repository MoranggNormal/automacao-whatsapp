import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib


contatos = pd.read_excel('ARQUIVO.XSLX')

navigator = webdriver.Edge()
navigator.get("https://web.whatsapp.com/")

while len(navigator.find_elements_by_id("side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navigator.get(link)
    while len(navigator.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navigator.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)

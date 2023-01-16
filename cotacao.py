# Passo 1: Acessar o navegador
import pyautogui
import time
import pyperclip
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/path/to/chromedriver")
chrome = webdriver.Chrome(service=service)
chrome.get("https://www.google.com/")


chrome.implicitly_wait(0.5)


# Passo 2: Pesquisar a cotação da moeda desejada
pyperclip.copy('cotação do dólar')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')

price_dolar = chrome.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

file_products = pd.read_excel('Produtos.xlsx')

file_products.loc[file_products['Moeda'] == 'Dólar', 'Cotação'] = price_dolar

chrome.get("https://www.google.com/")

pyperclip.copy('cotação do euro')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')

price_euro = chrome.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

file_products.loc[file_products['Moeda'] == 'Euro', 'Cotação'] = price_euro

chrome.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,%C3%A9%20de%20car%C3%A1ter%20exclusivamente%20informativo.')
price_gold = chrome.find_element(
    By.XPATH,
    '//*[@id="comercial"]'
).get_attribute('value')
file_products.loc[file_products['Moeda'] == 'Ouro', 'Cotação'] == price_gold

# Passo 3: Enviar esse dado da cotação para a tabela
# Passo 4: Calcular os valores de venda com base na cotação atual



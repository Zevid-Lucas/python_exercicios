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


pyperclip.copy('cotação do dólar')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')

price_dolar = chrome.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

file_products = pd.read_excel('Produtos.xlsx')

file_products.loc[file_products['Moeda'] == 'Dólar', 'Cotação'] = float(price_dolar)


chrome.get("https://www.google.com/")

pyperclip.copy('cotação do euro')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')

price_euro = chrome.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

file_products.loc[file_products['Moeda'] == 'Euro', 'Cotação'] = float(price_euro)

chrome.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,%C3%A9%20de%20car%C3%A1ter%20exclusivamente%20informativo.')

price_gold = chrome.find_element(
    By.XPATH,
    '//*[@id="comercial"]'
).get_attribute('value')
price_gold = price_gold.replace(',','.')

file_products.loc[file_products['Moeda'] == 'Ouro', 'Cotação'] == float(price_gold)
file_products['Preço de Compra'] = file_products['Preço Original'] * file_products['Cotação']
file_products['Preço de Venda'] = file_products['Preço de Compra'] * file_products['Margem']

file_products.to_excel('novos_produtos.xlsx', index=False)

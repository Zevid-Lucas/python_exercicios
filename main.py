import pandas as pd
import pyautogui
import time

# Passo 1 - Abrir o arquivo
file = pd.read_excel('Vendas - Dez.xlsx')
new_file = file.copy()

# Passo 2 - Calcular os dados de faturamento e produtos vendidos
faturamento = new_file['Valor Final'].sum()
quantidade_produtos_vendidos = new_file['Quantidade'].sum()


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

pyautogui.moveTo(3671, 11)
pyautogui.click()
time.sleep(1)
pyautogui.write('comida')
pyautogui.press('enter')


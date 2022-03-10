import time
import pyautogui #Importando o pyautogui        
import pyperclip #Importando o pyperclip
import pandas as pd
pyautogui.PAUSE = 2 #Pausa de 1 segundo
pyautogui.press("win") #Comando para pressionar a tecla win
pyautogui.write("chrome") #Comando para escrever o no chrome
pyautogui.press("enter") #Comando para pressionar a tecla enter
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga") #Comando para copiar a url
pyautogui.hotkey("ctrl","v") #Comando para colar o nosso link
pyautogui.press("enter") #Comando para pressionar a tecla enterhttps://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga
time.sleep(4)
pyautogui.click(x=476, y=331, clicks=2)# Comando para dar 2 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=425, y=395, clicks = 1)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=1661, y=205, clicks =1)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=1409, y=739, clicks = 1)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(6)
tabela = pd.read_excel(r"C:\Users\paulo\Downloads\Vendas - Dez.xlsx") #Lendo a tabela na pagina download
faturamento = tabela["Valor Final"].sum()#vendo o faturamento e somando
quantidade = tabela["Quantidade"].sum() #vendo a quantidade elementos na tabela e somando
pyautogui.hotkey("ctrl","t")#Comando para ultilizar o atalho
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")#Comando para copiar a url
pyautogui.hotkey("ctrl","v") #Comando para colar o nosso link
pyautogui.press("enter")#Comando para pressionar a tecla enter
time.sleep(4)
pyautogui.click(x=110, y=234, clicks=1)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(2)
pyautogui.write("paulodaniel925@gmail.com")#Comando para digitar o email
time.sleep(2)
pyautogui.press("enter") #comando para pressionar a tecla enter
time.sleep(2)
pyautogui.press("tab")# Comando para pular pra a proxima instrução
pyautogui.write("Faturamento da empresa")#Escrever no assunto do texto
time.sleep(2)
pyautogui.press("tab")# Comando para pular pra a proxima instrução
texto =f""" Prezados, Bom dia 
        O faturamento de ontem foi de:R${faturamento:,.2f}
        A quantidade de produtos vendido foi de: R${quantidade:,.2f}"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
time.sleep(4)
pyautogui.hotkey("ctrl","enter")#Código para enviar o email
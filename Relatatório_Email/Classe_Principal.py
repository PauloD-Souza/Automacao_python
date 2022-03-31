import time
import pyautogui #Importando o pyautogui        
import pyperclip #Importando o pyperclip
import pandas as pd
pyautogui.PAUSE = 2 #Pausa de 1 segundohttps://drive.google.com/drive/folders/1e79icNUtL7k50wTH-c5Pu3nCl3jSiycn
pyautogui.press("win") #Comando para pressionar a tecla win
pyautogui.write("edge") #Comando para escrever na barra de pesquisa
pyautogui.press("enter") #Comando para pressionar a tecla enter
time.sleep(3)
pyperclip.copy("https://drive.google.com/drive/folders/1e79icNUtL7k50wTH-c5Pu3nCl3jSiycn") #Comando para copiar a url
pyautogui.hotkey("ctrl","v") #Comando para colar o nosso link
pyautogui.press("enter") #Comando para pressionar a tecla enterhttps://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga
time.sleep(4)
pyautogui.click(x=1617, y=414, clicks=2)# Comando para dar 2 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=1623, y=327, clicks = 2)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=483, y=347, clicks =2)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x=483, y=347, clicks =2)
time.sleep(1)
pyautogui.click(x=775, y=340, clicks = 2)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(3)
pyautogui.click(x= 1116, y = 504, button='right')
time.sleep(1)
pyautogui.click (x = 1119, y = 619, clicks= 1)
pyautogui.click (x = 812, y = 61, clicks= 1)
pyautogui.write("projeto")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x = 516, y = 229, clicks = 2)
time.sleep(10)
pyautogui.hotkey("ctrl","t")#Comando para ultilizar o atalho
pyperclip.copy("https://web.whatsapp.com/")#Comando para copiar a url
pyautogui.hotkey("ctrl","v") #Comando para colar o nosso link
pyautogui.press("enter")#Comando para pressionar a tecla enterchrome
time.sleep(7)
pyautogui.click(x=457, y=215, clicks=1)# Comando para dar 1 click na tela, pyautogui.position, é o comando para saber a posição do mouse
time.sleep(2)
pyautogui.write("max")#Comando para digitar o email
time.sleep(1)
pyautogui.press("enter") #comando para pressionar a tecla enter
time.sleep(2)
pyautogui.write("O video esta sendo upado para o driver, em 5 minutos você pode ir olhar")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x = 1918, y = 6, clicks= 1)

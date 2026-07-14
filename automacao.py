# Bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time
pyautogui.PAUSE = 1

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


# Passo 1: Entrar no sistema da empresa
# abrir navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer login
#clicar no campo de e-mail
pyautogui.click(x=913, y=476)
pyautogui.write("projetoautomaçãogleise@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    # Passo 4: Cadastrar os produtos
    pyautogui.click(x=831, y=323)

    #campo código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o próximo campo

    #campo marca
    marca = str(tabela.loc [linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #campo tipo
    tipo = str(tabela.loc [linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #campo categoria
    categoria = str(tabela.loc [linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #campo preço unitário
    preco_unitario = str(tabela.loc [linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #campo custo
    custo = str(tabela.loc [linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #campo obs
    obs = str(tabela.loc [linha, "obs"])
    if obs != "nan":     # -> se a obs for diferente de NaN então deixe vazio
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    # voltar para o início da tela
    pyautogui.scroll(5000)

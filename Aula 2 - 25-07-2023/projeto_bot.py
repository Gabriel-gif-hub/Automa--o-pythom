# Projeto de bot para automação
import pyautogui as pa
from time import sleep
import pandas as pd

# Atribuindo a tabela/banco de dados
tabela = pd.read_csv('produtos.csv')

# Regra de tempo de execução de cada ação do pa
pa.PAUSE = 0.6

# def sleep
def s():
    sleep(1)

# Abrindo o windows
pa.press('win')
# Digitar o nome do navegador
pa.write('opera')
# Enter
pa.press('enter')
# Clicar na barra
s()
pa.click(x=489, y=66)
# Digitar link
s()
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
# Enter
pa.press('enter')
# Clicar no campo de login
s()
pa.click(x=525, y=390)
# Digitar email
pa.write('emaildeteste@gmail.com')
# Tab (ir para o próximo campo)
s()
pa.press('tab')
# Digitar senha
s()
pa.write('senha123')
# Entar no cadastro
pa.click(x=517, y=533)


for linha in tabela.index:

    # Clicar no campo inicial
    pa.click(x=281, y=289)

    # Cadastrando o produto
    pa.write(tabela.loc[linha,'codigo'])
    # Tab
    sleep(2)
    pa.press('tab')

    # Cadastrando o produto
    s()
    pa.write(str(tabela.loc[linha,'marca']))
    # Tab
    s()
    pa.press('tab')

    # Cadastrando o produto
    pa.write(str(tabela.loc[linha,'tipo']))
    # Tab
    s()
    pa.press('tab')

    # Cadastrando o produto
    pa.write(str(tabela.loc[linha,'categoria']))
    # Tab
    s()
    pa.press('tab')

    # Cadastrando o produto
    pa.write(str(tabela.loc[linha,'preco_unitario']))
    # Tab
    s()
    pa.press('tab')

    # Cadastrando o produto
    pa.write(str(tabela.loc[linha,'custo']))
    # Tab
    s()
    pa.press('tab')

    # Condição de cadastro
    if not pd.isna(tabela.loc[linha,'obs']):
        # Cadastrando o produto
        pa.write(str(tabela.loc[linha,'obs']))

    # Tab
    s()
    pa.press('tab')

    # Confirmar o cadastro do produto
    pa.press('enter')

    # Subir a tela
    pa.scroll(5000)

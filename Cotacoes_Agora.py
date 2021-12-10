import requests
from datetime import datetime
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}'''

    local_dt = datetime.now()
    local_dt_txt = local_dt.strftime('%d/%m/%Y %H:%M:%S')

    text_cotacoes["text"] = texto
    text_dt["text"] = local_dt_txt

janela = Tk()
janela.title("Cotação de Moedas")
janela.geometry("260x305")  # parametrizar o tamanho inicial da janela

text_presents = Label(janela, text="COTAÇÃO DE MOEDAS - US$ - € - Bitcoin", padx=15, pady=15)
text_presents.grid(column=0, row=0)

text_orientation = Label(janela, text="Clique no botão para obter as cotações.", padx=15, pady=15)
text_orientation.grid(column=0, row=1)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes, padx=10, pady=10)
botao.grid(column=0, row=2)

text_cotacoes = Label(janela, text="", padx=10, pady=10, font="Verdana")
text_cotacoes.grid(column=0, row=3)

text_dt = Label(janela, text="", padx=10)
text_dt.grid(column=0, row=4)

footer = Label(janela, text="Developed by Jorge Jah. © ")
footer.grid(column=0, row=5, pady=20)

janela.mainloop()

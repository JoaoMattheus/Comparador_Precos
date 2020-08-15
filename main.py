import PySimpleGUI as sg
from buscador import Buscador
from time import sleep

class Tela:
    def __init__(self):
        layout = [
            [sg.Text('Pesquisa de Preço', size=(20,1), justification='center', font='Arial 30')],
            [sg.Checkbox('Carrefur', key='carrefur')],
            [sg.Text('Link: ', size=(10,0), justification='right'), sg.Input(default_text='https://tinyurl.com/y57jxefk', size=(45,0), key='link_carrefur')],
            [sg.Checkbox('Extra', key='extra')],
            [sg.Text('Link: ', size=(10,0), justification='right'), sg.Input(default_text='https://tinyurl.com/y4knrdk5', size=(45,0), key='link_extra')],
            [sg.Checkbox('Casas Bahia', key='casasBahia')],
            [sg.Text('Link: ', size=(10,0), justification='right'), sg.Input(default_text='https://tinyurl.com/y2kjdfml', size=(45,0), key='link_casasBahia')],
            [sg.Checkbox('Ponto Frio', key='pontoFrio')],
            [sg.Text('Link: ', size=(10,0), justification='right'), sg.Input(default_text='https://tinyurl.com/yy4wckhq', size=(45,0), key='link_pontoFrio')],
            [sg.Submit("Pesquisar", size=(55,0), )]
        ]
        janela = sg.Window('Pesquisa de Preço').layout(layout)
        self.button, self.values = janela.read()
        self.valores = {}
        self.busca = Buscador()
        if self.button == 'Pesquisar':
            self.pesquisar()

    def pesquisar(self):
        carrefur = self.values['carrefur']
        link_carrefur = self.values['link_carrefur']
        xpath_carrefur = '/html/body/main/div/div[6]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div[2]/span/div/span[1]/item'
        extra = self.values['extra']
        link_extra = self.values['link_extra']
        xpath_extra = '//*[@id="ctl00_Conteudo_ctl00_precoPorValue"]/i'
        casasBahia = self.values['casasBahia']
        link_casasBahia = self.values['link_casasBahia']
        xpath_casasBahia = '//*[@id="ctl00_Conteudo_ctl00_precoPorValue"]/i'
        pontoFrio = self.values['casasBahia']
        link_pontoFrio = self.values['link_pontoFrio']
        xpath_pontoFrio = '//*[@id="ctl00_Conteudo_ctl00_precoPorValue"]/i'

        if carrefur:
            val_carrefur = self.busca.buscaPreco(link_carrefur, xpath_carrefur)
            self.valores['carrefur'] = val_carrefur[3:]
        if extra:
            self.valores['extra'] = self.busca.buscaPreco(link_extra, xpath_extra)
        if casasBahia:
            self.valores['casasBahia'] = self.busca.buscaPreco(link_casasBahia, xpath_casasBahia)
        if pontoFrio:
            self.valores['pontoFrio'] = self.busca.buscaPreco(link_pontoFrio, xpath_pontoFrio)
        self.busca.fechar()
        menor = min(self.valores, key=self.valores.get)
        mensagem = f'O menor valor é na loja {menor} por R$ {self.valores[menor]}'
        self.mostraResultado(mensagem)

    def mostraResultado(self, mensagem):
        layout2 = [
            [sg.Text(mensagem)]
        ]
        janela2 = sg.Window('Pesquisa de Preço').layout(layout2)
        self.button2, self.values2 = janela2.read()

Tela()
import json
import subprocess as s

class Chatbot():
    __comando = "indefinido"

    def __init__(self):
        self.__comando = "indefinido"

    def escuta(self, frase=None):
        if frase == None:
            return "Preciso de um comando"
        frase = str(frase)
        frase = frase.lower()
        return frase

    def encontraComando(self, comando):
        comandosConhecidos = ['passa', 'diga']
        if comando in comandosConhecidos:
            return True
        return False

    def pensa(self, frase):
        if frase.startswith('bucao'):
            strLista = frase.split(' ')
            for strComando in strLista:
                if self.encontraComando(strComando):
                    __comando = strComando

    def pegaDados(self, nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]

        nome = nome.title()
        return nome

    def fala(self):
        if self.__comando == "indefindo":
            return 'dados do Bucao'
        else:
            return 'dados da Mimi Catarinense'

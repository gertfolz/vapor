import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import misc
import database as db
from game import Game
from user import User
import authentication as auth
import friendshipmanager as fm
import storemanager as sm
import librarymanager as lm
import tkinter

from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        #Criação dos Containers das telas
        # Container do Titulo
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        #Container do input de Nome
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()

        #Container do Input de Senha
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 30
        self.terceiroContainer.pack()

        #Container do Botão
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Container do Criar Cadastro
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()


        self.titulo = Label(self.primeiroContainer, text="Plataforma Vapor")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        '''
        self.criaCadastro = Button(self.quintoContainer)
        self.criaCadastro["text"] = "Novo Usuário"
        self.criaCadastro["font"] = ("Calibri", "8")
        self.criaCadastro["width"] = 12
        self.criaCadastro["command"] = self.cadastro()
        self.criaCadastro.pack()
        '''
    #Método verificar senha
    def verificaSenha(self):
        user = User()
        user.username = self.nome.get()
        user.password = self.senha.get()
        cod = auth.login(user)
        if cod == 0:
            self.mensagem["text"] = "Login realizado com sucesso"
        elif cod == 1:
            self.mensagem["text"] = "Usuário não encontrado"
        else:
            self.mensagem["text"] = "Senha incorreta"


root = Tk()
Application(root)
root.mainloop()
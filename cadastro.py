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
        self.segundoContainer["padx"] = 50
        self.segundoContainer.pack()

        #Container do Input de Email
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 50
        self.terceiroContainer.pack()

        #Container do Input de senha
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        # Container do Input de confirmação de senha
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        # Container do Botão
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Plataforma Vapor")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.emailLabel = Label(self.terceiroContainer, text="Email", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.terceiroContainer)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.senhaLabel = Label(self.quartoContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.quartoContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.ConfirmaSenhaLabel = Label(self.quintoContainer, text="Confirmar Senha", font=self.fontePadrao)
        self.ConfirmaSenhaLabel.pack(side=LEFT)

        self.ConfirmaSenha = Entry(self.quintoContainer)
        self.ConfirmaSenha["width"] = 30
        self.ConfirmaSenha["font"] = self.fontePadrao
        self.ConfirmaSenha["show"] = "*"
        self.ConfirmaSenha.pack(side=LEFT)

        self.autenticar = Button(self.sextoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.Cadastro
        self.autenticar.pack()

        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def Cadastro(self):
        user = User()
        user.username = self.nome.get()
        user.password = self.senha.get()
        confirmPassword = self.ConfirmaSenha.get()
        if confirmPassword != user.password:
            self.mensagem["text"] = "Confirmação de senha invalida!"
        else:
            user.email = self.email.get()
            cod = auth.create_account(user)
            if cod == 1:
                self.mensagem["text"] = "Conta de usuário já existe!"
            elif cod == 2:
                self.mensagem["text"] = "Email já cadastrado!"
            else:
                self.mensagem["text"] = "Usuário criado com sucesso!"

root = Tk()
Application(root)
root.mainloop()
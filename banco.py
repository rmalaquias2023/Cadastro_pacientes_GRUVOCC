import sqlite3

def __init__(self):
    self.conexao = sqlite3.connect('banco_pacientes.sqlite3')
    self.createTable()

def createTable(self):
    c = self.conexao.cursor()

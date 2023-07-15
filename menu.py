from tkinter import *
from openpyxl import workbook

class Application: 
    def __init__(self, master=None):
        self.fonte = ("Arial", "8")
        self.container1 = Frame(master)
        self.container1 ["pady"] = 20
        self.container1.pack() 
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 20
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 20
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 20
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 20
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 20
        self.container6.pack()

        self.titulo = Label (self.container1, text = 'Programa para controle de pacientes')
        self.titulo['font'] = ('Arial', '28', 'bold')
        self.titulo.pack()

        self.btnBuscar = Button(self.container2, text="Cadastrar Paciente", font=self.fonte, width=50)
        self.btnBuscar["command"] = print('hello')
        self.btnBuscar.pack(side=RIGHT)

        self.btnBuscar = Button(self.container3, text="Pesquisar Paciente", font=self.fonte, width=50)
        self.btnBuscar["command"] = print('hello')
        self.btnBuscar.pack(side=RIGHT)

        self.btnBuscar = Button(self.container4, text="Alterar Cadastro", font=self.fonte, width=50)
        self.btnBuscar["command"] = print('hello')
        self.btnBuscar.pack(side=RIGHT)

        self.btnBuscar = Button(self.container6, text="Fazer relação dos pacientes", font=self.fonte, width=50)
        self.btnBuscar["command"] = print('hello')
        self.btnBuscar.pack(side=RIGHT)


root = Tk()
root.title('Grupo de Voluntários de Combate ao Câncer de Cerqueira Cesar')
root.iconphoto = True
root.iconbitmap('**\logo\logo1.png')
#root.geometry('800x600')
Application(root)

root.mainloop()
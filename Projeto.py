import tkinter as tk
from tkinter import ttk
import datetime as dt
#import pandas as pd

def janela_cadastro_tecnicos():
    cadastro_tecnicos = tk.Toplevel()
    cadastro_tecnicos.title('Cadastro dos Técnicos')

    label_cpf = tk.Label(cadastro_tecnicos, text='CPF')
    label_cpf.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan = 2)
    entry_cpf = tk.Entry(cadastro_tecnicos)
    entry_cpf.grid(row=1, column=3, padx=10, pady=10, sticky='nswe', columnspan = 2)

    label_nome = tk.Label(cadastro_tecnicos, text='Nome')
    label_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan = 2)
    entry_nome = tk.Entry(cadastro_tecnicos)
    entry_nome.grid(row=2,column=3, padx=10, pady=10, sticky='nswe', columnspan = 2)

    label_telefone = tk.Label(cadastro_tecnicos, text='Telefone de Contato')
    label_telefone.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_telefone = tk.Entry(cadastro_tecnicos)
    entry_telefone.grid(row=3, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_turno = tk.Label(cadastro_tecnicos, text='Turno de Trabalho')
    label_turno.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_turno = tk.Entry(cadastro_tecnicos)
    entry_turno.grid(row=4, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_equipe = tk.Label(cadastro_tecnicos, text='Equipe de Trabalho')
    label_equipe.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_equipe = tk.Entry(cadastro_tecnicos)
    entry_equipe.grid(row=5, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)



def janela_cadastro_ferramentas():
    Cadastro_De_Ferramentas = tk.Toplevel()
    Cadastro_De_Ferramentas.title('Cadastro de Ferramentas')

    label_codigo_ferramenta = tk.Label(Cadastro_De_Ferramentas, text='Código da Ferramenta')
    label_codigo_ferramenta.grid(row =1, column= 0, padx=10, pady=10, sticky= 'nswe', columnspan=2)
    entry_codigo_ferramenta = tk.Entry(Cadastro_De_Ferramentas)
    entry_codigo_ferramenta.grid(row=1, column= 3, padx=10, pady =10, sticky='nswe', columnspan=2)

    label_descricao_ferramenta = tk.Label(Cadastro_De_Ferramentas, text='Descrição da Ferramenta')
    label_descricao_ferramenta.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_descricao_ferramenta = tk.Entry(Cadastro_De_Ferramentas)
    entry_descricao_ferramenta.grid(row=2, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_fabricante = tk.Label(Cadastro_De_Ferramentas, text='Fabricante')
    label_fabricante.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_fabricante = tk.Entry(Cadastro_De_Ferramentas)
    entry_fabricante.grid(row=3, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_voltagem_uso = tk.Label(Cadastro_De_Ferramentas, text='Voltagem de Uso')
    label_voltagem_uso.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_voltagem_uso = tk.Entry(Cadastro_De_Ferramentas)
    entry_voltagem_uso.grid(row=4, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_part_number = tk.Label(Cadastro_De_Ferramentas, text='Part Number')
    label_part_number.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_part_number = tk.Entry(Cadastro_De_Ferramentas)
    entry_part_number.grid(row=5, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_tamanho = tk.Label(Cadastro_De_Ferramentas, text='Tamanho da Ferramenta')
    label_tamanho.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_tamanho = tk.Entry(Cadastro_De_Ferramentas)
    entry_tamanho.grid(row=6, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_unidade_medida = tk.Label(Cadastro_De_Ferramentas, text='Unidade de Medida')
    label_unidade_medida.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_unidade_medida = tk.Entry(Cadastro_De_Ferramentas)
    entry_unidade_medida.grid(row=7, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_tipo_ferramenta = tk.Label(Cadastro_De_Ferramentas, text='Tipo da Ferramenta')
    label_tipo_ferramenta.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_tipo_ferramenta = tk.Entry(Cadastro_De_Ferramentas)
    entry_tipo_ferramenta.grid(row=8, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    label_material_ferramenta = tk.Label(Cadastro_De_Ferramentas, text='Material da Ferramenta')
    label_material_ferramenta.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_material_ferramenta = tk.Entry(Cadastro_De_Ferramentas)
    entry_material_ferramenta.grid(row=9, column=3, padx=10, pady=10, sticky='nswe', columnspan=2)

    #botao_salvar_cadastro_ferramenta = tk.Button(Cadastro_De_Ferramentas, text='Salvar Cadastro', command=salvar_cadastro_ferramenta)
    #botao_salvar_cadastro_ferramenta.grid(row=10, column=2, padx=10, pady=10, sticky='nswe' , columnspan=2)


janela = tk.Tk()

# Titulo da Janela

janela.title('Sistema da Central de Ferramentas')

label_descricao = tk.Label(text='Tela De Solicitação de Ferramentas')
label_descricao.grid(row=1, column=0, padx= 10, pady=10, sticky='nswe', columnspan=4)

botao_cadastro_ferramenta = tk.Button(janela, text='Cadastro de Ferramentas', command= janela_cadastro_ferramentas)
botao_cadastro_ferramenta.grid(row=2, column=0, padx=10, pady=10, sticky='nswe' , columnspan=2)

botao_cadastro_tecnicos = tk.Button(janela, text='Cadastro dos Técnico', command=janela_cadastro_tecnicos)
botao_cadastro_tecnicos.grid(row=3, column=0, padx=10, pady=10, sticky='nswe' , columnspan=2)
janela.mainloop()

print(salvar_cadastro_ferramenta)

import tkinter as tk
from tkinter import ttk
from list.Alemanha import *
from list.EstadosUnidos import *
from list.Franca import *
from list.Italia import *
from list.Japan import *
from list.UK import *
from list.UniaoSovietica import *
from Functions.person import PersonGenerator

# Dicionários para mapear países a suas listas de nomes e sobrenomes
countries = {
    "Alemanha": (german_names, german_surnames),
    "Japão": (japanese_names, japanese_surnames),
    "Estados Unidos": (american_names, american_surnames),
    "UK": (uk_names, uk_surnames,),
    "União Soviética": (union_names, union_surnames),
    "França": (french_names, french_surnames),
    "Itália": (italian_names, italian_surnames),
}
citys = {
    "Alemanha": (german_citys),
    "Japão": (japan_citys),
    "Estados Unidos": (american_citys),
    "UK": (uk_citys),
    "União Soviética": (union_citys),
    "França": (french_citys),
    "Itália": (italy_citys),
}

# Criação da janela principal
app = tk.Tk()
app.title("Gerador de Nomes e Registros")
app.minsize(width=750, height=285)
app.maxsize(width=750, height=285)

# Barra Menu
barra_menu = tk.Menu(app)

# Menu arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Sair", command=app.quit)
menu_arquivo.add_command(label="Salvar em .txt", command=app.quit)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Janela que exibe o menu de arquivo
app.config(menu=barra_menu)

# Criando o dropdown list de países
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(app, textvariable=country_var, state="readonly")
country_dropdown["values"] = list(countries.keys())
country_dropdown.current(0)
country_dropdown.pack()

# Rótulo para exibir nome
label_name = tk.Label(app, text="", font=("Arial", 16))
label_name.pack()
 
#Rotulo para exibir idade
label_idade = tk.Label(app,text="", font=("Arial",14))
label_idade.pack()

#Rotulo para exibir data de nascimento
label_data_ano = tk.Label(app,text="", font=("Arial",12))
label_data_ano.pack()

# Rótulo para exibir tipo sanguineo
label_sangue = tk.Label(app, text="", font=("Arial", 12))
label_sangue.pack()

# Rotulo para exibir o estado e a cidade
label_city = tk.Label(app, text="",font=("Arial", 12))
label_city.pack()

# Chamada de classe para modulos de geração de personagem
person_generator = PersonGenerator(countries, country_var, label_name, label_idade, label_data_ano, label_sangue, label_city, citys)

botao_gerar_nome = tk.Button(app, text="Gerar Nome", command=person_generator.generate_name)
botao_gerar_nome.place(x=15, y=30)

botao_gerar_idade = tk.Button(app, text="Gerar Idade", command=person_generator.generate_age)
botao_gerar_idade.place(x=15, y=60)

botao_gerar_sangue = tk.Button(app, text="Tipo Sanguineo", command=person_generator.generate_blood)
botao_gerar_sangue.place(x=15, y=90)

# Rótulo para exibir nome
label_name = tk.Label(app, text="", font=("Arial", 16))
label_name.pack()
 
#Rotulo para exibir idade
label_idade = tk.Label(app,text="", font=("Arial",14))
label_idade.pack()

#Rotulo para exibir data de nascimento
label_data_ano = tk.Label(app,text="", font=("Arial",12))
label_data_ano.pack()

# Rótulo para exibir tipo sanguineo
label_sangue = tk.Label(app, text="", font=("Arial", 12))
label_sangue.pack()

# Rotulo para exibir o estado e a cidade
label_city = tk.Label(app, text="",font=("Arial", 12))
label_city.pack()

# Botão que gera a cidade de forma aleatoria
button_estado = tk.Button(app,text="Gerar Local", command=person_generator.select_random_state_city)
button_estado.place(x=15, y=120)

# Botão para sair da aplicação
quit_button = tk.Button(app, text="Sair", command=app.quit)
quit_button.pack()

# Inicializando a aplicação
app.mainloop()

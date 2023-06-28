import tkinter as tk
import random
from tkinter import ttk
from Alemanha import *
from EstadosUnidos import *
from Italia import *
from Japan import *
from UK import *
from UniaoSovietica import *
from Franca import *

# Dicionários para mapear países a suas listas de nomes e sobrenomes
countries = {
    "Alemanha": (german_names, german_surnames),
    "Japão": (japanese_names, japanese_surnames),
    "Estados Unidos": (american_names, american_surnames),
    "UK": (uk_names, uk_surnames,),
    "União Soviética": (ussr_names, ussr_surnames),
    "França": (french_names, french_surnames),
    "Itália": (italian_names, italian_surnames),
}
citys = {
    "Alemanha": (german_citys),
    "Japão": (japan_citys),
    "Estados Unidos": (american_citys),
    "UK": (uk_citys),
    "União Soviética": (ussr_citys),
    "França": (french_citys),
    "Itália": (italy_citys),
}

# Função para gerar nomes
def generate_name():
    selected_country = country_var.get()
    name_list, surname_list = countries[selected_country]
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    label_name.config(text=f"{name} {surname}")

def select_random_state_city():
    selected_country = country_var.get()
    cities_list = citys[selected_country]
    city = random.choice(cities_list)
    label_city.config(text=f"{city}")

def copy_to_clipboard():
    # Get the values of all the labels
    name = label_name.cget("text")
    age = label_idade.cget("text")
    blood_type = label_sangue.cget("text")
    aniversario = label_data_ano.cget("text")
    cidade = label_city.cget("text")

    # Create a string with all the information
    info = f"Name: {name}\nAge: {age}\nBlood Type: {blood_type}\nData Aniversario: {aniversario}\nCidade Natal: {cidade}"

    # Copy the information to the clipboard
    app.clipboard_clear()
    app.clipboard_append(info)

    # Display a message to confirm that the information has been copied
    message_label.config(text="Information copied to clipboard!")

def generate_age():
    ano_atual = random.randint(1939,1945)
    idade = random.randint(18,40)
    ano_nascimento= ano_atual - idade
    mes_nascimento = random.randint(1,12)        
    label_idade["text"] = f"Idade: {idade}"   
       
    # Verificação de numero maximo  de dias por mês
    if mes_nascimento == 2: #Fevereiro
        if ano_nascimento % 4 == 0: # Bissexto
            dia_max = 29
        else: 
            dia_max = 28
    elif mes_nascimento in [4,6,9,12]:
        dia_max = 30
    else:
        dia_max = 31

    dia_nascimento = random.randint(1,dia_max)
    
    label_data_ano["text"] = f"Data de Nascimento: {dia_nascimento} / {mes_nascimento} / {ano_nascimento}"
    
    return idade, dia_nascimento, mes_nascimento

# Função para gerar tipo sanguineo
def generate_blood():
 tipo_sangue=["O+","O-","A+","A-","B+","B-","AB+","AB-"]   
 blood = random.choice(tipo_sangue) 
 label_sangue["text"]= f"Tipo sanguinio : {blood}"   
        
# Criação da janela principal
app = tk.Tk()
app.title("Gerador de Nomes e Registros")
app.minsize(width=750, height=750)
app.maxsize(width=750, height=750)

# Barra Menu
barra_menu = tk.Menu(app)
tk.Menu(barra_menu)

# Comandos do Menu Arquivo  
def opcao2():
    print("Opção 2 selecionada")

def create_menu(app, countries, opcao2):
    # Menu arquivo
    barra_menu = tk.Menu(app)
    menu_arquivo = tk.Menu(barra_menu, tearoff=0)
    menu_arquivo.add_command(label="Salvar como", command=opcao2)
    menu_arquivo.add_command(label="Sair", command=app.quit)

    # Adicionar os menus a barra de menu
    barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Janela que exibe o menu de arquivo
app.config(menu=barra_menu)

# Criando o dropdown list de países
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(app, textvariable=country_var, state="readonly")
country_dropdown["values"] = list(countries.keys())
country_dropdown.current(0)
country_dropdown.pack()

# Botão para gerar nomes
botao_gerar_nome = tk.Button(app, text="Gerar Nome", command=generate_name)
botao_gerar_nome.place(x=15, y=30)

    # Botão para gerar idade
botao_gerar_idade = tk.Button(app, text="Gerar Idade", command=generate_age)
botao_gerar_idade.place(x=15, y=60)

# Botão para gerar tipo sanguineo
botao_gerar_sangue = tk.Button(app, text="Tipo Sanguineo", command=generate_blood)
botao_gerar_sangue.place(x=15, y=90)

# Create the button to copy the information to the clipboard
button_copy = tk.Button(app, text="Copiar", command=copy_to_clipboard)
button_copy.place(x=15, y=150)

# Botão que gera a cidade de forma aleatoria
button_estado = tk.Button(app,text="Gerar Local", command=select_random_state_city)
button_estado.place(x=15, y=120)

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

# Create a label to display a message when the information is copied to the clipboard
message_label = tk.Label(app, text="")
    
# Botão para sair da aplicação
quit_button = tk.Button(app, text="Sair", command=app.quit)
quit_button.pack()

# Inicializando a aplicação
app.mainloop()
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from list.Alemanha import *
from list.Japan import *
from list.EstadosUnidos import *
from list.Franca import *
from list.Italia import *
from list.UK import *
from list.UniaoSovietica import *
import random
from tkinter import filedialog

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

# Função que gera o nome aleatorio baseado no pais selecionado
def generate_name():
    selected_country = country_var.get()
    name_list, surname_list = countries[selected_country]
    name = random.choice(name_list)
    surname = random.choice(surname_list)
    full_name = f"{name} {surname}"
    label_name.config(text=full_name)
    return full_name

# Função que copia os dados para a area de transferencia
def copy_to_clipboard():
    # Pega os valores das Labels
    name = label_name.cget("text")
    age = label_idade.cget("text")
    blood_type = label_sangue.cget("text")
    aniversario = label_data_ano.cget("text")
    cidade = label_city.cget("text")

    # Cria uma string com todas as labels
    info = f"Name: {name}\nAge: {age}\nBlood Type: {blood_type}\nData Aniversario: {aniversario}\nCidade Natal: {cidade}"
   
    # Copia as informações para a area de transferencia
    app.clipboard_clear()
    app.clipboard_append(info)

    # Mostra que as informações foram copiadas com sucesso 
    message_label.config(text="Information copied to clipboard!")

# FUnção que gera uma idade aleatoria   
def generate_age():
    ano_atual = random.randint(1939,1945)
    idade = random.randint(18,40)
    ano_nascimento = ano_atual - idade
    mes_nascimento = random.randint(1,12)        
    label_idade["text"] = f"Idade: {idade}"  
     # Verificação de numero maximo  de dias por mês
    if mes_nascimento == 2: #Fevereiro
        if ano_nascimento % 4 == 0 and (ano_nascimento % 100 != 0 or ano_nascimento % 400 == 0): # Bissexto
            dia_max = 29
        else:
            dia_max = 28
    elif mes_nascimento in [4,6,9,11]:
        dia_max = 30
    else:
        dia_max = 31
    dia_nascimento = random.randint(1,dia_max)
    label_data_ano["text"] = f"Data de Nascimento: {dia_nascimento} / {mes_nascimento} / {ano_nascimento}"
    return idade, dia_nascimento, mes_nascimento

# Gera um tipo sanguinio aleatório
def generate_blood():
    tipo_sangue=["O+","O-","A+","A-","B+","B-","AB+","AB-"]  
    blood = random.choice(tipo_sangue)
    label_sangue["text"]= f"Tipo sanguinio : {blood}"  
    return generate_blood

#Escolhe um cidade aleatorio
def select_random_state_city():
    selected_country = country_var.get()
    cities_list = citys[selected_country]
    city = random.choice(cities_list)
    label_city.config(text=city)
    return city

def save_to_file():
    # Pega os dados das labels
    name = label_name.cget("text")
    age = label_idade.cget("text")
    blood_type = label_sangue.cget("text")
    aniversario = label_data_ano.cget("text")
    cidade = label_city.cget("text")

    # Cria uma string com todas as informações 
    info = f"Name: {name}\nAge: {age}\nBlood Type: {blood_type}\nData Aniversario: {aniversario}\nCidade Natal: {cidade}"
   
    # Pergunta ao usuario aonde quer salvar
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
   
    # Salva as informações no arquivo selecionados
    if file_path:
        with open(file_path, 'w') as file:
            file.write(info)
       
        # Mostra uma mensagem que o arquvi foi salvo
        messagebox.showinfo(title="Information saved", message=f"Information saved to {file_path}!")
       

# Criação da janela principal
app = tk.Tk()
app.title("Gerador de Nomes e Registros")
app.minsize(width=750, height=285)
app.maxsize(width=750, height=285)

# Barra Menu
barra_menu = tk.Menu(app)

# Menu arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Salvar como", command=save_to_file)
menu_arquivo.add_command(label="Sair", command=app.quit)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Adicionar os menus a barra de menu
menu_army = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Army", menu=menu_army)

menu_air_force = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Air Force", menu=menu_air_force)

menu_navy = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Navy", menu=menu_navy)


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

# Cria um botão para copias as informações
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
message_label.pack()

# Botão para sair da aplicação
quit_button = tk.Button(app, text="Sair", command=app.quit)
quit_button.pack()

# Inicializando a aplicação
app.mainloop()
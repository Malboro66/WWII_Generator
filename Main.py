import tkinter as tk

# Criação da janela principal
app = tk.Tk()
app.title("WWII Pilot Manager")
app.minsize(width=750, height=285)
app.maxsize(width=750, height=285)

# Barra Menu
barra_menu = tk.Menu(app)

# Menu arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Sair", command=app.quit)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Adicionar os menus a barra de menu
menu_generator = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Pilot Generator", menu=menu_generator)

menu_profile = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ver Pilotos", menu=menu_profile)

menu_act = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Activity", menu=menu_act)

# Janela que exibe o menu de arquivo
app.config(menu=barra_menu)

# Cria um rótulo com o título da tela
title_label = tk.Label(app, text="Bem-vindo ao Gerenciador de Pilotos", font=("Helvetica", 16))
title_label.pack(pady=10)

# Cria botões para as opções do menu
view_pilots_button = tk.Button(app, text="Ver Pilotos", width=20)
view_pilots_button.pack(pady=5)

add_pilot_button = tk.Button(app, text="Adicionar Piloto", width=20)
add_pilot_button.pack(pady=5)

edit_pilot_button = tk.Button(app, text="Editar Piloto", width=20)
edit_pilot_button.pack(pady=5)

delete_pilot_button = tk.Button(app, text="Excluir Piloto", width=20)
delete_pilot_button.pack(pady=5)

# Botão para sair da aplicação
quit_button = tk.Button(app, text="Sair", command=app.quit)
quit_button.pack()

# Inicializando a aplicação
app.mainloop()
import tkinter.messagebox as messagebox
from tkinter import filedialog

class Clipboard:
    def __init__(self, app, name, idade, sangue, data_ano, cidade, message_label):
        self.app = app
        self.name = name
        self.idade = idade
        self.sangue = sangue
        self.data_ano = data_ano
        self.cidade = cidade
        self.message_label = message_label

    def copy_to_clipboard(self):
        # Create a string with all the information
        info = f"Name: {self.name}\nAge: {self.idade}\nBlood Type: {self.sangue}\nData Aniversario: {self.data_ano}\nCidade Natal: {self.cidade}"
   
        # Copy the information to the clipboard
        self.app.clipboard_clear()
        self.app.clipboard_append(info)

        # Display a message to confirm that the information has been copied
        self.message_label.config(text="Information copied to clipboard!")

    def save_to_file(self):
        # Create a string with all the information
        info = f"Name: {self.name}\nAge: {self.idade}\nBlood Type: {self.sangue}\nData Aniversario: {self.data_ano}\nCidade Natal: {self.cidade}"
   
        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
   
        # Save the information to the selected file
        if file_path:
            with open(file_path, 'w') as file:
                file.write(info)
       
            # Display a message to confirm that the information has been saved
            messagebox.showinfo(title="Information saved", message=f"Information saved to {file_path}!")

import random

class PersonGenerator:
    def __init__(self, countries, country_var, label_name, label_idade, label_data_ano, label_sangue, label_city, citys):
        self.countries = countries
        self.country_var = country_var
        self.label_name = label_name
        self.label_idade = label_idade
        self.label_data_ano = label_data_ano
        self.label_sangue = label_sangue
        self.label_city = label_city
        self.citys = citys

    def generate_name(self):
        selected_country = self.country_var.get()
        name_list, surname_list = self.countries[selected_country]
        name = random.choice(name_list)
        surname = random.choice(surname_list)
        full_name = f"{name} {surname}"
        self.label_name.config(text=full_name)
        return full_name

    def generate_age(self):
        ano_atual = random.randint(1939,1945)
        idade = random.randint(18,40)
        ano_nascimento = ano_atual - idade
        mes_nascimento = random.randint(1,12)        
        self.label_idade["text"] = f"Idade: {idade}"  
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
        self.label_data_ano["text"] = f"Data de Nascimento: {dia_nascimento} / {mes_nascimento} / {ano_nascimento}"
        return idade, dia_nascimento, mes_nascimento

    def generate_blood(self):
        tipo_sangue=["O+","O-","A+","A-","B+","B-","AB+","AB-"]  
        blood = random.choice(tipo_sangue)
        self.label_sangue["text"]= f"Tipo sanguinio : {blood}"  
        return blood

    def select_random_state_city(self):
        selected_country = self.country_var.get()
        cities_list = self.citys[selected_country]
        city = random.choice(cities_list)
        self.label_city.config(text=city)
        return city
   
import re
from datetime import datetime

class MakeClient:
    def __init__(self, clients:list = []):
        self.clients = clients
        self.client = {"address": {}, "accounts": []}

    def name(self) -> bool:
        name = input("Nome: ")

        if not name:
            print("Digite seu nome!")
            return False

        self.client["name"] = name
        return True
            

    def cpf(self) -> bool:
        cpf = input("CPF: ")

        if not cpf:
            print("Digite seu CPF!")
            return False

        numeric_only = re.sub(r"\D", "", cpf)

        if len(numeric_only) != 11 and cpf:
            print("CPF inválido! Digite os 11 digitos (000.000.000-00)!")
            return False

        existing_cpf = False
        for value in self.clients:
            if value["cpf"] == numeric_only:
                print("Cliente ja possue cadastro!")
                existing_cpf = True
                break

        if existing_cpf:
            return False
            
        self.client["cpf"] = numeric_only
        return True

    def birth(self) -> bool:
        birth = input("Data de nascimento: ")

        if not birth:
            print("Digite a data de nascimento!")
            return False
    
        numeric_only = re.sub(r"\D", "", birth)

        if birth and len(numeric_only) != 8:
            print("Data inválida! Digite os 8 digitos (dd/mm/aaaa)!")
            return False

        try:
            birth = datetime.strptime(numeric_only, "%d%m%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida!")
            return False
            
        if birth and len(birth) == 10:
            self.client["birth"] = birth
            return True
        
    def address(self) -> bool:
        street = input("\n================ Endereço ================\nRua: ")
        if not street:
            print("O preenchimento do nome da rua é obrigatorio!")
            return False

        self.client["address"]["street"] = street
    
        number = input("Número: ")
        if not number:
            print("O preenchimento do número da residencia é obrigatorio!")
            return False

        self.client["address"]["number"] = number
    
        neighborhood = input("Bairro: ")
        if not neighborhood:
            print("O preenchimento do bairro é obrigatorio!")
            return False
    
        self.client["address"]["neighborhood"] = neighborhood

        city = input("Cidade: ")
        if not city:
            print("O preenchimento da cidade é obrigatorio!")
            return False
    
        self.client["address"]["city"] = city

        state_acronym = input("Sigla do Estado: ")
        if not state_acronym:
            print("O preenchimento da sigla do estado é obrigatorio!")
            return False

        letters_only = re.sub(r"[^A-Za-z]", "", state_acronym)
        if len(letters_only) != 2:
            print("Sigla inválida! Digite apenas 2 letras (AA)!")
            return False

        letters_only = letters_only.upper()
        self.client["address"]["state_acronym"] = letters_only
        return True

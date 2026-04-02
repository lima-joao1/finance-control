from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from time import sleep


obj = Despesa(100, "education", "26/06/2026", "escola do luquinhas")
print(obj)
print(obj.get_value())

control = ControleFinanceiro()
education = Categoria("Educação", 3000)


def get_command():
    print("*******  Controle Financeiro *******")
    print("""
        1 - Adicionar nova despesa
        2 - Checar despesas\n""")

    return int(input("Digite uma opção [1, 2]: "))

categories_tracker = []

def command_manager(command):
    choices = {1 : "Educação",
        2 : "Energia",
        3 : "Água",
        4 : "Internet",
        5 : "Alimentação",
        6 : "Transporte",
        7 : "Residência",
        8 : "Entretenimento"}


    if (command == 1):
        print("""
        1 - Educação
        2 - Energia
        3 - Água
        4 - Internet
        5 - Alimentação
        6 - Transporte
        7 - Residência
        8 - Entretenimento
        """)

        choice = int(input("Escolha um tipo de despesa [1, 8]: "))        

        while choice not in choices.keys():
            print("Escolha inválida. Tente novamente.")
            choice = int(input("Escolha um tipo de despesa [1, 8]: "))
            
        category_name = choices[choice]


        if category_name not in control.get_dictionary().keys():
            print(f"O dicionário que associa nome da categoria a um obj de categoria não tem {category_name}")
            print("Criando novo objeto da classe categoria e adicionando-o ao dicionário:")
            print("Categoria ainda não registrada.")
            limit = int(input(f"Limite mensal de gastos com {category_name.lower()}: R$ "))
            category = Categoria(category_name, limit)
            control.add_category(category_name, category)

        else:
            print("Categoria já cadastrada. Resgatando...")
            for category_key, category_value in control.get_dictionary().items():
                if (category_key == category_name):
                    category = category_value


        value = int(input("Valor da despesa: R$ "))
        date = input("Data da despesa: (DD/MM/YYYY): ")
        description = input("Descrição da despesa: ") # creche do juninho

        expense = Despesa(value, category_name, date, description)
        category.add_expense(value) # tem que registrar objeto da classe despesa na real

while True:
    command = get_command()
    if (command == 0):
        break
    command_manager(command)
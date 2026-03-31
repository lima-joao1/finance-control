from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from CategoriaArchive import CategoriaArchive
from time import sleep


obj = Despesa(100, "education", "26/06/2026", "escola do luquinhas")
print(obj)
print(obj.get_value())

control = ControleFinanceiro()
cat_archive = CategoriaArchive()
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
            
        if (choices[choice] not in cat_archive.show_names()):
            print("Categoria não cadastrada.")
            print("Iniciando cadastro...\n")
            sleep(3)
            limit = int(input(f"Digite o limite de gastos mensal para {choices[choice].lower()}: R$ "))
            category = Categoria(choices[choice], limit)
            cat_archive.add_category(category)

        category = Categoria(choices[choice], limit)


        value = int(input("Digite o valor da despesa: R$ "))
        category.add_expense(value)

        date = input("Digite a data da despesa (DD/MM/YYYY): ")

        description = input("Adicione uma breve descrição da despesa: ") # ex.: creche do juninho

        expense = Despesa(value, choices[choice], date, description)
        

        control.add_category(choices[choice], expense)
        control.show_categories()





while True:
    command = get_command()
    if (command == 0):
        break
    command_manager(command)
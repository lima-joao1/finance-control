from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from Usuario import Usuario

control = ControleFinanceiro()

def get_command():
    print("*******  Controle Financeiro *******")
    print("""
        1 - Adicionar nova despesa
        2 - Checar histórico mensal
        3 - Começar novo mês
        4 - Histórico completo\n
        
        0 - Fechar programa""")

    return int(input("Digite uma opção [0, 4]: "))

def command_manager(command, user):
    
    if (command == 1):

        choices = {1 : "Educação",
        2 : "Energia",
        3 : "Água",
        4 : "Internet",
        5 : "Alimentação",
        6 : "Transporte",
        7 : "Residência",
        8 : "Entretenimento"}

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

        category = register_category_or_retrieve(category_name)

        value = int(input("Valor da despesa: R$ "))
        date = input("Data da despesa: (DD/MM/YYYY): ")
        description = input("Descrição da despesa: ") # creche do juninho

        expense = Despesa(value, category_name, date, description)
        category.add_expense(expense, user) # tem que registrar objeto da classe despesa na real

        control.save()

# "Educação" : {category_object} -> objeto tem um array que com múltiplos objetos da classe despesa

def register_category_or_retrieve(category_name):
        
        if category_name not in control.get_dictionary().keys():
            print("Categoria ainda não registrada. Cadastrando...")
            limit = int(input(f"Limite mensal de gastos com {category_name.lower()}: R$ "))
            category = Categoria(category_name, limit)
            control.add_category(category_name, category)

        else:
            for category_key, category_value in control.get_dictionary().items():
                if (category_key == category_name):
                    category = category_value
    
        return category

user_name = input("Digite o nome do usuário: ")
user_mail = input("Digite o email do usuário: ")
user = Usuario(user_name, user_mail)

while True:

    command = get_command()
    if (command == 0):
        break
    command_manager(command, user)
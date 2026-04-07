from Despesa import Despesa
from Categoria import Categoria
from ControleFinanceiro import ControleFinanceiro
from Usuario import Usuario
from time import sleep

def get_command():
    print("*******  Controle Financeiro *******")
    print("""
        1 - Adicionar nova despesa
        2 - Checar histórico mensal
        3 - Gerar PDF
        4 - Limpar histórico mensal\n 
        
        0 - Fechar programa""") # Perguntar, quando for gerar PDF, se deseja gerar apenas do mês atual ou de todos os meses.

    return int(input("Digite uma opção [0, 3]: "))

def command_manager(command, user):
    
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

        register_new_expense(user)
    
    elif (command == 2):
        print("\n**** Histórico Mensal ****\n")
        for category_name, category_object in control.get_dictionary().items():
            print(f"{category_name} - Limite: R$ {category_object.get_limit():.2f}")
            for expense in category_object.get_expenses():
                print(f"    - {expense.get_description()} | {expense.get_date()} | Custo: R$ {expense.get_value():.2f}")
            
            if (category_object.get_total_spent() > category_object.get_limit()):
                print(f"\n  Total gasto: R$\033[31m {category_object.get_total_spent():.2f}\033[0m")
                print(f"    Você gastou R$ {(category_object.get_total_spent() - category_object.get_limit()):.2f} acima do limite.")
            else:
                print(f"\n  Total gasto: R$\033[92m {category_object.get_total_spent():.2f}\033[0m")

            print()
        
    elif (command == 3):
        print("Enviando PDF para o e-mail registrado...")
        control.import_to_pdf(user)

    elif (command == 4):
        print("Limpando histórico...")
        control.clear()
        print("Histórico limpo para começar um novo mês...")
        sleep(3)

# "Educação" : {category_object} -> objeto tem um array que com múltiplos objetos da classe despesa

def register_new_expense(user):
    choices = {1 : "Educação",
        2 : "Energia",
        3 : "Água",
        4 : "Internet",
        5 : "Alimentação",
        6 : "Transporte",
        7 : "Residência",
        8 : "Entretenimento"}
    
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

control = ControleFinanceiro()

while True:

    command = get_command()
    if (command == 0):
        break
    command_manager(command, user)
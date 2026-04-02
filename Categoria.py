class Categoria: # Cada objeto da classe Categoria é um literal de categoria de despesa. P/ um objeto com nome "Educação", tens um limite mensal de gastos e uma lista com todos os gastos.

    def __init__(self, name, limit):
        self.__name = name
        self.__limit = limit
        self.__expenses = []
    
    def get_name(self):
        return self.__name
    
    def get_limit(self):
        return self.__limit
    
    def get_expenses(self):
        return self.__expenses
    
    def check_overspent(self):

        if (sum(self.__expenses) == self.__limit):
            print("Você já gastou tudo que podia. Nem mais um centavo!\n")

        elif (sum(self.__expenses) > self.__limit):

            overspent = sum(self.__expenses) - self.__limit

            print("Seu limite de gastos na categoria é de R$%.2f e você gastou R$%.2f" % (self.__limit, sum(self.__expenses)))
            print("Você já gastou R$%.2f acima do total.\n" % (overspent))
        
        else:
            print("Seu limite é de R$%.2f e você já gastou R$%.2f." % (self.__limit, sum(self.__expenses)))
            print("Você está dentro do limite de gastos e ainda pode gastar R$%.2f\n" % (self.__limit - sum(self.__expenses)))

    def add_expense(self, value):
        self.__expenses.append(value)
        
        self.check_overspent()
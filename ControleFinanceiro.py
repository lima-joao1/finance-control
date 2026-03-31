class ControleFinanceiro:

    def __init__(self):
        self.__categories = {}

    def add_category(self, category_name, category_object):
        # Sempre que adicionar uma despesa com mesma key, vai dar overwrite na passada. 
        # Fazer então que o value não é um objeto de Despesa, mas um array de objetos Despesa

        if (category_name not in self.__categories.keys()):
            self.__categories[category_name] = []
            self.__categories[category_name].append(category_object)
        else:
            self.__categories[category_name].append(category_object)
            
    def show_categories(self):
        for key, value in self.__categories.items():
            print(f"{key} : {value}")

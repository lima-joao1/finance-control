class ControleFinanceiro:

    def __init__(self):
        self.__categories = {}

    def add_category(self, category_name, category_object):
        self.__categories[category_name] = category_object
            
    def show_categories(self):
        for key, value in self.__categories.items():
            print(f"{key} : {value}")

    def get_dictionary(self):
        return self.__categories

    def get_values_names(self): # dicionário com key string (nome da categoria) associa value que é instância da categoria
        values = []
        for value in self.__categories.values():
            values.append(value.get_name())

        return values

    def show_names(self):
        names = []
        for category in self.__categories_list:
            names.append(category.get_name())
        return names
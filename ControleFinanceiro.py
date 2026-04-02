import json
from Categoria import Categoria
from Despesa import Despesa

class ControleFinanceiro:

    def __init__(self):
        self.__categories = {}
        self.__history = [] # p/ manter o tracking de meses anteriores
        self.load()

    def add_category(self, category_name, category_object):
        self.__categories[category_name] = category_object
        
    def get_dictionary(self):
        return self.__categories

    def save(self):
        current_data = {}
        for name, cat in self.__categories.items(): # p/ cada key, que são strings com o nome da categoria, pega um objeto da classe Categoria.
            expenses_list = []
            for expense in cat.get_expenses():
                expense_dict = {
                    "value": expense.get_value(),
                    "category": expense.get_category(),
                    "date": expense.get_date(),
                    "description": expense.get_description()
                }

                expenses_list.append(expense_dict)
            current_data[name] = {
                "limit": cat.get_limit(),
                "expenses": expenses_list
            }
        data = {
            "current": current_data,
            "history": self.__history
        }
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)  # aqui passa aquele dicionário gigante p/ ser usado 
            for name, cat_data in data["current"].items():
                cat = Categoria(name, cat_data["limit"])
                for expens in cat_data["expenses"]:
                    expense = Despesa(expens["value"], expens["category"] ,expens["date"] ,expens["description"])
                    cat.get_expenses().append(expense)
                self.__categories[name] = cat
                self.__history = data["history"]
        except FileNotFoundError:
            pass
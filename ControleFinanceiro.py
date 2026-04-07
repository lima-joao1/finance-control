import json
from Categoria import Categoria
from Despesa import Despesa
from fpdf import FPDF
from pdf_mail import sendpdf


class ControleFinanceiro:

    def __init__(self):
        self.__categories = {}
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
        except FileNotFoundError:
            pass
            
    def import_to_pdf(self, user):
        pdf = FPDF("L", "mm", "A4") #construtor
        pdf.add_page() # p/ ter 1 pagina
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_font('ComicSans', '', r'C:\Windows\Fonts\comic.ttf', uni=True)         # coisa só pra poder usar comicsans

        
        pdf.set_font('ComicSans', '', 40)         # sempre depois de adicionar uma page
        pdf.cell(0, 20, "Histórico Mensal", ln=True, align="C") # ai faz a cell 
        pdf.ln(10)


        pdf.set_font("ComicSans", "", 14)
        for category_name, category_object in self.__categories.items():
            pdf.cell(0, 10, f"{category_name} - Limite: R$ {category_object.get_limit()}", ln=True)
            for expense in category_object.get_expenses():
                pdf.cell(0, 10, f"    - {expense.get_description()} | R$ {expense.get_value()} | Data: {expense.get_date()}", ln=True)

            pdf.cell(0, 10, f"                     - Total gasto: R$ {category_object.get_total_spent()}")
            pdf.ln(15)

        pdf.image(r"C:\Users\joaov\Downloads\unnamed.jpg", 200, 100, 110, 110)

        pdf.output("Historico.pdf")
        self.send_pdf_email(user)
    
    def send_pdf_email(self, user):
        k = sendpdf("financecontrol999@gmail.com",
                    user.get_mail(),
                    "vhvq kxyw byyv kdke",
                    "Histórico Mensal de Controle Financeiro",
                    f"Querido {user.get_name().capitalize().strip()},\n Em anexo segue o histórico financeiro mensal requisitado.",
                    "Historico",
                    r"C:\Users\joaov\Desktop\AA2")
        k.email_send()

    def clear(self):
        self.__categories.clear()
        self.save()
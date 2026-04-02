import smtplib

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
    
    def get_total_spent(self):
        total_spent = 0

        for expense in self.__expenses:
            total_spent += expense.get_value()
        
        return total_spent

    def check_overspent(self, user):

        total_spent = self.get_total_spent()

        if (total_spent == self.__limit):
            print("Você já gastou tudo que podia. Nem mais um centavo!\n")

        elif (total_spent > self.__limit):

            overspent = total_spent - self.__limit

            print("Seu limite de gastos na categoria é de R$%.2f e você gastou R$%.2f" % (self.__limit, total_spent))
            print("Você já gastou R$%.2f acima do total.\n" % (overspent))
            
            self.send_mail(user)
        
        else:
            print("Seu limite é de R$%.2f e você já gastou R$%.2f." % (self.__limit, total_spent))
            print(f"Você está dentro do limite de gastos e ainda pode gastar R${(self.__limit - total_spent):.2f} com {self.get_name().lower()}.\n")

    def add_expense(self, expense, user):
        self.__expenses.append(expense)
        
        self.check_overspent(user)

    def send_mail(self, user):
        sender = "financecontrol999@gmail.com"
        receiver_mail = user.get_mail()
        receiver_name = user.get_name()
        password = "vhvq kxyw byyv kdke"
        subject = "Infração do limite de gastos"
        body = f"\nQuerido(a) {receiver_name.capitalize()},\nvocê ultrapassou seu teto de gastos na categoria {self.get_name().lower()}.\n" + f"Você gastou um total de R$ "+ str(self.get_total_spent()) + ", sendo que seu limite era de R$ " + str(self.get_limit())

        message = f"""From: Controle Financeiro\nTo: {receiver_name} \nSubject: {subject} \n {body}
        """

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender, password)

            server.sendmail(sender, receiver_mail, message.encode("utf-8"))
            print("Enviando e-mail de alerta...")
        except smtplib.SMTPAuthenticationError:
            print("Unable to log in.")
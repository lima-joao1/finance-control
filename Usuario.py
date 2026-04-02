class Usuario:
    def __init__(self, name, mail):
        self.__name = name
        self.__mail = mail

    def get_name(self):
        return self.__name
    
    def get_mail(self):
        return self.__mail
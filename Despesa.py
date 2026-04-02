class Despesa:

    def __init__(self, value, category, date, description):
        self.__value = value
        self.__category = category
        self.__date = date
        self.__description = description

    def get_value(self):
        return self.__value

    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date
    
    def get_description(self):
        return self.__description
    
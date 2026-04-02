class CategoriaArchive:
    def __init__(self):
        self.__categories = []

    def add_category(self, category):
        self.__categories.append(category)

    def show_names(self):
        names = []
        for category in self.__categories:
            names.append(category.get_name())
        return names
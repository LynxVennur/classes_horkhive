class Ad():
    def __init__(self, username, category, description, price):
        self.__username = username
        self.__category = category
        self.__description = description
        self.__price = float(price)
        self.__favoritos = 0
        self.__feedbacks = []

    def add_feedback(self, feedback):
        self.__feedbacks.append(feedback)

    def get_username(self):
        return self.__username

    def get_category(self):
        return self.__category

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_favoritos(self):
        return self.__favoritos

    def favoritar(self):
        self.__favoritos += 1  # Incrementar o contador de favoritos

    def get_feedbacks(self):
        return self.__feedbacks
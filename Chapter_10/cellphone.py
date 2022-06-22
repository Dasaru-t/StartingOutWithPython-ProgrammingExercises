# cellphone.py
# The CellPhone class holds data about a cell phone.

class CellPhone:

    # The _ _init_ _ method initializes the attributes.

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # The set_manufact method accepts an argument for
    # the phone's manufacturer.

    def set_manufact(self,manufact):
        self.__manufact = manufact

    # The set_model method accepts an argument for
    # the phone's model number.

    def set_model(self, model):
        self.__model = model


    # The set_retail_price method accepts an argument
    # for the phone's retail price.

    def set_retail_price(self, price):
        self.__retail_price = price
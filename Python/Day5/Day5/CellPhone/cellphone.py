class CellPhone:

    def __init__(self, manufact, model, retailprice):
        self.__manufact = manufact
        self.__model = model
        self.__retailprice = retailprice

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retailpriec(self, retailprice):
        self.__retailprice = retailprice

    def get_manufact(self):
       return self.get_manufact()

    def get_model(self):
        return self.get_model()

    def get_retailprice(self):
        return self.get_retailprice()

    # def __str__(self):
    #     return "Manufacturer:" + self.__manufact + '\n' \
    #          + "Model" + self.get_model + '\n' \
    #          + "Price" + format(self.__retailprice, ",.2f") + '\n'


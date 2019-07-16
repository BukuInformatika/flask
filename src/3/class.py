class Product:
    __vendor_message = "Ini adalah rahasia"
    name = ""
    price = ""
    size = ""
    unit = ""

    def __init__(self, name):
        print "Ini adalah constructor"
        self.name = name
        self.unit = "ml"
        self.size = 250

    def get_vendor_message(self):
        print self.__vendor_message

    def set_price(self, price):
        self.price = price
class Coffee():
    def __init__(self, name, origin, description, producer, stock, buy_price, sell_price, id = None):
        self.name = name
        self.origin = origin
        self.description = description
        self.producer = producer
        self.stock = stock 
        self.buy_price = buy_price 
        self.sell_price = sell_price 
        self.id = id

    def mark_up(self):
        if self.buy_price == 0:
            return self.sell_price * 100
        return round(((self.sell_price - self.buy_price) / self.buy_price) * 100,2)


   
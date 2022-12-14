import time

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
            return "Nothing paid for this product"
        return round(((self.sell_price - self.buy_price) / self.buy_price) * 100,2)


    def coffee_auction_countdown(self):
        duration = 60
        while duration > 0:
            time.sleep(1)
            duration -= 1
            return duration
        return "It's Auction Time!"


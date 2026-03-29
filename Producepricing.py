from abc import ABC, abstractmethod
from os import name

class Item(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def calculate_cost(self):
        pass

class ByWeightItem(Item):
    def __init__(self, name, weight, price_per_pound):
        super().__init__(name)
        self.weight = weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.weight * self.price_per_pound

class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self.quantity = quantity
        self.cost_each = cost_each

    def calculate_cost(self):
        return self.quantity * self.cost_each
    
class Grapes(ByWeightItem):
    price_per_pound = 2.5
    def __init__(self, weight):
        super().__init__("Grapes", weight, self.price_per_pound)

class Bananas(ByWeightItem):
    price_per_pound = 1.2
    def __init__(self, weight):
        super().__init__("Bananas", weight, self.price_per_pound)

class Oranges(ByQuantityItem):
    cost_each = 1
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, self.cost_each)

class Cantaloupes(ByQuantityItem):
    cost_each = 3
    def __init__(self, quantity):
        super().__init__("Cantaloupes", quantity, self.cost_each)

class Order():
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def __len__ (self):
        return len(self.items)
    
def main():
    newOrder = Order()
    newOrder.add_item(Grapes(2))
    newOrder.add_item(Bananas(3))
    newOrder.add_item(Oranges(4))
    newOrder.add_item(Cantaloupes(1))

    for item in newOrder.items:
        print(item.name, "costs", f'${item.calculate_cost():.2f}')
    
if __name__ == "__main__":
    main()
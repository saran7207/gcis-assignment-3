import random

menu = {
    "Drinks" : {
        "Cola" : 5.0,
        "Juice" : 7.0
    },
    "Entrees" : {
        "Burger" : 20.0,
        "Pizza" : 25.0 
    },
    "Sides" : {
        "Fries" : 8.0,
        "Salad" : 10.0
    }
}

class Combo:
    __slots__ = ["drink", "entree", "side", "total_price"]

    def __init__(self, drink, entree, side):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.total_price = 0.0

        for item in [drink, entree, side]:
            if item:
                for category in menu:
                    if item in menu[category]:
                        self.total_price += menu[category][item]
                        break
                        

    def get_total(self):
        return self.total_price
    
    def display_combo(self):
        return f"Drink: {self.drink} | Entree: {self.entree} | Side: {self.side} \nTotal Combo Price: {self.total_price}"
    
class Order:
    __slots__ = ["order_id", "combos", "total_amount"]

    def __init__(self, order_id):
        self.order_id = order_id
        self.combos = []
        self.total_amount = 0.0

    def add_combo(self, combo):
        self.combos.append(combo)
        self.total_amount += combo.get_total()

    def display_receipt(self):
        print(f"Reciept Order ID: {self.order_id}")
        print("-----------------------------------")
        
        for combo in range(len(self.combos)):
            print(f"Combo: {combo + 1}")
            print(f"Drink: {self.combos[combo].drink} | Entree: {self.combos[combo].entree} | Side: {self.combos[combo].side}")
            print("-----------------------------------")
            print(f"Total Amount: {self.total_amount}")
                
def main():
    while True:
        print("--- Welcome to Eat and Drink ---")
        print()
        print("Today's Menu:")
        print()
        for key in menu:
            for item in menu[key]:
                print(f"{item} - {menu[key][item]} AED")
        print()
        print("Create your combo")
        
        drink = input("Enter drink: ").capitalize()
        entree = input("Enter entree: ").capitalize()
        side = input("Enter side: ").capitalize()

        print("Order Successfully Created")
        
        combo1 = Combo(drink, entree, side)
        combo1.get_total()
        
        order1 = Order(random.randint(1, 200))
        order1.add_combo(combo1)
        order1.display_receipt()

        option = input("Do you want to order again (y/n): ").lower()
        if option == 'y':
            continue
        else:
            print("Thanks for ordering")
            break

if __name__ == "__main__":
    main() 
        
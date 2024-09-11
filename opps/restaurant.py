class Dish:

    def __init__(self,name,price,qty):

        self.name=name

        self.price=price

        self.quantity=qty

    def __str__(self):

        return self.name

class Restaurent:  

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.dishes=[]

    def add_food(self,dish):

        self.dishes.append(dish)

    def list_foods(self):

        for d in self.dishes:

            print(d)


biriyani_instance=Dish("biriyani",120,"full")
mandhi_instance=Dish("mandhi",280,"full")
shavaya_instance=Dish("shavaya",450,"full")


restaurent_instance=Restaurent("paradise","kakkanad")


restaurent_instance.add_food(mandhi_instance)

restaurent_instance.add_food(shavaya_instance)


restaurent_instance.list_foods()


restaurent_instance2=Restaurent("thamaki","vaytila")


restaurent_instance2.add_food(mandhi_instance)

restaurent_instance2.add_food(shavaya_instance)

restaurent_instance2.add_food(biriyani_instance)


restaurent_instance2.list_foods()












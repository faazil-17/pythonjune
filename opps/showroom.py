class Bike:   

    def __init__(self,name,brand,price):

        self.name=name

        self.price=price

        self.brand=brand

    def __str__(self):

        return self.name


class ShowRoom:  

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.bikes=[]

    def add_vehicle(self,bike):

        self.bikes.append(bike)

    def list_vehicles(self):

        for b in self.bikes:

            print(b)


hunter_instance=Bike("hunter","re",200000)
activa_instance=Bike("activa","hinda",100000)
dominar_instance=Bike("dominar","bajaj",120000)
himalaya_instance=Bike("himalaya","re",220000)

showroom_instance=ShowRoom("popular","kakkanad")

showroom_instance.add_vehicle(hunter_instance)

showroom_instance.add_vehicle(dominar_instance)

showroom_instance.list_vehicles()

showroom_instance2=ShowRoom("tags","thrissur")

showroom_instance2.add_vehicle(hunter_instance)
showroom_instance2.add_vehicle(activa_instance)
showroom_instance2.add_vehicle(himalaya_instance)
showroom_instance2.add_vehicle(dominar_instance)

showroom_instance2.list_vehicles()
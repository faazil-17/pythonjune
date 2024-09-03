mobiles={"name":"motoedge14","brand":"moto","price":22000,"is_available":True,"offer":500}






# for k,v in mobiles.items():

#     print(k,v)



# methods=.>>>

# get(key) return key value

# keys() return all keys

# values() return all values

# items()return values and keys


# mobiles.pop("name")

# print(mobiles)

#pop(key) remove key from dictionary


# mobiles["offer"]=500

# print(mobiles)>>{'name': 'motoedge14', 'brand': 'moto', 'price': 22000, 'is_available': True, 'offer': 500}




if "offer" in mobiles:

    selling_price=mobiles.get("price")-mobiles.get("offer")


    print(selling_price)

else:

    selling_price=mobiles.get("price")

    print(selling_price)    
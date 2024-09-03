
from json import load


f=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\jsonworks\\products.json","r",encoding="UTF-8")


items=load(f)

# print(len(items))

product_title=[i.get("title") for i in items ]

# print(product_title)

jewllery=[j.get("title")for j in items if j.get("category")=="jewelery"]

# print(jewllery)

price_filter=[p.get("title")for p in items if p.get("price")>100]

# print(price_filter)

price_range=[p.get("title")for p in items if p.get ("price")>=100 and  p.get("price")<=150]

# print(price_range)



#product with most number of rating

def get_rating_count(dic):


    return dic.get("rating").get("count")


top_rating_product=max(items,key=get_rating_count)

print(top_rating_product)





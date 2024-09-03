#region=asia
#population lowest
#population between
#dependent 
#capital
#calling codes african countries
#sub region =south america
#highest area
#demonym  == Virgin Islander
#european countries border



from json import load

f=open("C:\\Users\\fayiz\\OneDrive\\Desktop\\PythonJuneWorks\\jsonworks\\\country.json",encoding="UTF-8")

countries=load(f)


dependent=[c.get("name")for c in countries if c.get("independent")==False]

print(dependent)

# print(len(countries))


# asian countries

asian_countries=[c.get("name") for c in countries if c.get("region")=="Asia"]

# print(asian_countries)


# lowest population


def get_population(dic):


    return dic.get("population")

population_lowest=min(countries,key=get_population)

# print(population_lowest.get("name"))



# population between 2000000 to 4500000


population_range=[p.get("name")for p in countries if p.get ("population")>=2000000 and  p.get("population")<=4500000]





# dependent_countries

dependent_countries=[p.get("name")for p in countries if p.get("independent")==False]

# print(dependent_countries)


# capital of all countries

capital=[c.get ("capital") for c in countries]

# print(capital)

# african_countries_calling codes

american_countries_calling_codes=[c.get ("callingCodes")for c in countries if c.get("region")=="Americas"]

# print(american_countries_calling_codes)


# subregion is south america



subregion_south_america=[c.get ("name") for c in countries if c.get ("subregion")=="South America"]


# print(subregion_south_america)



# highest area


def get_area(dic):
     

    if "area" in dic:
          
        return dic.get("area")
    else:
        return 0
     



highest_area=max(countries,key=get_area)

print(highest_area.get("name"))



# demonym  == Virgin Islander


virgin_islander=[c.get("name") for c in countries if c.get("demonym")=="Virgin Islander"]


# print(virgin_islander)


# European_countries_border

European_countries_border=[c.get("borders") for c in countries if c.get("region")=="Europe"]

# print(European_countries_border)

all_region={c.get("region") for c in countries}

# print(all_region)



region_summery={}

for c in countries:

    region_name=c.get("region")

    if region_name in region_summery:

        region_summery[region_name]+=c.get("area",0)

    else:

        region_summery[region_name]=c.get("area",0)

value_key=[(v,k) for k,v in  region_summery.items()]

print(max(value_key))

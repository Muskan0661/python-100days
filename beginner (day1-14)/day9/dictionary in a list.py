travel_log=[
    {
        "country":"france",
        "visits":12,
        "cities":["paris","lille","dijon"]
    },
    {
      "country":"germany",
      "visits":5,
      "cities":["berlin","hamburg","stuttgart"]  
    },
]

def add_new(country_visited, times_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visited"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)

add_new("russia",2,["moscow","saint "])
print(travel_log)
travel_log = [
    {
        "country" : "France", 
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add(country, times_visited : int, places_been):
    travel_log.append({
        "country" : country,
        "visits" : times_visited,
        "cities" : places_been.split(",")
    })
    print(travel_log)

add("Russia", 2, "Moscow, Saint Petersburg")
travel_log = [
    {"country": "France",
     "visits": 12,
     "cities": ["Paris", "Lille", "Di jon"]
     },
    {"country": "Germany",
     "visits": 2,
     "cities": ["Hamburg", "Berlin", "Stuttgart"]
     }
]

country_name = input("enter the name of the country:")
number_of_visits = int(input("enter the no. of visits to the country"))
cities_visited_list = list(map(str, input("enter the cities separated by the coma").split(", ")))


def add_new_country(country_name, number_of_visits, cities_visited_list):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = number_of_visits
    new_country["cities"] = cities_visited_list
    travel_log.append(new_country)


add_new_country(country_name, number_of_visits, cities_visited_list)
print(travel_log)

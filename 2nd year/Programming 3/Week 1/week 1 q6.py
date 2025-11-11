#usr/bin/env python3

def filter_star(data, star_rating):

    results = {}

    for item, stars in data.items():
        if len(stars) == star_rating:
            results[item] = stars

    if not results:
        return "No result found!"
    else:
        return results


chocolates = {
    "Luxury Chocolates": "*****",
    "Tasty Chocolates": "****",
    "Big Chocolates": "*****",
    "Generic Chocolates": "***",
}
rating_to_find = 4

print(filter_star(chocolates, rating_to_find))

rating_to_find = 2
print(filter_star(chocolates, rating_to_find))
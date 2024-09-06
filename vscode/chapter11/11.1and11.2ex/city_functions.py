def get_city_countrys(city, country, population=None):
    if population:
        string = f"{city}, {country} - population {population}"
    else:
        string = f"{city}, {country}"
    return string.title()

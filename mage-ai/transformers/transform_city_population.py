from geonamescache import GeonamesCache
from datetime import datetime


@transformer
def city_population(df_2021):

    # Initialize the GeonamesCache
    gc = GeonamesCache()

    # Create a dictionary to map city names to their respective populations
    city_populations = {}
    for city_info in gc.get_cities().values():
        city_name = city_info['name']
        population = city_info['population']
        city_populations[city_name] = population

    # Add city_population column using --> city served column
    def get_city_population(city):
        return city_populations.get(city)

    # Add the 'city_population' column
    df_2021['city_population'] = df_2021['city_served'].apply(get_city_population)
    
    df_2021['ingested_at'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    return df_2021
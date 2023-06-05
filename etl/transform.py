from geonamescache import GeonamesCache
from datetime import date, datetime
from load import load_bq


def rename_data(df_2021):

    # drop column 'Rank2021' 
    df_2021.drop('Rank2021', axis=1, inplace=True)

    df_2021.rename(columns={
    'Airport': 'airport',
    'city served': 'city_served',
    'Country': 'country',
    'Passenger_2021': 'passenger_2021',
    'Passenger_2020': 'passenger_2020',
    'Change-2021–2020-Num': 'change_2021_2020',
    'Change 2020-2019-%': 'change_percentage_2021_2020'
}, inplace=True)
    
    city_population(df_2021)


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
    df_2021['city_population'] = df_2021['city served'].apply(get_city_population)
    
    df_2021['ingested_at'] = datetime.utcnow()

    load_bq()

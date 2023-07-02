if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def rename_data(df_2021):

    # drop column 'Rank2021' 
    df_2021.drop('Rank2021', axis=1, inplace=True)

    df_2021.rename(columns={
    'Airport': 'airport',
    'City served': 'city_served',
    'Country': 'country',
    'Passengers-2021': 'passengers_2021',
    'Passengers-2020': 'passengers_2020',
    'Change 2021-2020-Num': 'change_2021_2020',
    'Change 2021-2020-%': 'change_percentage_2021_2020'
}, inplace=True)
    
    print(df_2021.head())
    return df_2021


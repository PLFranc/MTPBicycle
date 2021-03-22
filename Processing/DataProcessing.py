import pandas as pd
dataset = pd.read_csv('../Datasets/Dataset_clean.csv')
year = []
#Normalisation des données
for i,day in dataset.iterrows():
    data = {'Date': day['Date'],   'Y_Total': day['Y_Total'],  'D_Total': day['D_Total'],
            'MAX_TEMPERATURE_C': day['MAX_TEMPERATURE_C']/100,  'MIN_TEMPERATURE_C': day['MIN_TEMPERATURE_C']/100,
            'WINDSPEED_MAX_KMH': day['WINDSPEED_MAX_KMH']/100,  'PRECIP_TOTAL_DAY_MM': day['PRECIP_TOTAL_DAY_MM']/100,
            'HUMIDITY_MAX_PERCENT': day['HUMIDITY_MAX_PERCENT']/100,'CLOUDCOVER_AVG_PERCENT': day['CLOUDCOVER_AVG_PERCENT']/100,
            'HEATINDEX_MAX_C': day['HEATINDEX_MAX_C']/100,  'WINDTEMP_MAX_C': day['WINDTEMP_MAX_C']/100,  'SUNHOUR': day['SUNHOUR']/100,
            'hollyday': day['hollyday']}
    year.append(data)
df = pd.DataFrame(year)
print(df.head(30).to_string())
df.to_csv('../Datasets/input.csv',index=False,header=True)
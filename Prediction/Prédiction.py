import pandas as pd
from LinearRegression import pred

test = {'MAX_TEMPERATURE_C':18,
        'MIN_TEMPERATURE_C':11,
        'WINDSPEED_MAX_KMH':45,
        'PRECIP_TOTAL_DAY_MM':0,
        'HUMIDITY_MAX_PERCENT':31,
        'CLOUDCOVER_AVG_PERCENT':12,
        'HEATINDEX_MAX_C':14,
        'WINDTEMP_MAX_C':13,
        'SUNHOUR':11.5,
        'Hollyday':0
}
input = pd.DataFrame(columns=['MAX_TEMPERATURE_C','MIN_TEMPERATURE_C','WINDSPEED_MAX_KMH','PRECIP_TOTAL_DAY_MM','HUMIDITY_MAX_PERCENT',
        'CLOUDCOVER_AVG_PERCENT','HEATINDEX_MAX_C','WINDTEMP_MAX_C','SUNHOUR','Hollyday'])
input = input.append(test,ignore_index=True)

data_forecast = pred(input)
#définition de la plage horaire
start = 0
end = 9
dataset = pd.read_csv('../Datasets/hour_dataset.csv')
data_ = dataset[dataset['Time']<end]
data_ = data_[data_['Time']>=start]

data_range = data_['D_Total'].sum()
cycle = dataset['D_Total'].sum()
print((data_range/cycle)*data_forecast)
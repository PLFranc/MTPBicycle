from datetime import datetime

import pandas as pd



final_dataset = pd.DataFrame(columns=['Date','Y_Total','D_Total'])

dataset = pd.read_csv('../Datasets/La myriade de Totems de Montpellier - SaisiesFormulaire (4).csv')
dataset_meteo_1 = pd.read_csv('../Datasets/export-montpellier2020.csv')
dataset_meteo_2 = pd.read_csv('../Datasets/export-montpellier2021.csv')
frames = [dataset_meteo_1,dataset_meteo_2]
dataset_meteo = pd.concat(frames,ignore_index=True  )

dataset.rename(columns={"Heure / Time": "Time", "Vélos depuis le 1er janvier / Grand total": "Y_Total",
                                  "Vélos ce jour / Today's total": "D_Total"},inplace=True)
dataset.drop(['Unnamed: 4', 'Remarque'],axis=1,inplace=True)
dataset.dropna(inplace=True)
print(dataset_meteo.to_string())
for j,day in dataset.iterrows():
    dataset['Date'].loc[j] = datetime.strptime(day['Date'],"%d/%m/%Y")
for j, day in dataset_meteo.iterrows():
    dataset_meteo['DATE'].loc[j] = datetime.strptime(day['DATE'], "%Y-%m-%d")

date_range = pd.date_range(start=dataset['Date'].iloc[0],
                               end=dataset['Date'].iloc[-1])
#cumuler les données d'une journée en une seule data


for date in date_range:
    df = dataset[dataset['Date'] == date]
    Y_total = 0
    D_total = 0
    for i, days in df.iterrows():
         D_total = D_total + days['D_Total']
         Y_total = Y_total + days['Y_Total']
    final_dataset = final_dataset.append({'Date':date,'Y_Total':Y_total,'D_Total':D_total},ignore_index=True)


final_dataset.drop([279],inplace=True)
print(final_dataset.to_string())
final_dataset.drop([358],inplace=True)
final_dataset.drop([364],inplace=True)
final_dataset.drop([365],inplace=True)
final_dataset.to_csv('../Datasets/Dataset_processed.csv',index=False,header=True)

final_dataset.set_index('Date',inplace=True)
dataset_meteo.set_index('DATE',inplace=True)

df = pd.concat([final_dataset,dataset_meteo],axis=1,join='inner')
df.reset_index(inplace=True)
df.rename(columns={'index': 'Date'},inplace=True)
print(df.tail(10).to_string())
data = pd.read_csv('../Datasets/Dataset_processed.csv')


date_range_2 = pd.date_range(start=datetime.strptime('2020-07-01', "%Y-%m-%d"),
                               end=datetime.strptime('2020-08-30', "%Y-%m-%d"))
hollidayList = []
for date in date_range_2:
        hollidayList.append({'Date': date, 'hollyday': 1})

hollyday_df = pd.DataFrame(hollidayList)

df.set_index('Date',inplace=True)
hollyday_df.set_index('Date',inplace=True)
dataframe = pd.concat([df, hollyday_df], axis=1)
dataframe.reset_index(inplace=True)
dataframe.rename(columns={'index': 'Date'},inplace=True)
dataframe.fillna(0.4,inplace=True)
dataframe.drop(columns=['TEMPERATURE_MORNING_C','TEMPERATURE_NOON_C','TEMPERATURE_EVENING_C','VISIBILITY_AVG_KM','PRESSURE_MAX_MB','DEWPOINT_MAX_C','WEATHER_CODE_MORNING','WEATHER_CODE_NOON','WEATHER_CODE_EVENING','TOTAL_SNOW_MM','UV_INDEX','OPINION'],inplace=True)
print(dataframe.to_string())
dataframe.to_csv('../Datasets/Dataset_clean.csv',index=False,header=True)

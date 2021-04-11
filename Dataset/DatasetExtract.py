from wwo_hist import retrieve_hist_data
import os
os.chdir("E:/collage/SEM-6/ML/Final Project/Dataset")

frequency = 24
start_date = '1-JAN-2009'
end_date = '11-4-2021'
api_key = '27846d15f07e44a983c102124211104' #your api key from worldweatheronline website
location_list = ['Ahmedabad']
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

from createdb import create_connection,close_connection
from create_pandasdf import convert_dict_to_df
from loaddb import update_db
from transform import keep_columns, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from extract_weather import get_current_weather, write_weather_data

import argparse
#import time

parser=argparse.ArgumentParser()
parser.add_argument("--city_id", default="5128581", help ="Fetch weather data for a specified city. Find the id of the city on OpenWeatherMap.org")
parser.add_argument("--frequency", default=900, type=int, help="How often does the program run in seconds")

args=parser.parse_args()
if args.city_id:
    print("city id inserted")
if args.city_id:
    print("program frequency inserted")


def main():

    connection=create_connection()
    filename=write_weather_data(get_current_weather(args.city_id))
    df_to_sql=set_datetime_col_as_row_index(convert_kelvin_to_celsius(
        change_col_name(keep_columns(convert_dict_to_df(filename)))))
        
    update_db(df_to_sql,connection)

    close_connection(connection)

if __name__=="__main__":
    main()

'''

city id inserted
program frequency inserted
Connection with database established ..........
Getting current weather data from OpenWeatherMap.org..........
Uploaded to database!

'''

import json
import argparse


def forecast(days):
    with open('/home/mheide/Documents/python/Weather/56119.json') as json_file:
        data = json.load(json_file)
        #Dig into JSON data to grab what I want. 
        quick = data['forecast']['simpleforecast']['forecastday']
        text  = data['forecast']['txt_forecast']['forecastday']
        for x in range(days):
            print('{}\nTemp: {} to {}\nConditions: {}\nWind: {} - {} MPH\n'.format(
                quick[x]['date']['weekday'],
                quick[x]['low']['fahrenheit'],
                quick[x]['high']['fahrenheit'],
                quick[x]['conditions'],
                quick[x]['avewind']['mph'],
                quick[x]['maxwind']['mph']))
        for x in range(days):
            print('\n{}\n{}\n'.format(text[x]['title'],text[x]['fcttext']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('days', help="Number of days to look at", nargs = '?', const= 1, type = int, default = input('Enter number of Days: '))
    args = parser.parse_args()

    forecast(args.days)

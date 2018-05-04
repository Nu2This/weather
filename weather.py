import json
import argparse
import requests
import webbrowser


def forecast(days):
    r = 'http://api.wunderground.com/api/08c90c66a7d001aa/forecast10day/q/MN/Worthington.json'
    data = requests.get(r).json()
    # Dig into JSON data to grab what I want. 
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

def radar():
    # radar api string
    r ='http://api.wunderground.com/api/08c90c66a7d001aa/animatedradar/q/56119.gif?newmaps=1&radius=200&width=500&height=500&noclutter=1&timelabel=1&timelabel.y=10'
    # Download gif to open
    with open('radar.gif', 'wb') as f:
        f.write(requests.get(r).content)
    webbrowser.get('firefox').open('/home/mheide/Documents/python/weather/radar.gif')
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('days', help="Number of days to look at", nargs = '?', const = 3, type = int,default=3)
    parser.add_argument('--radar', help="Display Radar", action = 'store_true')
    args = parser.parse_args()

    if args.radar:
        radar()
    else:
        forecast(args.days)

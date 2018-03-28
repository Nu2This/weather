import json

def extended_forecast():
    with open('/home/mheide/Documents/python/Weather/56119.json')as json_file:
        #Dig into the nested json to get workable data out of it. 
        data = json.load(json_file)
        forecast = data['forecast']
        simpleforecast = forecast['simpleforecast']
        forecastday = simpleforecast['forecastday']
        #Made these to make it easier to remember what is what
        today = forecastday[0]
        tomorrow = forecastday[1]
        nextday = forecastday[2]
        #put them in their own dict for easier iteration.
        three_day = [today,tomorrow,nextday]
        #Grab Text data from JSON
        for x in three_day:
            print(' '+'-'*5)
            print('| {0:4}   Temp    Con   Wind '.format(x['date']['weekday_short']))
            print('|' + ' '*5 + '{0:2} to {0:2}'.format(x['low']['fahrenheit'],
                                                       x['high']['fahrenheit']) +
                                  ' ' + '{0:2}'.format(x['conditions']) +
                          ' ' + '{0:2} - {0:2}'.format(x['avewind']['mph'],x['maxwind']['mph']))
                                                    # x['conditions'],
                                                   # x['avewind']['mph'],
                                                   # x['maxwind']['mph']))
def text_forecast():
    with open('/home/mheide/Documents/python/Weather/56119.json') as json_file:
        data = json.load(json_file)
        forecast = data['forecast']
        txt_forecast = forecast['txt_forecast']
        forecastday = txt_forecast['forecastday']
        today = forecastday[0]
        tomorrow = forecastday[1]
        nextday = forecastday[2]

        three_day_txt = [today,tomorrow,nextday]

        for day in three_day_txt:
            print('\n{}\n{}\n'.format(day['title'],day['fcttext']))

def ext_fore():
    with open('/home/mheide/Documents/python/Weather/56119.json') as json_file:
        data = json.load(json_file)
        #Dig into JSON data to grab what I want. 
        quick = data['forecast']['simpleforecast']['forecastday']
        text  = data['forecast']['txt_forecast']['forecastday']
        for x in range(0,3):
            print('{}\nTemp: {} to {}\nConditions: {}\nWind: {} - {} MPH\n'.format(
                quick[x]['date']['weekday'],
                quick[x]['low']['fahrenheit'],
                quick[x]['high']['fahrenheit'],
                quick[x]['conditions'],
                quick[x]['avewind']['mph'],
                quick[x]['maxwind']['mph']))
        for x in range(0,3):
            print('\n{}\n{}\n'.format(text[x]['title'],text[x]['fcttext']))

if __name__ == '__main__':
    ext_fore()

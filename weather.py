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

        for x in three_day:
            print(' '+'-'*5)
            print('| {0:4} Temp Cond Wind '.format(x['date']['weekday_short']))
            print('|' + ' '*5 + '{0:2} - {0:2}'*3''.format(x['low']['fahrenheit'],
                                                    x['high']['fahrenheit'],
                                                    x['conditions'],
                                                    x['avewind']['mph'],
                                                    x['maxwind']['mph']))

if __name__ == '__main__':
    extended_forecast()

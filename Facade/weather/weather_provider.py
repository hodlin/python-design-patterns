import urllib
import urllib2

APPID = '7e1cd1760c0c7c8014947bb2ba9dfbdd'  # An APPID for openweaathermap service


class WeatherProvider(object):
    def __init__(self):
        self.api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}'

    def get_weather_data(self, city, country):
        city = urllib.quote(city)
        url = self.api_url.format(city, country, APPID)
        return urllib2.urlopen(url).read()

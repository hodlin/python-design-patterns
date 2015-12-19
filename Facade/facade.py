from sys import argv
from weather.converter import Converter
from weather.weather import Weather
from weather.weather_provider import WeatherProvider
from weather.cache import Cache
from weather.parser import Parser


def rounded(fn):
    def wrapped(*argv):
        result = fn(argv[0], argv[1], argv[2])
        return round(result, 2)
    return wrapped

class Facade(object):



    @rounded
    def get_forecast(self, city, country):
        cache = Cache('cache_file')

        cache_result = cache.load()

        if cache_result:
            return cache_result
        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)

            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)

            weather = Weather(parsed_data)
            converter = Converter()
            temperature_celcius = converter. from_kelvin_to_celcius(weather.temperature)

            #cache.save(temperature_celcius)
            return temperature_celcius

if __name__ == '__main__':

    if len(argv) == 3:
        city = str(argv[1])
        country = str(argv[2])
    else:
        city = 'Kiev'
        country = 'UA'

    facade = Facade()
    print facade.get_forecast(city, country)

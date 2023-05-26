from pyowm import OWM
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'en'

city = input('Which city are you interested for?: ')


owm = OWM('5199357829d61a3c578235e6104ee736')
mgr = owm.weather_manager()



observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
detailed_status = w.detailed_status
print(w)

print("The temperature in " + city + "is: " + str(temperature) + " celsius.")
print("In that city " + str(detailed_status))
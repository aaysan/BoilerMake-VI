import pyowm
import pprint as pp


def get_weather_info():
    owm = pyowm.OWM('9e1a0fcd8ee8deffd5bf508f39f421f0')  # You MUST provide a valid API key



    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

    # Search for current weather in London (Great Britain)
    observation = owm.weather_at_place('West Lafayette')
    w = observation.get_weather()
    # print(w)                      # <Weather - reference time=2013-12-18 09:20,
                                  # status=Clouds>

    # Weather details
    # print(w.get_wind()      )            # {'speed': 4.6, 'deg': 330}
    # print(w.get_humidity()   )           # 87
    # print(w.get_temperature('celsius') ) # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.get_detailed_status())
    # pp.pprint(w.to_JSON())
    # print(dir(w))

    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
    observation_list = owm.weather_around_coords(-22.57, -43.12)

    weather_info = dict()
    weather_info["Temperature"] = w.get_temperature()['temp']
    weather_info["Description"] = w.get_detailed_status().title()

    return weather_info

print(get_weather_info())

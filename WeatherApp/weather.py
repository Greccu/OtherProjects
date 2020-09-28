import requests as req

API_KEY = "2e04fbf3a75cdf5be2079f573f2bb345"
API_ADRESS = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def kelvin_to_celsius(temp):
    return round(temp - 273.15)

def geticonurl(data):

    code = data['weather'][0]['icon']
    return "http://openweathermap.org/img/wn/"+code+"@2x.png"

def getinfo(city = "auto"):
    try:
        if city == "auto":
            try:
                cityurl = "https://ipinfo.io/json"
                citydata = req.get(cityurl).json()
                city = citydata['city']
            except:
                return "Location unavailable"
        url = API_ADRESS.format(city, API_KEY)
        data = req.get(url).json()
        return data
    except:
        return "City not found or connection failed"

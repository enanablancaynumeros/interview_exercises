# Weather forecast

[![Build Status](https://travis-ci.org/enanablancaynumeros/OpenWeatherForecast.svg?branch=master)](https://travis-ci.org/enanablancaynumeros/OpenWeatherForecast)
[![Coverage Status](https://coveralls.io/repos/enanablancaynumeros/OpenWeatherForecast/badge.svg)](https://coveralls.io/r/enanablancaynumeros/OpenWeatherForecast)
[![Latest Version](https://pypip.in/version/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Supported Python versions](https://pypip.in/py_versions/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Supported Python implementations](https://pypip.in/implementation/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Development Status](https://pypip.in/status/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)
[![Wheel Status](https://pypip.in/wheel/OpenWeatherForecast/badge.svg)](https://pypi.python.org/pypi/OpenWeatherForecast/)

Openweather python wrapper to forecast weather data.

OpenWeatherForecast is released under the [MIT license](https://github.com/enanablancaynumeros/weather_forecast/blob/master/LICENSE.txt). The source code is on [GitHub](https://github.com/enanablancaynumeros) and [issues are also tracked on GitHub](https://github.com/enanablancaynumeros/weather_forecast/issues).

### Install 
#### Pypi
```bash
pip install openweatherforecast
```

#### Manual
```bash
git clone git@github.com:enanablancaynumeros/OpenWeatherForecast.git
cd OpenWeatherForecast
python setup.py install
```

### Run test
```shell
python setup.py test

or 

nosetest openweatherforecast

```

#### Db configuration
Change the folder in constants or use the one defined in "/etc/openweather/settings.yaml"
```bash
sudo mkdir /etc/openweather/
sudo chmod 777 -R /etc/openweather/
cp contrib/settings.yaml /etc/openweather/
```

### Code example for weather data

```python
from open_weather_forecast.info_extractor.temperature.get_temperature import GetTemperature
from open_weather_forecast.conf.constants import WEATHER_INFORMATION_SCHEMA

city = "London,uk"
url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format(city)

temperature_manager = GetTemperature()
temperature_manager.download_store_new_data(url=url, information_schema=WEATHER_INFORMATION_SCHEMA)
weather_historic_data = temperature_manager.load_data()
del temperature_manager
print(weather_historic_data)
```

### Code example for forecast weather data

```python
from open_weather_forecast.info_extractor.forecast.get_forecast import GetForecast
from open_weather_forecast.conf.constants import FORECAST_WEATHER_INFORMATION_SCHEMA

city = "London,uk"
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format(city)

forecast_manager = GetForecast()
forecast_manager.download_store_new_data(url=forecast_url, information_schema=FORECAST_WEATHER_INFORMATION_SCHEMA)
forecast_historic_data = forecast_manager.load_data()
del forecast_manager    
print(forecast_historic_data)
```

### Code example to represent the data
```python
from open_weather_forecast.info_extractor.temperature.get_temperature import GetTemperature
from open_weather_forecast.conf.constants import WEATHER_INFORMATION_SCHEMA

city = "London,uk"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}'.format(city)

temperature_manager = GetTemperature()
temperature_manager.download_store_new_data(url=url, information_schema=WEATHER_INFORMATION_SCHEMA)
weather_historic_data = temperature_manager.load_data()


from open_weather_forecast.info_extractor.forecast.get_forecast import GetForecast
from open_weather_forecast.conf.constants import FORECAST_WEATHER_INFORMATION_SCHEMA

forecast_url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}'.format(city)

forecast_manager = GetForecast()
forecast_manager.download_store_new_data(url=forecast_url, information_schema=FORECAST_WEATHER_INFORMATION_SCHEMA)
forecast_historic_data = forecast_manager.load_data()

import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
measures = ["temp_min", "temp_max", "temp"]

plt.subplot(221)
plt.title("Weather measures")
plt.xlabel('Time')
plt.ylabel('Temperature in K')
for measure in measures:
    plt.plot([weather_historic_data[x].get(measure) for x in weather_historic_data], label=measure)

plt.xticks(range(len(list(weather_historic_data.keys()))),
    [x[5:] for x in list(weather_historic_data.keys())],
    rotation="vertical",
    fontsize=6)
plt.legend(loc="upper right", prop={'size': 6})


plt.subplot(222)
plt.title("Forecast Weather")
plt.xlabel('Time')
plt.ylabel('Temperature in K')
for measure in measures:
    plt.plot([forecast_historic_data[x].get(measure) for x in forecast_historic_data], label=measure)

plt.xticks(range(len(list(forecast_historic_data.keys()))),
    [x[5:] for x in list(forecast_historic_data.keys())],
    rotation="vertical",
    fontsize=6)
plt.legend(loc="upper right", prop={'size': 6})


plt.subplot(223)
plt.title("Error between forecasting and final measures")
plt.xlabel('Time')
plt.ylabel('Error')

common_days = [x for x in weather_historic_data if x in forecast_historic_data.keys()]
errors = defaultdict(list)

for measure in measures:
    for day in common_days:
        value = np.power((weather_historic_data.get(day).get(measure) - forecast_historic_data.get(day).get(measure)), 2)
        errors[measure].append(value)
    plt.plot(errors[measure], label=measure)
plt.xticks(range(len(common_days)), [x[5:] for x in common_days], rotation="vertical", fontsize=6)
plt.legend(loc="upper right", prop={'size': 6})


from datetime import datetime
from open_weather_forecast.conf.constants import WEATHER_DATE_FORMAT

times_measured = [datetime.strptime(x, WEATHER_DATE_FORMAT) for x in weather_historic_data]
comparable_forecast = [x for x in forecast_historic_data if datetime.strptime(
    x, WEATHER_DATE_FORMAT) > times_measured[0] and datetime.strptime(x, WEATHER_DATE_FORMAT) < times_measured[-1]]
plt.subplot(224)
plt.title("Estimation comparison")
plt.xlabel('Time')
plt.ylabel('Temperature in K')

plt.plot([weather_historic_data.get(day.strftime(WEATHER_DATE_FORMAT)) for day in comparable_forecast],
         label="Measured", marker="*")
plt.plot([forecast_historic_data.get(day.strftime(WEATHER_DATE_FORMAT)) for day in comparable_forecast],
         label="Forecast", marker="o")
plt.xticks(range(len(comparable_forecast)), [x[5:] for x in comparable_forecast], rotation="vertical", fontsize=6)
plt.legend(loc="upper right", prop={'size': 6})

plt.tight_layout()
plt.show()
```


See [Pypi](https://pypi.python.org/pypi/openweatherforecast/0.1.0) project page.



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/enanablancaynumeros/openweatherforecast/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


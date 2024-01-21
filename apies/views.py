from django.shortcuts import render
import requests

def get_weather(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        api_key = '4f06873149e336c2f2f9d960ca8c953f'  # Замените на свой API-ключ от OpenWeatherMap
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city_name, 'appid': api_key, 'units': 'metric'}


        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                weather_info = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                }
                return render(request, 'apies/result.html', {'weather_info': weather_info})

            else:
                error_message = f"Error: {data['message']}"
                return render(request, 'apies/error.html', {'error_message': error_message})

        except Exception as e:
            return render(request, 'apies/error.html', {'error_message': str(e)})
    else:
        response = requests.get('https://catfact.ninja/fact')
        data = response.json()
        cat_fact = data['fact']
        

    return render(request, 'apies/index.html', {'cat_fact': cat_fact})


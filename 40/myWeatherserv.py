import socket
import threading
import requests


class WeatherWebAPI:
    def __init__(self):
        self.unit = 'metric'
        self.lang = 'RU'
        self._api_key = '0e778d43f3287d5fa9fa831e4a77c084'
        self.url = r'https://api.openweathermap.org/data/2.5/weather'
        self.exclude = 'current,minutely,hourly,alerts'
        self.limit = 1

    def get_weather_data(self, city, country):
        geocode = self.get_cities_geocode(city, country)
        if geocode:
            options = f'?lat={geocode["lat"]}&lon={geocode["lon"]}&exclude={self.exclude}&units={self.unit}&lang={self.lang}'
            api_head = f'&appid={self._api_key}'
            rec_weather = f'https://api.openweathermap.org/data/2.5/weather{options}{api_head}'
            r = requests.get(rec_weather)
            weather_resp_json = r.json()
            weather = weather_resp_json
            result = ''
            clearance = weather['weather'][0]['description']
            avg_temperature = round((weather['main']['temp_min'] + weather['main']['temp_max']) / 2, 1)
            wind_speed = weather['wind']['speed']
            humidity = weather['main']['humidity']
            result += f'==========================================\n' \
                      f'Today forecast is:\n' \
                      f'Weather: {clearance.capitalize()}\n' \
                      f'Average temperature: {avg_temperature}°C\n' \
                      f'Speed of wind: {wind_speed} m/s\n' \
                      f'Humidity: {humidity} %\n' \
                      f'==========================================\n'

            answer = result
        else:
            answer = "Такого города нет."
        return answer

    def get_cities_geocode(self, city: str, country: str):
        options = f'?q={city},{country}&limit={self.limit}'
        auth = f'&appid={self._api_key}'
        req_str = f'http://api.openweathermap.org/geo/1.0/direct{options}{auth}'
        resp = requests.get(req_str)
        if resp.json():
            geocode_json = resp.json()[0]
            lat = geocode_json['lat']
            lon = geocode_json['lon']
            return {'lat': lat, "lon": lon}
        else:
            return False


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 4321
server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')
server_socket.listen(5)
welcome_message = 'Добро пожаловать! Вы подключены к серверу о погоде.\n' \
                  'Введите сообщение в виде "Страна, Город": '


def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    client_socket.send(welcome_message.encode())
    my_weather_api = WeatherWebAPI()

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Клиент отключился: ', client_address)
            break

        words = client_message.split(',')
        words = list(map(str.strip, words))
        country, city = words[0].lower(), words[1][0].upper() + words[1][1:].lower()
        answer = my_weather_api.get_weather_data(city, country)
        if not answer:
            answer = '-*-Такой город не найден-*-'
        client_socket.send(answer.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

import socket
import time
import json


def run_on_port(port, time_delta):
    # Создаем сокет и привязываем его к порту 123
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', port))

    print(f'Server started on localhost:{port}')

    while True:
        # Получаем данные от клиента
        data, address = server_socket.recvfrom(1024)
        print(f'Received data {data} from {address}')

        # Получаем текущее время
        current_time = int(time.time())

        # Вычисляем "вранье"
        modified_time = current_time + time_delta

        # Отправляем измененное время клиенту
        server_socket.sendto(str(modified_time).encode(), address)


def get_config():
    with open('config.json', 'r') as f:
        loaded_config = json.load(f)
    return loaded_config


if __name__ == "__main__":
    config = get_config()
    run_on_port(config['port'], config['time_delta'])

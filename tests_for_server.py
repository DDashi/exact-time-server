import unittest
import json
import threading
import socket
import time
from time_server import run_on_port


class TestTimeServer(unittest.TestCase):
    def setUp(self):
        # Запускаем тестовый сервер в отдельном потоке
        config = self.get_config()

        self.port = config['port']
        self.delta_from_config = config['time_delta']

        self.server_thread = threading.Thread(target=run_on_port)
        self.server_thread.start()

    def get_config(self):
        with open('config.json', 'r') as f:
            loaded_config = json.load(f)
        return loaded_config

    def test_time_calculation(self):
        # Проверяем, что время корректно изменяется

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'data for test', ('localhost', self.port))

        data, address = sock.recvfrom(1024)
        current_time = int(time.time())

        delta_time = int(data) - current_time
        self.assertEqual(delta_time, self.delta_from_config)


if __name__ == '__main__':
    unittest.main()

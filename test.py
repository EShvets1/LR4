import unittest
from main import app
class TestStringMethods(unittest.TestCase):
    def test_page(self):  # тестируем функцию, которая отвечает за главную страницу
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.get('/')  # отправляем GET-запрос на главную страницу
        self.assertEqual(response.status_code, 200)  # проверяем, что код ответа равен 200

    def test_ipoteca_type_1_1(self):#Первый тест работоспособности первого режима
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 120000, 'num_2': 2, 'num_3': 15, 'options': 1})#Ввод параметров
        self.assertIn('61127', response.data.decode())

    def test_ipoteca_type_1_2(self):  # Второй тест работоспособности первого режима
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 1000000, 'num_2': 12, 'num_3': 5, 'options': 1})  # Ввод параметров
        self.assertIn('85607.48', response.data.decode())

    def test_ipoteca_type_2_1(self):  # Первый тест работоспособности второго режима
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 1000000, 'num_2': 15, 'num_3': 20, 'options': 2})  # Ввод параметров
        self.assertIn('70063.93', response.data.decode())

    def test_ipoteca_type_2_2(self):  # Второй тест работоспособности второго режима
        tester = app.test_client(self)  # создаем клиент для тестирования
        response = tester.post("/", content_type='multipart/form-data', data={'num_1': 15000, 'num_2': 11, 'num_3': 53, 'options': 2})  # Ввод параметров
        self.assertIn('2038.85', response.data.decode())

if __name__ == '__test__':
    unittest.test()
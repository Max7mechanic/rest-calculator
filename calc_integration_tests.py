import math
import unittest

from requests import get

import calc
from json import loads


class IntegrationCase(unittest.TestCase):
    def setUp(self) -> None:
        self.host = calc.HOST
        self.port = calc.PORT
        self.base_path = f'http://localhost:{self.port}'
        self.header_content_type = 'application/json'
        self.a = 12
        self.b = 11

    def prepare_params(self):
        return {'a': self.a, 'b': self.b}

    def process_response(self, response):
        self.assertEqual(response.headers.get("Content-Type"), self.header_content_type)
        self.assertEqual(response.status_code, 200)
        return loads(response.text)['result']

    def test_add(self):
        response = get(url=f'{self.base_path}/add', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a + self.b)

    def test_substract(self):
        response = get(url=f'{self.base_path}/substract', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a - self.b)

    def test_multiply(self):
        response = get(url=f'{self.base_path}/multiply', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a * self.b)

    def test_divide(self):
        response = get(url=f'{self.base_path}/divide', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a / self.b)

    def test_negative_zero_divison(self):
        response = get(url=f'{self.base_path}/divide', params={'a': 10, 'b': 0})
        self.assertEqual(self.process_response(response), -1)

    def test_mod(self):
        response = get(url=f'{self.base_path}/mod', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a % self.b)

    def test_log(self):
        response = get(url=f'{self.base_path}/log', params=self.prepare_params())
        self.assertEqual(self.process_response(response), math.log(self.a, self.b))

    def test_average(self):
        response = get(url=f'{self.base_path}/average', params=self.prepare_params())
        self.assertEqual(self.process_response(response), (self.a + self.b) / 2)

    def test_exp(self):
        response = get(url=f'{self.base_path}/exp', params=self.prepare_params())
        self.assertEqual(self.process_response(response), self.a ** self.b)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        url = '/api/products/'
        data = {'name': 'Produit Test', 'price': 20.5, 'stock': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_products(self):
        Product.objects.create(name='Produit Test', price=20.5, stock=10)
        url = '/api/products/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

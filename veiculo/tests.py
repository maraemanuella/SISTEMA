from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from veiculo.forms import FormularioVeiculo
from veiculo.models import Veiculo


class TesteModelVeiculo(TestCase):
    def setUp(self):
        self.instancia = Veiculo.objects.create(
            marca='HONDA',
            modelo='ABCDE',
            ano=datetime.now().year,
            cor='Preto',
            combustivel='Flex',
        )

    def test_is_new(self):
        self.assertTrue(self.instancia.veiculo_novo)
        self.instancia.ano = datetime.now().year - 5
        self.assertFalse(self.instancia.veiculo_novo)

    def test_anos_de_uso(self):
        self.assertEqual(self.instancia.anos_de_uso(), 0)
        self.instancia.ano = datetime.now().year - 5
        self.assertEqual(self.instancia.anos_de_uso(), 5)


class TestesViewListarVeiculos(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345teste')
        self.client.force_login(self.user)
        self.url = reverse('listar-veiculos')
        Veiculo.objects.create(
            marca='HONDA',
            modelo='ABCDE',
            ano=2023,
            cor='Preto',
            combustivel='Flex',
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('lista_veiculos')), 1)


class TestesViewCriarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar-veiculo')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        dados = {
            'marca': 'HONDA',
            'modelo': 'ABCDE',
            'ano': '2023',
            'cor': 'Preto',
            'combustivel': 'Flex',
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')


class TestesViewEditarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(
            marca='HONDA',
            modelo='ABCDE',
            ano=2023,
            cor='Preto',
            combustivel='Flex',
        )
        self.url = reverse('editar-veiculo', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
        self.assertEqual(response.context.get('object').marca, 'HONDA')

    def test_post(self):
        data = {
            'marca': 'FIAT',
            'modelo': 'FGHIJ',
            'ano': '2024',
            'cor': 'Branco',
            'combustivel': 'Gasolina',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        veiculo_atualizado = Veiculo.objects.first()
        self.assertEqual(veiculo_atualizado.marca, 'FIAT')
        self.assertEqual(veiculo_atualizado.pk, self.instancia.pk)


class TestesViewDeletarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='12345')
        self.client.force_login(self.user)
        self.instancia = Veiculo.objects.create(
            marca='HONDA',
            modelo='Civic',
            ano=2023,
            cor='Preto',
            combustivel='Flex',
        )
        self.url = reverse('deletar-veiculo', kwargs={'pk': self.instancia.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instancia.pk)
        self.assertEqual(response.context.get('object').modelo, 'Civic')

    def test_post(self):
        self.assertEqual(Veiculo.objects.count(), 1)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)
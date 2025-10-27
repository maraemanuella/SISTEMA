#!/usr/bin/env python3
"""
Script para testar a API com token de autenticação
"""
import requests

# Configuração
BASE_URL = "http://127.0.0.1:8000"
TOKEN = "c7b2561fe6374304a6bd975a4edbfea5443a40de"

# Headers com token
headers = {
    "Authorization": f"Token {TOKEN}"
}

# Testar endpoint de listagem
print("🔍 Testando GET /api/listar/")
print("-" * 50)

response = requests.get(f"{BASE_URL}/api/listar/", headers=headers)

print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print("\nResposta:")
print(response.json())

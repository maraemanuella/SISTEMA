#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login   

class Login(View):
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):
        usuario = request.POST.get('usuario', '')
        senha = request.POST.get('senha', '')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Login realizado com sucesso!")
            else:
                return render(request, 'autenticacao.html', {'erro': 'Usuário inativo.'})
        else:
            return render(request, 'autenticacao.html', {'erro': 'Usuário ou senha incorretos.'})

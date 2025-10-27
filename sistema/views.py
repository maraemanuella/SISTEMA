from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy


class LoginView(DjangoLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, 'Usuário ou senha inválidos.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, f'Bem-vindo(a), {self.request.user.first_name or self.request.user.username}!')
        return reverse_lazy('listar-veiculos')


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Você saiu do sistema com segurança.')
        return super().dispatch(request, *args, **kwargs)


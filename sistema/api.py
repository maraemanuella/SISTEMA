from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sistema.serializers import SerializadorVeiculo
from veiculo.models import Veiculo


class VehicleListView(ListAPIView):
    """Endpoint somente leitura que lista veículos disponíveis."""
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()


class ObtainAuthTokenView(ObtainAuthToken):
    """Endpoint para autenticação baseada em token."""
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key,
            'created': created,
        })

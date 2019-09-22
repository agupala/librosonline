from django.urls import path
from consulta.views import ConsultaResp

urlpatterns = [
    path('', ConsultaResp.as_view(), name='consultaresp'),
]
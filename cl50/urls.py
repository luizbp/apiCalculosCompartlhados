from django.urls import path
from cl50.views import calculo_cl50
# from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('<str:comando>/', calculo_cl50),
    # path(r'^login/', obtain_jwt_token),
]
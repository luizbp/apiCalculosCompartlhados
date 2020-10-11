from django.urls import path
# from cl50.views import calculo_cl50, teste, calculo_cl50_json
from cl50.views import calculo_cl50_json
# from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', calculo_cl50_json),
    # path(r'^login/', obtain_jwt_token),
]
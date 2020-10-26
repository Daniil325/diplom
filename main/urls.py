from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', product_list, name='list'),
    path('<int:id>/<slug:slug>/', product_detail.as_view(), name='main_detail'),
    path('login/', MyprojectLoginView.as_view(), name='login_page'),
    path('register/', RegisterUserView.as_view(), name='register_page'),
    path('logout/', MyProjectLogout.as_view(), name='logout_page'),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserRegisterView, UserListCreateView, UserDetailView, UserUpdateView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('list/', UserListCreateView.as_view(), name='get_users'),
    path('user/<str:id>/', UserDetailView.as_view(), name='get_user'),
    path('user/update/', UserUpdateView.as_view(), name='update_user')
]
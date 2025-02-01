from django.urls import path
from .views import (
    RegisterView,
    UserListCreateView,
    UserDetailView,
    VerifyTokenView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify/", VerifyTokenView.as_view(), name="verify"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("list/", UserListCreateView.as_view(), name="get_users"),
    path("user/<str:id>/", UserDetailView.as_view(), name="get_user"),
]

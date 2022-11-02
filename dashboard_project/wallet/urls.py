from django.urls import path
from .views import UsersView, CreateUserView, DeleteUserView, CreditUserView, DebitUserView

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/user/', CreateUserView.as_view(), name='create_user'),
    path('delete/user/', DeleteUserView.as_view(), name='delete_user'),
    path('credit/user/', CreditUserView.as_view(), name='credit_user'),
    path('debit/user/', DebitUserView.as_view(), name='debit_user')
]
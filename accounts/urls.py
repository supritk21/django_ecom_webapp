
from django.urls import path
from accounts.views import login_page , register_page, activate_email, account_details, add_address, delete_address
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login/', login_page, name="login"),
   path('register/', register_page, name="register" ),
   path('details/', account_details, name="account_details"),
   path('address/', add_address, name="user_address"),
   path('delete/<uuid:address_id>/',delete_address , name="delete_address"),
   path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
   path('activate/<email_token>', activate_email, name="activate_email")
]

from django.urls import path
from user.views import GetUserView, AddUserView, \
    UserLoginView, UserLogoutView, \
    UserGetView, SetSuperView, SetStaffView


urlpatterns = [
    path('all/', GetUserView.as_view(), name="all_users"),
    path('signup/', AddUserView.as_view(), name="add_new_user"),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('<int:id>/', UserGetView.as_view(), name='get_delete_user'),
    path('<int:id>/setsuper/', SetSuperView.as_view(), name='set_super'),
    path('<int:id>/setstaff/', SetStaffView.as_view(), name='set_staff'),
]
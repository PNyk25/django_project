from django.urls import path, include
from details_app.api.views import User_Detail,User_list

urlpatterns = [
    path('list/', User_list.as_view(), name='user-list'),
    path('list/<int:pk>/', User_Detail.as_view(), name='user-detail'),

]
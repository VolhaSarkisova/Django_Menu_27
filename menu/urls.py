
from django.urls import path
from menu.views import child, page1, page2

app_name = "menu"

urlpatterns = [
    path('child/', child, name="child"),
    path('page1/', page1, name="page1"),
    path('page2/', page2, name="page2"),
]
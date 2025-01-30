from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('',home_view,name='index'),
    path('<int:pid>',single_view,name='single'),
    # path('test',test,name='test'),
]

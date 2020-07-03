from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('people_signin',views.p_signin,name='people_signin'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('user_signin',views.u_signin,name='user_signin'),
    path('logout',views.logout,name='logout'),
    #path('home',views.index,name='home'),
]
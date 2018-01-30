from django.conf.urls import url
from django.urls import path
from rango import views


app_name = 'rango'

urlpatterns = [
    path('', views.rango_index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('category/<category_name_slug>/', views.show_category, name='show_category'),
    path('register/', views.register, name='register'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<username>', views.user_profile_view, name='profile'),
    path('goto/', views.track_url, name='goto'),

]


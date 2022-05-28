
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('homepage_after_login',views.login,name='homepage_after_login'),
    path('sell_page',views.sell,name='sell'),
    path('buy',views.buy,name='buy'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('team1',views.team1,name='team1'),
    path('team2',views.team2,name='team2'),
    path('team3',views.team3,name='team3'),
    path('team4',views.team4,name='team4'),
    path('propertysingle',views.propertysingle,name='propertysingle'),
    path('propertysingle1',views.buy_propperty,name='propertysingle1'),
    path("predict", views.predict, name="predict"),
    path("result", views.result),

    #path('propertysingle1',views.propertysingle1,name='propertysingle1')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


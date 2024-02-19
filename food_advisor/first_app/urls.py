from django.urls import path

from . import views

urlpatterns=[
    path('create_person/', views.create_person, name='create_person'),
    path('person_list/', views.person_list, name='person_list'),
    path('create_advisor/', views.create_advisor, name='create_advisor'),
    path('advisor_list/', views.advisor_list, name='advisor_list'),
    path('create_item/', views.create_item, name='create_item'),
    path('item_list/', views.item_list, name='item_list'),
    path('create_report/', views.create_report, name='create_report'),
    path('report_list/', views.report_list, name='report_list'),
    path('home/',views.home,name='home'),
    path('login/',views.Login,name='Login'),
    path('logout/',views.Logout,name='Logout'),
]
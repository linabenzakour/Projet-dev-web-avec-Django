from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='base'),
    path('avion/<str:id_avion>/', views.detail_avion, name='detail_avion'),
    path('aeroport/<str:id_aeroport>/', views.detail_aeroport, name='detail_aeroport'),
    path('create_avion/', views.create_avion, name='create_avion'),
    path('create_aeroport/', views.create_aeroport, name='create_aeroport'),
    path('delete_aeroport/<str:id_aeroport>/', views.delete_aeroport, name='delete_aeroport'),

    path('delete_avion/<str:id_avion>/', views.delete_avion, name='delete_avion'),
    path('modify_avion/<str:id_avion>/', views.modify_avion, name='modify_avion'),
    path('modify_aeroport/<str:id_aeroport>/', views.modify_aeroport, name='modify_aeroport'),
    path('aeroport_plein/', views.aeroport_plein, name='aeroport_plein'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('data_list/', views.data_list, name='data_list'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
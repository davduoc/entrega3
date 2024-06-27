from django.urls import path
from .views import pagina_1Ecchi, pagina_1Josei, pagina_1Seinen, pagina_1Shojo_ai, pagina_1Shojo, pagina_1Shonen_ai, pagina_1Shonen, pagina_1Yaoi, pagina_1Yuri, pagina_buscar, pagina_buscart, pagina_carrito, pagina_catalogo, pagina_confirmarcompra, pagina_contacto, pagina_contacto2, pagina_en_construccion, pagina_index, pagina_inicio_sesion, pagina_plantilla, pagina_prueba_2, pagina_registro


from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('1Ecchi/', pagina_1Ecchi, name='1Ecchi'),
    path('1Josei/', pagina_1Josei, name='1Josei'),
    path('1Seinen/', pagina_1Seinen, name='1Seinen'),
    path('1Shojo_ai/', pagina_1Shojo_ai, name='1Shojo_ai'),
    path('1Shojo/', pagina_1Shojo, name='1Shojo'),
    path('1Shonen_ai/', pagina_1Shonen_ai, name='1Shonen_ai'),
    path('1Shonen/', pagina_1Shonen, name='1Shonen'),
    path('1Yaoi/', pagina_1Yaoi, name='1Yaoi'),
    path('1Yuri/', pagina_1Yuri, name='1Yuri'),
    path('buscar/', pagina_buscar, name='buscar'),
    path('buscart/', pagina_buscart, name='buscart'),
    path('carrito/', pagina_carrito, name='carrito'),
    path('catalogo/', pagina_catalogo, name='catalogo'),
    path('confirmarcompra/', pagina_confirmarcompra, name='confirmarcompra'),
    path('contacto/', pagina_contacto, name='contacto'),
    path('contacto2/', pagina_contacto2, name='contacto2'),
    path('en_construccion/', pagina_en_construccion, name='en_construccion'),
    path('index/', pagina_index, name='index'),
    path('inicio_sesion/', pagina_inicio_sesion, name='inicio_sesion'),
    path('plantilla/', pagina_plantilla, name='plantilla'),
    path('prueba_2/', pagina_prueba_2, name='prueba_2'),
    path('registro/', pagina_registro, name='registro'),

    path('manga_list', views.manga_list, name='manga_list'),
    path('manga/create/', views.manga_create, name='manga_create'),
    path('manga/<int:pk>/update/', views.manga_update, name='manga_update'),
    path('manga/<int:pk>/delete/', views.manga_delete, name='manga_delete'),
]

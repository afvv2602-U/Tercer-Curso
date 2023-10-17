from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    #path('post/<int:id>/', views.detalle_post, name='detalle_post'),
    path('about_us/', views.about_us, name = "about_us"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('register/', views.register, name='register'),
    path("logout/", views.logout_view, name="logout"),
    path('search/', views.post_search, name='post_search'),
    #path('publicaciones/', views.listar_publicaciones, name='listar_publicaciones'),
    path('publicacion/<int:publicacion_id>/', views.ver_publicacion, name='ver_publicacion'),
    # Define una URL para el popup de comentarios
    path('agregar_comentario/<int:publicacion_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('register/politics/', views.politics, name='politics'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

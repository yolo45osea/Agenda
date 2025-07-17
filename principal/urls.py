from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('crear_pago', view.crear_pago, name='crear_pago'),
    path('', views.index, name='index'),
    path('administrador', views.administrador, name='administrador'),
    path('alerta_accesos/', views.alerta_accesos, name='alerta_accesos'),
    path('jefe_maestranza/', views.jefe_maestranza, name='jefe_maestranza'),
    path('mantenimiento_activo/', views.mantenimiento_activo, name='mantenimiento_activo'),
    path('operador/', views.operador, name='operador'),
    path('registro_movimientos/', views.registro_movimientos, name='registro_movimientos'),
    path('calendario/', views.calendario, name='calendario'),
    path('registro_evento/', views.registro_evento, name='registro_evento'),
    path('organizador/', views.organizador, name='organizador'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path("ping/", lambda r: HttpResponse("pong")),
    path('sendmail', views.sendmail, name='sendmail'),


    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('mecanicos', views.mecanicos, name='mecanicos'),
    path('servicio', views.servicio, name='servicio'),
    #path('subir_excel/', views.subir_excel, name='subir_excel'),


    #path('password_reset/', views.password_reset, name='password_reset'),
    #path('recuperar/enviado/', views.custom_password_reset_done, name='custom_password_reset_done'),
    #path('recuperar/<uidb64>/<token>/', views.custom_password_reset_confirm, name='custom_password_reset_confirm'),
    #path('recuperar/completado/', views.custom_password_reset_complete, name='custom_password_reset_complete'),
]

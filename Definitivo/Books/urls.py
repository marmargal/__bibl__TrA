from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^populate', 'principal.views.populateDB'),
    url(r'^loadRS', 'principal.views.loadRS'),
    url(r'^search/$', 'principal.views.search'),
    #url(r'^recommendedFilms', 'principal.views.recommendedFilms'),
    #url(r'^similarFilms', 'principal.views.similarFilms'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
     #nuevoUsuario
    url(r'^header$','principal.views.header'),
    
    #nuevoUsuario
    url(r'^nuevousuario$','principal.views.nuevo_usuario'),
    
    #ingresar usuario
    url(r'^ingresar/$','principal.views.ingresar'),
    
    #ingresar mejorado privado
    url(r'^privado/$','principal.views.privado'),
    
    #Cierre de sesion
    url(r'^cerrar/$', 'principal.views.cerrar'),
)
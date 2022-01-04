from django.urls import path

from . import views

urlpatterns = [
    #mesmo esquema do urls.py superior, só que aqui no segundo parametros chamo o metodo index dentro do view.py
    path('', views.index, name='index'),
]
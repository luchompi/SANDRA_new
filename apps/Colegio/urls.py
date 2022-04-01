from django.urls import path 
from . import views as v
app_name="colegio"


urlpatterns =[
path('sedes/',v.SedeListView.as_view(),name="sedeIndex"),
path('sedes/nuevo',v.SedeCreateView.as_view(),name="sedeCreate"),
path('sedes/detalles/<pk>',v.SedeDetailView.as_view(),name="sedeDetail"),
path('sedes/actualizar/<pk>',v.SedeUpdateView.as_view(),name="sedeUpdate"),
path('sedes/eliminar/<pk>',v.SedeDeleteView.as_view(),name="sedeDelete"),

path('cursos/',v.CursoListView.as_view(),name="cursoIndex"),
path('cursos/generar/',v.GenerarCursos.as_view(),name="cursoGenerar"),
path('cursos/borrar/<pk>',v.borrarCurso.as_view(),name="cursoDelete"),
]
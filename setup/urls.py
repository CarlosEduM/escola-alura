from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudante, ListaMatriculasCurso

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudante')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matricula')

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação API",
      default_version='v1',
      description="Documentação API Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

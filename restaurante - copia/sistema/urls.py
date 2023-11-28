from django.contrib import admin
from django.urls import path
from .views import HomeView, TemplateView, AboutView, AdminListView, CocinaFunView, MeseroFunView, AdminFunElimPlato, AdminFunEditPlato, AdminFunCreatePlato, AdminCrUserFunView

app_name = 'sistema'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('funciones/', AboutView.as_view(), name='funciones'),
    path('funciones/funciones admin/', AdminListView.as_view(), name='fun admin'),
    path('funciones/funciones admin/crear plato', AdminFunCreatePlato.as_view(), name='fun_admin_crplato'),
    path('funciones/funciones admin/editar plato/<int:pk>/', AdminFunEditPlato.as_view(), name='fun_admin_editplato'),
    path('funciones/funciones admin/eliminar plato/<int:pk>/', AdminFunElimPlato.as_view(), name='fun_admin_elimplato'),
#    path('funciones/funciones admin/crear usuario', AdminCrUserFunView.as_view(), name='fun admin cruser'),
    path('funciones/funciones cocina', CocinaFunView.as_view(), name='fun cocina'),
    path('funciones/funciones mesero', MeseroFunView.as_view(), name='fun mesero'),
]
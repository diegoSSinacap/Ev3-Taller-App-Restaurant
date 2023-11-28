from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView 
from sistema.models import Plato, Pedidos
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    
class LoginView(TemplateView):
    def get(self, request):
        return render(request, "login.html")


class AboutView(TemplateView):
    template_name = "funciones.html"


class AdminListView(LoginRequiredMixin, ListView):
    login_required = True
    model = Plato
    template_name = "fun_admin.html"
    context_object_name = "platos"
    

class AdminCrUserFunView(TemplateView):
    template_name = "fun_admin_cruser.html"
    
class AdminFunCreatePlato(LoginRequiredMixin, CreateView):
    login_required = True
    model = Plato # Aqui especificamos la tabla
    template_name = "fun_admin_crplato.html"
    fields = ['nom_plato', 'desc_plato', 'prec_plato']
    success_url = "/funciones/funciones admin"

    def form_valid(self, form):
        # Realizar alguna lógica adicional si es necesario
        return super().form_valid(form)

class AdminFunEditPlato(LoginRequiredMixin, UpdateView):
    login_required = True
    model = Plato # Aqui especificamos la tabla
    fields = ['nom_plato', 'desc_plato', 'prec_plato']
    success_url = "/funciones/funciones admin"
    template_name = "fun_admin_editplato.html"

class AdminFunElimPlato(LoginRequiredMixin, DeleteView):
    login_required = True
    model = Plato # Aqui especificamos la tabla
    template_name = "eliminar-clase.html"
    success_url = "/funciones/funciones admin"

class CocinaFunView(TemplateView):
    template_name = "fun_cocina.html"

class MeseroFunView(LoginRequiredMixin, CreateView):
    template_name = "fun_mesero.html"
    login_required = True
    model = Pedidos # Aqui especificamos la tabla
    fields = ['nom_plato', 'prec_plato', 'desc_plato', 'pedido_estado']
    success_url = "/funciones/funciones admin"

    def form_valid(self, form):
        # Realizar alguna lógica adicional si es necesario
        return super().form_valid(form)

# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('nom_plato') and request.POST.get('desc_plato') and request.POST.get('prec_plato'):
#                 post= Platos()
#                 post.nom_plato= request.POST.get('nom_plato')
#                 post.desc_plato= request.POST.get('desc_plato')
#                 post.prec_plato= request.POST.get('prec_plato')
#                 post.save()
                
#                 return render(request, '/funciones/funciones admin')  

#         else:
#                 return render(request,'/funciones/funciones admin')
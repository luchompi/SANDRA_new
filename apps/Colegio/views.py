from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Sede,Curso
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,View
from .forms import sedeForm

class SedeListView(LoginRequiredMixin,ListView):
    login_url='/auth/login'
    model = Sede
    template_name = "Colegio/Sede/index.html"

class SedeCreateView(LoginRequiredMixin,CreateView):
    login_url='/auth/login'
    model = Sede
    form=sedeForm
    fields = ['nombre','direccion','telefono','correo']
    success_url='/colegio/sedes/'
    template_name = "Colegio/Sede/create.html"


class SedeDetailView(LoginRequiredMixin,DetailView):
    login_url='/auth/login'
    model = Sede
    template_name='Colegio/Sede/list.html'

class SedeUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/auth/login'
    model = Sede
    form=sedeForm
    fields = ['nombre','direccion','telefono','correo']
    success_url='/colegio/sedes/'
    template_name="Colegio/Sede/update.html"


class SedeDeleteView(LoginRequiredMixin,DeleteView):
    login_url="/auth/login"
    model = Sede
    success_url='/colegio/sedes/'
    template_name = "Colegio/Sede/delete.html"

class CursoListView(LoginRequiredMixin,ListView):
    login_url='/auth/login'
    model = Curso
    template_name = "Colegio/Curso/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list']=Curso.objects.all()
        return context

class GenerarCursos(LoginRequiredMixin,View):
    login_url='/auth/login/'
    def get(self,request,**kwargs):
        query = Sede.objects.all()
        for element in range(1,query.count()+1):
            for i in range(1,12):
                try:
                    Curso.objects.create(curso=i,sede=element)
                except:
                    pass
        return redirect('colegio:cursoIndex')

class borrarCurso(LoginRequiredMixin,View):
    login_url='/auth/login/'
    def get(self,request,**kwargs):
        ide =self.kwargs['pk']
        Curso.objects.get(curso=ide).delete()
        return redirect('colegio:cursoIndex')
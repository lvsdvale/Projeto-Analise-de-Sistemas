from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.contrib import messages
from django.db import models
from marker.models import *

# Create your views here.
class SubtaskView(ListView):
    template_name = 'index.html'
    context_object_name = 'index'
    paginate_by = 5

    def get_queryset(self):
        queryset = SubTaskModel.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(name__icontains=q) | models.Q(descricao__icontains=q)
            )

        return queryset
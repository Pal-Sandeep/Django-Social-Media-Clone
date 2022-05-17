from calendar import c
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                            PermissionRequiredMixin, )
from django.urls import reverse
from django.views import generic

from .models import Group,GroupMember
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
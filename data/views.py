from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from data.models import KeyWords

class IndexView(generic.ListView):
    template_name = 'data/index.html'
    model = KeyWords

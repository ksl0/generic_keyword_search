from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from data.models import KeyWords
from django.conf import settings

class IndexView(generic.ListView):
    model = KeyWords 
    template_name = 'data/index.html'
    
words = 'cheesestick'
#add a regrex function here
#KeyWords.objects.all()[0].topic

total = settings.T_KEY.search(q=words, count=2)

text = []
username = []
text = total['statuses'][0]['text']
username = total['statuses'][0]['user']['screen_name']




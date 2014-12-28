from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse

from data.models import KeyWords

def index(request):
    template= loader.get_template('data/index.html')

    def unwritten(model, n_results): 
	#for simplicity, assuming that we only have one topic 
	#total_topics = []
	topic1 = model.objects.all()[0].topic
	topic1.encode("ascii",'ignore')
	total_twitter_output = settings.T_KEY.search(q=topic1, count=n_results)
	tweet_list = []   
        user_list = []
	
	for i in xrange(0,n_results): 
	# call a filtering function here      
	    text = total_twitter_output['statuses'][i]['text'].encode("ascii", 'ignore')
	    username = total_twitter_output['statuses'][i]['user']['screen_name'].encode("ascii", 'ignore')
	    tweet_list.append([username, text])
	    #response.write("<div><p> username </p><p> text </p></div>")
	return tweet_list 

    context = RequestContext(request, {
             'datapoints':  unwritten(KeyWords, 47)
    })
   
    return HttpResponse(template.render(context))
    
     
    
#def filter_results(results): 


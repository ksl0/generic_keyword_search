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

	num_results = total_twitter_output['search_metadata']['count']
	print num_results
	for i in xrange(0,1): 
             	
	# call a filtering function here      
            #response.write("<div><p> username </p><p> text </p></div>")
            #total_twitter_output['statuses'][0]['id']
            #total_twitter_output["statuses"][0]["user"]["profile_image_url_https"]
            #saving a Person to the model 
            status_id = total_twitter_output['statuses'][i]['id']
	    time = total_twitter_output['statuses'][i]['user']['created_at']
	    text = total_twitter_output['statuses'][i]['text'].encode("ascii", 'ignore')
	    username = total_twitter_output['statuses'][i]['user']['screen_name'].encode("ascii", 'ignore')
            pic = total_twitter_output['statuses'][i]['user']['profile_image_url']
	    tweet_list.append([username, status_id, text,time, pic])
	    #response.write("<div><p> username </p><p> text </p></div>")
	return tweet_list 

    context = RequestContext(request, {
             'datapoints':  unwritten(KeyWords, 100)
    })
   
    return HttpResponse(template.render(context))
    
     
    
#def filter_results(results): 


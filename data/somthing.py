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


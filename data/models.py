from django.db import models


class KeyWords(models.Model): 
#    total_search_terms= models.CharField(max_length=200)
#    exact_phrase = models.CharField(max_length=100)
#    ignore_words = models.CharField(max_length=200)
    topic = models.CharField(max_length = 150)
    def words(self): 
        return self.total_search_terms
    def __unicode__(self):
        return self.topic
#takes in a word and prints out the rest


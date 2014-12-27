from django.db import models


class KeyWords(models.Model): 
    total_search_terms= models.CharField(max_length=200)
#    exact_phrase = models.CharField(max_length=100)
#    ignore_words = models.CharField(max_length=200)
    topic = models.CharField(max_length = 150)

    def __str__(self): 
        return self.topic
    def words(self): 
        return self.total_search_terms
  

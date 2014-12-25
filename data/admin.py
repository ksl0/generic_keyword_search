from django.contrib import admin
from models import KeyWords

class KeyWordsAdmin(admin.ModelAdmin): 
    fieldsets = [
        ('Topic', {'fields': ['topic']}), 
        ('Included Words', {'fields': ['total_search_terms']}), 
]

admin.site.register(KeyWords)

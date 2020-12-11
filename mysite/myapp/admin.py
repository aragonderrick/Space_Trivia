from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.suggestionModel)
admin.site.register(models.CommentModel)
admin.site.register(models.Profile)
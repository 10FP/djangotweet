from django.contrib import admin
from . import models
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fields = ["nickname", "tweet"]


admin.site.register(models.Tweet)
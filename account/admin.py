from django.contrib import admin
from .models import SubscribedUsers, CommentPerson
#Register your models here.

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email', 'date_created')

admin.site.register(SubscribedUsers,SubscribedUsersAdmin)
admin.site.register(CommentPerson)

#admin.site.register(CommentPerson)
from django.forms import forms

from account.models import SubscribedUsers

class NewsletterForm(forms.Form):
    class Meta:
        model= SubscribedUsers
        fields = "__all__"
from django import forms
from cmsplugin_contact.forms import ContactForm

class CustomContactForm(ContactForm):
    template = "contact.html"

#from django import forms
#from django.core.mail import send_mail
#from django.utils.translation import ugettext, ugettext_lazy as _

#class ContactForm(forms.Form):
    #email = forms.EmailField(label=_('Your email address'))
    #message = forms.CharField(widget=forms.Textarea, label=_('Your message'))
    #def send_email(self):
       #subject = "from the contact page"
       #message = self.cleaned_data['message']
       #sender = self.cleaned_data['email']
       #recipients = ['contact@mlinbees.com']
       #send_mail(subject, message, sender, recipients)

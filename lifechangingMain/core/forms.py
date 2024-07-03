from django.forms import ModelForm
from .models import *

class T_receiverForm(ModelForm):
    class  Meta:
        model = T_receiver
        fields = '__all__'
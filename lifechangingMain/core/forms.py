from django.forms import ModelForm
from .models import *

class T_donorForm(ModelForm):
    class Meta:
        model = T_donor
        fields = '__all__'  

class P_donorForm(ModelForm):
    class Meta:
        model = P_donor
        fields = '__all__'
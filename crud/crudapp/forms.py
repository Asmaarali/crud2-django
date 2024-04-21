from django.forms import ModelForm
from .models import studentinfo

class studentform(ModelForm):
    class Meta:
        model=studentinfo
        fields="__all__"

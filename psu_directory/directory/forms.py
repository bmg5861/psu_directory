from django import forms  
from directory.models import Staff
class StaffForm(forms.ModelForm):  
    class Meta:  
        model = Staff  
        fields = "__all__"  
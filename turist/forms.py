from django.forms import ModelForm
from turist.models import Turist

class CreateTuristForm(ModelForm):

    class Meta:
        fields = ('name','content','rasmi','category')
        model = Turist
from django.forms import ModelForm
from .models import CellRecord


class RecordForm(ModelForm):
    class Meta:
        model = CellRecord
        fields = ['locomotive', 'techwork', 'month']

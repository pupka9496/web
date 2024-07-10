from django.forms import ModelForm, NumberInput, TextInput, CheckboxInput, RadioSelect, Select, DateInput
from main.models import NewAudits

class AuditsForm(ModelForm):
    class Meta:
        model = NewAudits
        fields = ['audit_id', 'name', 'date', 'auditor', 'plant', 'brief_description', 'description', 'report', 'status']

        widgets = {
            'name': TextInput(),
            'date': DateInput(),
            'auditor': TextInput(),
            'plant': NumberInput(),
            'brief_description': TextInput(),
            'description': TextInput(),
            'report': NumberInput(),
        }

import datetime
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Leave

def validate_date(date):
    today = timezone.now().date()
    if date <= today:
        print("validate-today------>>>>", f'{date} is already past {today}')
        raise ValidationError(
            _(f'{date} should not be later than {today}'),
            params={'date':date}
        )
    return date


class LeaveForm(forms.ModelForm):
    description = forms.CharField(label="Reason", max_length="100", widget=forms.Textarea, required=False)
    start_date  = forms.DateField(label="Start Date", initial=timezone.now().date(), validators=[validate_date], widget=forms.DateInput(attrs={'type': 'date'}))
    end_date  = forms.DateField(label="End Date", validators=[validate_date], widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Leave
        fields = ('employee', 'type', 'description', 'status', 'start_date', 'end_date',)
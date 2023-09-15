# forms.py
from django import forms
from event.models import Event, Organizer


class EventForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={"class": "text-small-pentest w-100"}),
    )

    description = forms.CharField(
        label="Descrição",
        widget=forms.Textarea(attrs={"class": "description w-100"}),
    )

    image = forms.ImageField(
        label="Imagem",
        widget=forms.FileInput(attrs={"class": "form-control-file"}),
    )

    start_date = forms.DateTimeField(
        label="Data de início",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    
    end_date = forms.DateTimeField(
        label="Data de término",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    organizer = forms.ModelChoiceField((Organizer.objects.all()), label="Organizador")

    class Meta:
        model = Event
        fields = ["name", "description", "image", "start_date", "end_date", "organizer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
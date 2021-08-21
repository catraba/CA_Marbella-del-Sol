from django import forms

from .models import Atleta, Marca


class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = '__all__'
        exclude = ('usuario', 'slug', 'imagen', 'categoria', )

        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'apellido1': forms.TextInput(attrs={'class': 'input', 'type': 'text'}),
            'apellido2': forms.TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'OPCIONAL'}),
            'edad': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'instagram': forms.TextInput(attrs={'class': 'input', 'placeholder': 'OPCIONAL'})
        }


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        exclude = ('usuario', )

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'tiempo': forms.DateInput(attrs={'class': 'input', 'type': 'number', 'step': 0.01, 'min': 0}),
        }
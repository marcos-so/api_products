import django.forms as forms
from . import models

class ContactForm(forms.Form):
    name = forms.CharField(label='Seu nome', max_length=100, required=True, help_text='Digite seu nome completo.')
    email = forms.EmailField(label='Seu email', required=True, help_text='Digite um email válido.')

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = [
            'category',
            'name',
            'description',
            'price',
            'stock',
            'is_available',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'price': forms.NumberInput(attrs={'class': 'form-control'}),

            'stock': forms.NumberInput(attrs={'class': 'form-control'}),

            'category': forms.Select(attrs={'class': 'form-control'}),

            'is_available': forms.CheckboxInput(),
        }

        labels = {
            'name': 'Nome do Produto',
            'description': 'Descrição',
            'price': 'Preço',
            'stock': 'Estoque',
            'category': 'Categoria',
            'is_available': 'Disponível para venda?',
        }
from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    achtung_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name'].lower()

        for word in self.achtung_words:
            if word in cleaned_data:
                raise forms.ValidationError('В названии содержится запрещенное слово')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description'].lower()

        for word in self.achtung_words:
            if word in cleaned_data:
                raise forms.ValidationError('В описании содержится запрещенное слово')

        return cleaned_data

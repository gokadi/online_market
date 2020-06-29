from django import forms

from online_market.products.models import Category


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            query = self.fields['parent_category'].queryset
            self.fields['parent_category'].queryset = query.exclude(
                pk=self.instance.pk
            )

    class Meta:
        model = Category
        fields = '__all__'

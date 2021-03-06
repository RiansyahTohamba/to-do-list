from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item, List

DUPLICATE_ITEM_ERROR = "You've already got this in your list"

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text','deadline',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'id': 'id_new_item',
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
            'deadline': forms.fields.DateInput(attrs={
                'class': 'form-control input-lg',
            }),
        }



class NewListForm(ItemForm):

    def save(self, owner):
        if owner.is_authenticated:
            return List.create_new(first_item_text=self.cleaned_data['text'], owner=owner)
        else:
            return List.create_new(first_item_text=self.cleaned_data['text'])



class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list


    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)


from django import forms

from world_of_speed.cars.models import Car


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = True


from django.forms.widgets import TextInput
from .models import sell_property,sell_property1
from django import forms
from django.forms import Textarea, IntegerField,TextInput
class sell_property_Form(forms.ModelForm):
    class Meta:
        model = sell_property
        fields = '__all__'
        labels = {'photo':''}
        widgets={
            'Property_Description' : Textarea(
                attrs={
                    "class":"new-class-name three",
                    "rows":9,
                    "cols":130,
                    "placeholder":"Add Description with Contact Details"
                    }),
            'Property_Name' : TextInput(attrs={"placeholder":"property name"}),
            #'Property_Description' : TextInput(attrs={"placeholder":"Add Description with Contact Details"}),
            'Area' : TextInput(attrs={"placeholder":"500 sq. ft."}),
            'Location' : TextInput(attrs={"placeholder":"Mumbai"}),
            'Price' : TextInput(attrs={"placeholder":"Rs 5000000"}),  
            'Status' : TextInput(attrs={"placeholder":"On Sale/Sold"}),
            'rent_or_sell' : TextInput(attrs={"placeholder":"Sale/Rent"}), 
        }


class sell_property_Form1(forms.ModelForm):
    class Meta:
        model = sell_property1
        fields = '__all__'
        labels = {'photo1':'','photo2':'','photo3':''}
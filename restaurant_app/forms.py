from django import forms
from restaurant_app.models import Table,MenuItem,MenuCategory

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields=['table_number','capacity','status']
        

# class MenuCategoryForm(forms.ModelForm):
#     class Meta:
#         model=MenuCategory
#         fields=['name','description']
#         widgets={'name':forms.TextInput(attrs={'class':'for23m-control'}),'description':forms.Textarea(attrs={'class':'form-control','rows':3}),}


# class MenuItemForm(forms.ModelForm):
#     class Meta:
#         model=MenuItem
#         fields=['name','category','price','availability','image']
#         widgets={'name':forms.TextInput}
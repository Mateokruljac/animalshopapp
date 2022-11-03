from django import forms 
from .models import Animal, Category, Comments, Tag

class AnimalForms(forms.ModelForm):
    class Meta: 
        model = Animal
        fields = ["name","about","tag","species","img","status","price"]
        widgets = {
            "name" : forms.TextInput(attrs = {"placeholder": "Name", "class":"form-control"}),
            "tag" : forms.SelectMultiple(attrs = {"class":"form-control"}),
            "species" : forms.Select(attrs = {"class":"form-control"}),
            "status" : forms.Select(attrs = {"class":"form-control"}),
            "price" : forms.NumberInput(attrs = {"class":"form-control"}),
            "about" : forms.TextInput(attrs = {"class":"form-control","placeholder":"Write..."})
        }
        
        


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title" : forms.TextInput(attrs = {"placeholder":"name","class":"form-control"})
        }
        
        

        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name" : forms.TextInput(attrs = {"placeholder":"name","class":"form-control"})
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["name","body"]
        widgets = {
            "name":  forms.TextInput(attrs = {"placeholder":"Name","class":"form-control"}),
            "body":  forms.TextInput(attrs = {"placeholder":"Write...","class":"form-control"})
        }
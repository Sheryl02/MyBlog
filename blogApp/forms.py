from django import forms
from .models import Post, Category, Comment, Profile
# from .models import Post, Category


# choices = [('Origmai', 'Origami'), ('Photography','Photography'), ('Painting','Painting')]
choices = Category.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
    choice_list.append(item)


class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

# class postForm(forms.ModelForm):
#     title = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control'}))
#     author= forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control'})),
#     body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={'class':'form-control'})),
#     category = forms.ChoiceField(choices = choice_list)
#
#     class Meta:
#         model = Post
#         fields = ['title', 'author','body','category']
#         # fields = ['title', 'author','body']
#
#         # widgets = {
#         #     'title':forms.TextInput(attrs={'class':'form-control'}),
#         #     'author':forms.TextInput(attrs={'class':'form-control'}),
#         #     'body':forms.Textarea(attrs={'class':'form-control'}),
#         #     'category':forms.Select(choices = choice_list, attrs={'class':'from-control'})
#         #     # 'category':forms.Select()
#         #
#         # }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body', 'category']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            # 'category':forms.Select(choices = choice_list, attrs={'class':'from-control'})
            'category':forms.SelectMultiple(choices = choice_list, attrs={'class':'form-control'})
        }

class addCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'your_comments']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'your_comments':forms.Textarea(attrs={'class':'form-control','placeholder':'Please leave your comments here.'}),
        }

from django import forms
from django.forms  import FileInput
from. models import Post

class PostForm(forms.ModelForm):
	title =forms.CharField(label='title',widget=forms.TextInput(attrs={'class':'form-control',}))
	content =forms.CharField(label='content',widget=forms.Textarea(attrs={'class':'form-control',}))
	image = forms.ImageField(label='Image', widget=FileInput(attrs={'class': 'form-control-file'}))
	class Meta:
		model=Post
		fields=('title','content','image')
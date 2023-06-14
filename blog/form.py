from django import forms

#
# class CommentModelForm(forms.ModelForm):
#     class Meta:
#         model = CommentModel
#         exclude = ['post', 'created_at']

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

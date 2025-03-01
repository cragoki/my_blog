from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {"user_name": "Your Name",
                  "user_email": "Your Email",
                  "text": "Your Comment"}

    user_name = forms.CharField(max_length=120)
    user_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

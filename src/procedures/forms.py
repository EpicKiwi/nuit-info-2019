from django import forms
from procedures.models import Tag


class CommentForm(forms.Form):

	step_content_id = forms.IntegerField(widget=forms.HiddenInput, required=True)
	comment = forms.CharField(
		widget=forms.Textarea(attrs={
			"placeholder": "Ecrivez une astuces pour les suivants..."
		}), required=True)
	tag = forms.ModelChoiceField(Tag.objects.all(), required=False)

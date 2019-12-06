from django import forms


class CommentForm(forms.Form):

	step_content_id = forms.IntegerField(widget=forms.HiddenInput, required=True)
	comment = forms.CharField(
		widget=forms.Textarea(attrs={
			"placeholder": "Ecrivez une astuces pour les suivants..."
		}), required=True)

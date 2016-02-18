from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _

class BlogForm(forms.Form):
	title = forms.CharField(
		label=_("Title"),
		widget=forms.Textarea,
		required=True,
		max_length=255,
	)
	description = forms.CharField(
		label=_("Description"),
		widget=forms.Textarea,
		required=True,
		max_length=255,
	)
	content = forms.CharField(
		label = _("Content"),
		widget=forms.Textarea,
		required=True,
	)
	
	published = forms.BooleanField(
		label = _("Publish now?"),
		required=False,
		initial=True,
	)
from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['pdf']
        required = ['pdf']
        readonly_fields = ['uploaded_at']

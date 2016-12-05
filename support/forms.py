from django import forms

class supportForm(forms.Form):
    Name = forms.CharField(required=True, max_length=100)
    Email = forms.EmailField(required=True, max_length=100)
    Disputes = forms.CharField(required=True, max_length=100)
    Feedback = forms.CharField(required=True, widget=forms.Textarea, help_text='Enter Adjustments & Cancellations here')




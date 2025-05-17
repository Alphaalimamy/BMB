from django import forms
from .models import Volunteer, Donation, BlogPost, Event, PolicyPosition

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'first_name', 'last_name', 'email', 'phone', 
            'address', 'city', 'state', 'zip_code',
            'skills', 'availability', 'interests'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'availability': forms.Textarea(attrs={'rows': 3}),
            'interests': forms.Textarea(attrs={'rows': 3}),
        }

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'donor_first_name', 'donor_last_name', 'donor_email',
            'amount', 'payment_method', 'is_recurring'
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={'min': 1}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title', 'slug', 'content', 'excerpt', 
            'featured_image', 'is_published', 'published_at'
        ]
        widgets = {
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'content': forms.Textarea(attrs={'rows': 20}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'category', 'content', 'excerpt', 
                 'featured_image', 'is_published', 'published_at']
        widgets = {
            'published_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'content': forms.Textarea(attrs={'rows': 20}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 
                 'start_time', 'end_time', 'image', 'registration_link']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PolicyPositionForm(forms.ModelForm):
    class Meta:
        model = PolicyPosition
        fields = ['title', 'slug', 'summary', 'detailed_position', 'icon', 'priority']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'detailed_position': forms.Textarea(attrs={'rows': 10}),
        }
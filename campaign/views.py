from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils import timezone
from .models import BlogPost, Volunteer, Event, PolicyPosition, ContactMessage
from .forms import VolunteerForm, ContactForm, BlogPostForm, BlogPostForm, EventForm, PolicyPositionForm

def home(request):
    # Get latest published blog posts (3 most recent)
    latest_posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')[:3]
    
    # Get upcoming events
    upcoming_events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')[:3]
    
    # Get key policies (4 highest priority)
    key_policies = PolicyPosition.objects.all().order_by('priority')[:4]
    
    context = {
        'latest_posts': latest_posts,
        'upcoming_events': upcoming_events,
        'key_policies': key_policies,
    }
    return render(request, 'home.html', context)

def blog_list(request):
    # Get all published blog posts ordered by publish date
    posts_list = BlogPost.objects.filter( is_published=True ).order_by('-published_at')
    
    # Paginate the results (6 per page)
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, slug):
    # Get the blog post or return 404 if not found
    post = get_object_or_404(BlogPost, slug=slug,  is_published=True )
    context = {'post': post}
    return render(request, 'blog_detail.html', context)

def volunteer(request):
    if request.method == 'POST':
        # If form was submitted, process it
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_thanks')
    else:
        # If GET request, show empty form
        form = VolunteerForm()
    
    context = {'form': form}
    return render(request, 'volunteer.html', context)

def volunteer_thanks(request):
    return render(request, 'volunteer_thanks.html')

def events(request):
    # Get all upcoming events
    events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    context = {'events': events}
    return render(request, 'events.html', context)

def policies(request):
    # Get all policies ordered by priority
    policies = PolicyPosition.objects.all().order_by('priority')
    context = {'policies': policies}
    return render(request, 'policies.html', context)

def policy_detail(request, slug):
    # Get the policy or return 404 if not found
    policy = get_object_or_404(PolicyPosition, slug=slug)
    
    context = {'policy': policy}
    return render(request, 'policy_detail.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                # submitted_at is set automatically in the model
            )
            return redirect('contact_thanks')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def contact_thanks(request):
    return render(request, 'contact_thanks.html')



def is_admin(user):
    return user.is_authenticated and user.is_staff

# Blog Views
@user_passes_test(is_admin)
def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_post_list') 
            # return redirect(post.get_absolute_url())
    else:
        form = BlogPostForm()
    return render(request, 'admin/blog_post_form.html', {
        'form': form,
        'title': 'Create Blog Post'
    })

@user_passes_test(is_admin)
def blog_post_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list') 
            #return redirect(post.get_absolute_url())
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'admin/blog_post_form.html', {
        'form': form,
        'title': 'Edit Blog Post'
    })

@user_passes_test(is_admin)
def blog_post_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_post_list')
    return render(request, 'confirm_delete.html', {
        'object': post,
        'type': 'blog post'
    })

# Event Views
@user_passes_test(is_admin)
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('event_list') 
            # return redirect('events')
    else:
        form = EventForm()
    return render(request, 'admin/event_form.html', {
        'form': form,
        'title': 'Create Event'
    })

@user_passes_test(is_admin)
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list') 
            # return redirect('events')
    else:
        form = EventForm(instance=event)
    return render(request, 'admin/event_form.html', {
        'form': form,
        'title': 'Edit Event'
    })

@user_passes_test(is_admin)
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'admin/confirm_delete.html', {
        'object': event,
        'type': 'event'
    })

# Policy Views
@user_passes_test(is_admin)
def policy_create(request):
    if request.method == 'POST':
        form = PolicyPositionForm(request.POST)
        if form.is_valid():
            policy = form.save()
            return redirect('policy_list') 
            #return redirect(policy.get_absolute_url())
    else:
        form = PolicyPositionForm()
    return render(request, 'admin/policy_form.html', {
        'form': form,
        'title': 'Create Policy'
    })

@user_passes_test(is_admin)
def policy_edit(request, slug):
    policy = get_object_or_404(PolicyPosition, slug=slug)
    if request.method == 'POST':
        form = PolicyPositionForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            return redirect(policy_list)
    else:
        form = PolicyPositionForm(instance=policy)
    return render(request, 'admin/policy_form.html', {
        'form': form,
        'title': 'Edit Policy'
    })

@user_passes_test(is_admin)
def policy_delete(request, slug):
    policy = get_object_or_404(PolicyPosition, slug=slug)
    if request.method == 'POST':
        policy.delete()
        return redirect('policy_list')
    return render(request, 'admin/confirm_delete.html', {
        'object': policy,
        'type': 'policy'
    })



@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

@user_passes_test(is_admin)
def blog_post_list(request):
    posts = BlogPost.objects.all().order_by('-published_at')
    return render(request, 'admin/blog_post_list.html', {'posts': posts})

@user_passes_test(is_admin)
def event_list(request):
    events = Event.objects.all().order_by('-start_time')
    return render(request, 'admin/event_list.html', {'events': events})

@user_passes_test(is_admin)
def policy_list(request):
    policies = PolicyPosition.objects.all().order_by('priority')
    return render(request, 'admin/policy_list.html', {'policies': policies})

@user_passes_test(is_admin)
def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by('-created_at')
    return render(request, 'admin/volunteer_list.html', {'volunteers': volunteers})

@user_passes_test(is_admin)
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by('-submitted_at')
    return render(request, 'admin/contact_list.html', {'contacts': contacts})

@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        'blog_count': BlogPost.objects.count(),
        'event_count': Event.objects.count(),
        'policy_count': PolicyPosition.objects.count(),
        'volunteer_count': Volunteer.objects.count(),
        'contact_count': ContactMessage.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)
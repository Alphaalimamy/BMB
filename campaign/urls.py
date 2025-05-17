from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer/thanks/', views.volunteer_thanks, name='volunteer_thanks'),
    path('events/', views.events, name='events'),
    path('policies/', views.policies, name='policies'),
    path('policies/<slug:slug>/', views.policy_detail, name='policy_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    
        # Single admin entry point
    path('manage/', views.admin_dashboard, name='admin_home'),
    
    # Dashboard
    path('manage/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Blog URLs
    path('manage/blog/', views.blog_post_list, name='blog_post_list'),
    path('manage/blog/create/', views.blog_post_create, name='blog_post_create'),
    path('manage/blog/edit/<slug:slug>/', views.blog_post_edit, name='blog_post_edit'),
    path('manage/blog/delete/<slug:slug>/', views.blog_post_delete, name='blog_post_delete'),
    
    # Event URLs
    path('manage/events/', views.event_list, name='event_list'),
    path('manage/events/create/', views.event_create, name='event_create'),
    path('manage/events/edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('manage/events/delete/<int:pk>/', views.event_delete, name='event_delete'),
    
    # Policy URLs
    path('manage/policies/', views.policy_list, name='policy_list'),
    path('manage/policies/create/', views.policy_create, name='policy_create'),
    path('manage/policies/edit/<slug:slug>/', views.policy_edit, name='policy_edit'),
    path('manage/policies/delete/<slug:slug>/', views.policy_delete, name='policy_delete'),
    
    # Other URLs
    path('manage/volunteers/', views.volunteer_list, name='volunteer_list'),
    path('manage/contacts/', views.contact_list, name='contact_list'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
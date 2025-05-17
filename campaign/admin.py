from django.contrib import admin
from .models import BlogPost, Volunteer, Donation, Event, PolicyPosition, Category, ContactMessage

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ('-published_at',)
    raw_id_fields = ('author',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'content', 'excerpt', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at'),
            'classes': ('collapse',)
        }),
    )

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'city', 'state', 'created_at')
    list_filter = ('state', 'city', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'city')
    date_hierarchy = 'created_at'

class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_first_name', 'donor_last_name', 'amount', 'payment_method', 'created_at')
    list_filter = ('payment_method', 'is_recurring', 'created_at')
    search_fields = ('donor_first_name', 'donor_last_name', 'donor_email')
    date_hierarchy = 'created_at'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_time', 'end_time')
    list_filter = ('start_time',)
    search_fields = ('title', 'location', 'description')
    date_hierarchy = 'start_time'

class PolicyPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'created_at')
    list_filter = ('priority',)
    search_fields = ('title', 'summary', 'detailed_position')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(PolicyPosition, PolicyPositionAdmin)
admin.site.register(Category)
admin.site.register(ContactMessage)
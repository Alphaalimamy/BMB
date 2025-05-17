from django.conf import settings

def campaign_context(request):
    return {
        'candidate_name': settings.CAMPAIGN_SETTINGS['candidate_name'],
        'position': settings.CAMPAIGN_SETTINGS['position'],
        'campaign_email': settings.CAMPAIGN_SETTINGS['campaign_email'],
        'campaign_phone': settings.CAMPAIGN_SETTINGS['campaign_phone'],
    }
from django.shortcuts import get_object_or_404, render_to_response

from django_surveys.models import SurveyGroup, Survey
from django_surveys.views import do_survey

def survey(request, survey_slug):
    
    survey_group = get_object_or_404(SurveyGroup, slug=survey_slug)
    survey, created = Survey.objects.get_or_create(survey_group=survey_group)

    return do_survey(request, survey, template_name=['perusal/%s.html' % survey_group.slug, 'purusal/generic.html'])



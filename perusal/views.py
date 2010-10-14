from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django_surveys.models import SurveyGroup, Survey
from django_surveys.views import do_survey

def survey(request, survey_slug):
    
    survey_group = get_object_or_404(SurveyGroup, slug=survey_slug)
    survey = Survey(survey_group=survey_group)
    return do_survey(request, survey, template_name=['perusal/%s.html' % survey_group.slug, 'perusal/generic.html'])



def index(request):
    return render_to_response('perusal/index.html', {}, context_instance=RequestContext(request))

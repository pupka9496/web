from django.shortcuts import render
from django.template.defaulttags import register
from django.urls import reverse_lazy
from django.http import HttpResponse
from main.models import NewAudits, NewReport
from django.views.generic import UpdateView, CreateView, DetailView
from .forms import AuditsForm

@register.filter
def get_status(value):
    dic = {
        'completed': 'согласовано',
        'not completed': 'не согласовано',
        'pending': 'на доработку',
    }
    return dic[value.lower()]

def main(request):
    audits = NewAudits.objects.all()

    data = {
        'audits': audits,
    }

    return render(request, 'audits/audits.html', data)

class Audit(DetailView):
    model = NewReport
    template_name = 'audits/audit.html'
    context_object_name = 'report'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        audits = NewAudits.objects.all()
        context['audits'] = audits

        return context
    
class CreateAudit(CreateView):
    template_name = 'audits/create_audit.html'
    form_class = AuditsForm
    success_url = reverse_lazy('page2')


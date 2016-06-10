from django.contrib import messages
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse

from tjfail.forms import FailSubmissionForm
from tjfail.models import Fail


class IndexView(FormView):
    template_name = 'tjfail/index.html'
    form_class = FailSubmissionForm

    def get_context_data(self, **kw):
        ctx = super(IndexView, self).get_context_data(**kw)
        ctx['fails'] = Fail.objects.filter(approved=True)
        return ctx

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Fail has been received and is pending moderation.')
        return super(IndexView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


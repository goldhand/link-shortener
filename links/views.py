from djago.view.generic import CreateView, ListView
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import Link


class LinkCreate(LoginRequiredMixin, CreateView):

    model = Link
    fields = ['base_url', 'name']

    def get_success_url(self):
        return reverse('links:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(LinkCreate, self).form_valid(form)


class LinkListView(LoginRequiredMixin, ListView):

    model = Link

    def get_queryset(self):
        '''
        return links that a user owns
        '''
        return Link.objects.filter(owner=self.request.user)

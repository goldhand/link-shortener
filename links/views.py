from django.views.generic import CreateView, ListView, RedirectView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin

from .models import Link


class LinkCreate(LoginRequiredMixin, CreateView):
    '''
    creates a new link to shorten
    '''

    model = Link
    fields = ['base_url', 'name']

    def get_success_url(self):
        return reverse('links:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(LinkCreate, self).form_valid(form)


class LinkList(LoginRequiredMixin, ListView):
    '''
    lists links for a user
    '''

    model = Link

    def get_queryset(self):
        '''
        return links that a user owns
        '''
        return Link.objects.filter(owner=self.request.user)

    def get_context_data(self):
        context = super(LinkList, self).get_context_data()
        context['domain'] = self.request.get_host().lower()
        return context


class LinkRedirect(SingleObjectMixin, RedirectView):
    '''
    redirects a request to the link base_url
    '''

    permanent = False
    model = Link
    pk_url_kwarg = 'pk'  # TODO: Does SingleObjectMixin need this?

    def get_redirect_url(self, pk):
        return self.get_object().base_url


class LinkDelete(LoginRequiredMixin, DeleteView):
    '''
    Deletes a link
    '''

    model = Link

    def get_queryset(self):
        '''
        users can only delete links they own
        '''
        return Link.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('links:list')

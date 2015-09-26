from django.views.generic import (CreateView, ListView, RedirectView,
                                  DeleteView, UpdateView)
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

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

    def get_context_data(self, *args, **kwargs):
        context = super(LinkCreate, self).get_context_data(*args, **kwargs)
        context['action_url'] = reverse('links:create')
        return context


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


class LinkRedirect(RedirectView):
    '''
    redirects a request to the link base_url
    '''

    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, link_key=kwargs['link_key'])
        return link.base_url


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


class LinkUpdate(LoginRequiredMixin, UpdateView):
    '''
    Updates a link
    '''

    model = Link
    fields = ['base_url', 'name', 'link_key']

    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('links:list')

    def get_context_data(self, *args, **kwargs):
        context = super(LinkUpdate, self).get_context_data(*args, **kwargs)
        context['action_url'] = reverse('links:update',
                                        kwargs={'pk': self.get_object().pk})
        return context

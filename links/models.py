import uuid

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Link(models.Model):
    '''
    A shortenable link
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    base_url = models.URLField(help_text='Link you would like to shorten',
                               verbose_name='URL')
    name = models.CharField(max_lenght=255,
                            help_text='Title of page link is going to')

    owner = models.ForeignKey(settings.USER_MODEL)

    def __unicode__(self):
        return u'{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('links:detail', self.id)

    def shortend_url(self):
        '''
        link that request should be routed to
        '''
        return reverse('links:shorten', self.id)

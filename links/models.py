import uuid

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from .settings import DEFAULT_LINK_LENGTH


def set_link_key():
    return uuid.uuid4().hex.title()[:DEFAULT_LINK_LENGTH]


def get_unique_link_key(link):
    '''
    make sure link that is returned is unique
    '''
    link_key = link.link_key
    while Link.objects.exclude(id=link.id).filter(link_key=link_key):
        link_key = set_link_key()
    return link_key


class Link(models.Model):
    '''
    A shortenable link
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    base_url = models.URLField(help_text='Link you would like to shorten',
                               verbose_name='URL')
    name = models.CharField(max_length=255,
                            help_text='Title of page link is going to')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    link_key = models.SlugField(unique=True, max_length=100,
                                default=set_link_key,
                                help_text='Custom shortend version of link')

    def __unicode__(self):
        return u'{}'.format(self.name)

    def __init__(self, *args, **kwargs):
        '''
        assert link_key is unique when object is initialized
        '''
        super(Link, self).__init__(*args, **kwargs)
        self.link_key = get_unique_link_key(self)

    def shortend_url(self):
        '''
        link that request should be routed to
        '''
        return reverse('links:shorten', kwargs={'link_key': self.link_key})

# -*- coding: utf-8 -*-

from wsgitraining.site import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SentryEventView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('sentry-event-view.pt')

    def __call__(self):
        # Implement your own actions:
        raise AttributeError('Hi Sentry')
        self.msg = _(u'A small message')
        return self.index()

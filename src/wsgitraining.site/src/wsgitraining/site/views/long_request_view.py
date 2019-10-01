# -*- coding: utf-8 -*-

from wsgitraining.site import _
from Products.Five.browser import BrowserView
from time import sleep

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LongRequestView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('long-request-view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        for i in range(13):
            sleep(1.0)
        return self.index()

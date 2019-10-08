# -*- coding: utf-8 -*-

from wsgitraining.site import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AttributeErrorView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('attribute_error_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        raise AttributeError
        return self.index()

# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import wsgitraining.site


class WsgitrainingSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=wsgitraining.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'wsgitraining.site:default')


WSGITRAINING_SITE_FIXTURE = WsgitrainingSiteLayer()


WSGITRAINING_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WSGITRAINING_SITE_FIXTURE,),
    name='WsgitrainingSiteLayer:IntegrationTesting',
)


WSGITRAINING_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WSGITRAINING_SITE_FIXTURE,),
    name='WsgitrainingSiteLayer:FunctionalTesting',
)


WSGITRAINING_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        WSGITRAINING_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='WsgitrainingSiteLayer:AcceptanceTesting',
)

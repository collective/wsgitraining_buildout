# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from wsgitraining.site.testing import WSGITRAINING_SITE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that wsgitraining.site is properly installed."""

    layer = WSGITRAINING_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if wsgitraining.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'wsgitraining.site'))

    def test_browserlayer(self):
        """Test that IWsgitrainingSiteLayer is registered."""
        from wsgitraining.site.interfaces import (
            IWsgitrainingSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IWsgitrainingSiteLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = WSGITRAINING_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['wsgitraining.site'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if wsgitraining.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'wsgitraining.site'))

    def test_browserlayer_removed(self):
        """Test that IWsgitrainingSiteLayer is removed."""
        from wsgitraining.site.interfaces import \
            IWsgitrainingSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IWsgitrainingSiteLayer,
            utils.registered_layers())

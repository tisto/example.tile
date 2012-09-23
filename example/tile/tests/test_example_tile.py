# -*- coding: utf-8 -*-
from zope.component import queryUtility
#from plone.app.texttile.tile import ITextTile
from plone.tiles.interfaces import ITileType
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, \
    setRoles, login
from plone.registry.interfaces import IRegistry

from example.tile.testing import \
    EXAMPLE_TILE_INTEGRATION_TESTING


class ExampleTileIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_TILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Document', 'doc')
        self.doc = self.portal.doc

    def test_tile_exists(self):
        from example.tile.tile import ExampleTile
        self.assertTrue(ExampleTile(self.portal, self.request))

    def test_file_rendering(self):
        from example.tile.tile import ExampleTile
        self.assertEqual(
            ExampleTile(self.portal, self.request)(),
            u"<html><body><p>Hello world</p></body></html>")

    def test_tiletype_registration(self):
        self.assertTrue(queryUtility(ITileType, name='example.tile'))
        self.assertEqual(
            queryUtility(ITileType, name='example.tile').title,
            "Example tile")
        self.assertEqual(
            queryUtility(ITileType, name='example.tile').description,
            "This is an example tile")

    def test_tile_registration(self):
        registry = queryUtility(IRegistry)
        self.assertTrue(u'example.tile' in registry['plone.app.tiles'])


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

# -*- coding: utf-8 -*-
import unittest2 as unittest

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, \
    setRoles, login

from example.tile.testing import \
    EXAMPLE_TILE_INTEGRATION_TESTING


class ExampleTileIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_TILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Document', 'doc')
        self.doc = self.portal.doc

    def test_pass(self):
        pass

#    def test_tile_registration(self):
#        tile = queryUtility(ITileType, name='example.tile')
#        self.assertEqual(tile.title, u"Text tile")
#        self.assertEqual(tile.schema, ITextTile)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

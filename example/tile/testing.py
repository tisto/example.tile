import doctest

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting


class ExampleTileLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import example.tile
        xmlconfig.file('configure.zcml', example.tile,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.tile:default')


EXAMPLE_TILE_FIXTURE = ExampleTileLayer()

EXAMPLE_TILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_TILE_FIXTURE,),
    name="ExampleTileLayer:Integration")
EXAMPLE_TILE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_TILE_FIXTURE,),
    name="ExampleTileLayer:Functional")
EXAMPLE_TILE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(EXAMPLE_TILE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ExampleTileLayer:Acceptance")

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

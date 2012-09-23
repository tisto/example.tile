from plone.tiles import Tile


class ExampleTile(Tile):

    def __call__(self):
        return u"<html><body><p>Hello world</p></body></html>"

"""
week05 homework assignment
"""

import cherrypy
import bookdb

class Page:
    # Store the page title in a class attribute
    title = 'Untitled Page'

    def header(self):
        return '''
            <html>
            <head>
                <title>%s</title>
            <head>
            <body>
        ''' % (self.title)

    def footer(self):
        return '''
            </body>
            </html>
        '''

class HomePage(Page):
    title = 'Book List'

    def __init__(self):
        self.bdb = bookdb.BookDB()
        self.ttls = self.bdb.titles()
        print self.ttls
        self.id1 = Id1Page(self.bdb)
        self.id2 = Id2Page(self.bdb)
        self.id3 = Id3Page(self.bdb)
        self.id4 = Id4Page(self.bdb)
        self.id5 = Id5Page(self.bdb)

    def index(self):
        yield self.header()

        yield '''
            <h2>%s</h2>
            <p>These are reference books:</p>
            <ul>''' % (self.title)

        for ttl in self.ttls:
            idn = ttl['id']
            yield '<li><a href="./' + idn + '/">' + ttl['title'] + '</a></li>'

        yield '</ul>'
        yield self.footer()
    index.exposed = True


class Id1Page(Page):

    def __init__(self, db):
        self.bdb = db
        self.info = self.bdb.title_info('id1')
        self.title = self.info['title']
        self.isbn = self.info['isbn']
        self.publisher = self.info['publisher']
        self.author = self.info['author']

    def index(self):
        yield self.header()
        yield '<p><br></p>'
        yield '<ul><li>Title     : ' + self.title + '</li> <li>ISBN      : ' + self.isbn + '</li> <li>Publisher : ' + self.publisher + '</li> <li>Author    : ' + self.author + '</li> </ul>'
        yield '<p>[<a href="..">Return</a>]</p>'
        yield self.footer()
    index.exposed = True

class Id2Page(Page):

    def __init__(self, db):
        self.bdb = db
        self.info = self.bdb.title_info('id2')
        self.title = self.info['title']
        self.isbn = self.info['isbn']
        self.publisher = self.info['publisher']
        self.author = self.info['author']

    def index(self):
        yield self.header()
        yield '<p><br></p>'
        yield '<ul><li>Title     : ' + self.title + '</li> <li>ISBN      : ' + self.isbn + '</li> <li>Publisher : ' + self.publisher + '</li> <li>Author    : ' + self.author + '</li> </ul>'
        yield '<p>[<a href="..">Return</a>]</p>'
        yield self.footer()
    index.exposed = True

class Id3Page(Page):

    def __init__(self, db):
        self.bdb = db
        self.info = self.bdb.title_info('id3')
        self.title = self.info['title']
        self.isbn = self.info['isbn']
        self.publisher = self.info['publisher']
        self.author = self.info['author']

    def index(self):
        yield self.header()
        yield '<p><br></p>'
        yield '<ul><li>Title     : ' + self.title + '</li> <li>ISBN      : ' + self.isbn + '</li> <li>Publisher : ' + self.publisher + '</li> <li>Author    : ' + self.author + '</li> </ul>'
        yield '<p>[<a href="..">Return</a>]</p>'
        yield self.footer()
    index.exposed = True

class Id4Page(Page):

    def __init__(self, db):
        self.bdb = db
        self.info = self.bdb.title_info('id4')
        self.title = self.info['title']
        self.isbn = self.info['isbn']
        self.publisher = self.info['publisher']
        self.author = self.info['author']

    def index(self):
        yield self.header()
        yield '<p><br></p>'
        yield '<ul><li>Title     : ' + self.title + '</li> <li>ISBN      : ' + self.isbn + '</li> <li>Publisher : ' + self.publisher + '</li> <li>Author    : ' + self.author + '</li> </ul>'
        yield '<p>[<a href="..">Return</a>]</p>'
        yield self.footer()
    index.exposed = True

class Id5Page(Page):

    def __init__(self, db):
        self.bdb = db
        self.info = self.bdb.title_info('id5')
        self.title = self.info['title']
        self.isbn = self.info['isbn']
        self.publisher = self.info['publisher']
        self.author = self.info['author']

    def index(self):
        yield self.header()
        yield '<p><br></p>'
        yield '<ul><li>Title     : ' + self.title + '</li> <li>ISBN      : ' + self.isbn + '</li> <li>Publisher : ' + self.publisher + '</li> <li>Author    : ' + self.author + '</li> </ul>'
        yield '<p>[<a href="..">Return</a>]</p>'
        yield self.footer()
    index.exposed = True

# Of course we can also mount request handler objects right here!
root = HomePage()
cherrypy.tree.mount(root)

# Remember, we don't need to mount ExtraLinksPage here, because
# LinksPage does that itself on initialization. In fact, there is
# no reason why you shouldn't let your root object take care of
# creating all contained request handler objects.


if __name__ == '__main__':
    import os.path
    thisdir = os.path.dirname(__file__)
    cherrypy.quickstart(config=os.path.join(thisdir, 'w5_cherrypy.conf'))


from yaturbo import YandexTurboFeed

class TurboFeed(YandexTurboFeed):
    """
    More information on Django Syndication Feed Framework configuration:
    https://docs.djangoproject.com/en/2.0/ref/contrib/syndication/
    """

    turbo_sanitize = True  # Let's strip HTML tags unsupported by Turbo pages.

    def item_turbo(self, item):
        # By default Turbo contents is taken from `item_description`.
        # Here we take turbo page contents from `html` attribute of an item.
        # Since we have `turbo_sanitize = True`, our HTML will be sanitized
        # automatically.
        #
        # Take a note, that if we return falsy item would be considered
        # as not having turbo contents at all.
        #
        return item.get('html', '')

       # You can also override other item_turbo_* family members.

def feed(request_get):

    feed = MyFeed([
        {
            'title': 'a',
            'descr': 'turbo!',
            'link': 'd',
            'source': 'http://some.com',
            'topic': 'Title',
        },
        {
            'title': 'b',
            'descr': '<span><div data-x="y">sanitized</div></span>',
            'link': 'link_b',
        }
    ])

    feed.configure_ad_yandex('A-123', 'page-top')
    feed.configure_ad_yandex('B-123', 'page-bottom')

    feed.configure_analytics_yandex('12345', params={'key': 'value'})
    feed.configure_analytics_google('7890')

    content = feed(request_get('/')).content.decode('utf-8')

    chunks = [
        'xmlns:turbo="http://turbo.yandex.ru"',
        'xmlns:yandex="http://news.yandex.ru"',
        'turbo:analytics',
        'id="12345"',
        'id="7890"',
        'turbo:adNetwork',
        'id="A-123"',
        'turbo-ad-id="page-top"',
        'id="B-123"',
        'turbo-ad-id="page-bottom"',
        'item turbo="true"',
        '<turbo:content><![CDATA[turbo!]]></turbo:content>',
        '<turbo:source>http://some.com</turbo:source>',
        '<turbo:topic>Title</turbo:topic>',
        '<turbo:content><![CDATA[<div>sanitized</div>]]></turbo:content>',
    ]

    for chunk in chunks:
        assert chunk in content      
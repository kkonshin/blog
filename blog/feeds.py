from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Мой блог'
    link = '/'
    description = 'Новые записи в моем блоге'

    def items(self):
        return Post.published.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)


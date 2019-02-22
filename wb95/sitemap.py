from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost

class StaticSitemap(Sitemap):

    def items(self):
        return [
            'photography:home',
            'photography:contact',
            'photography:gallery',
            'blog:photography'
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):

    def items(self):
        return BlogPost.objects.all()

    def location(self, item):
        return reverse('blog:post', args=[item.slug])
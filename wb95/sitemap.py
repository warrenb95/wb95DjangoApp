from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import BlogPost

class StaticSitemap(Sitemap):

    def items(self):
        return [
            'photography:photography-home',
            'photography:photography-contact',
            'photography:photography-gallery',
            'blog:blog-photography'
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):

    def items(self):
        return BlogPost.objects.all()

    def location(self, item):
        return reverse('blog:photography-post', args=[item.slug])
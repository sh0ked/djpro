from django.views import generic
from django.utils import timezone
from nuash.models import Article


class IndexView(generic.ListView):
    template_name = 'nuash/index.html'

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Article
    template_name = 'nuash/detail.html'

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now())
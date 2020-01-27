from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Article, Comment
from django.urls import reverse

#
#
# # Create your views here.
def index(request):
    #return HttpResponse("hello here")
    latest_articles_list = Article.objects.order_by('-pub_date')    #[:5]
    return render(request, 'rwr/list.html', {'latest_articles_list': latest_articles_list})
#
def detail(request, article_id):
    try:
        article_detail = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")
    latest_comments_list = article_detail.comment_set.order_by('-id')[:10]

    return render(request, 'rwr/detail.html', {'article':article_detail, 'latest_comments_list':latest_comments_list})
#
#
# def leave_comment(request, article_id):
#     try:
#         article_detail = Article.objects.get(id=article_id)
#     except:
#         raise Http404("Статья не найдена")
#
#     article_detail.comment_set.create(author_name = request.POST['name'], comment_text = request.POST["text"])
#     return HttpResponseRedirect( reverse('articles:detail', args = (article_detail.id, )) )
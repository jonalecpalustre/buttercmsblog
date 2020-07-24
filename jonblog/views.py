from django.http import Http404
from django.shortcuts import render
from butter_cms import ButterCMS
from django.conf import settings

client = ButterCMS(settings.BUTTER_API_KEY)


def home(request):
    return render(request, 'home.html', {})

def blog(request, page=1):
    response = client.posts.all({'page_size': 10, 'page': page})

    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']

    return render(request, 'blog.html', {
        'recent_posts': recent_posts,
        'next_page': next_page,
        'previous_page': previous_page
    })

def post(request, slug):
    try:
        response = client.posts.get(slug)
    except:
        raise Http404('Post not found')

    post = response['data']
    return render(request, 'blog_post.html', {
        'post': post
    })

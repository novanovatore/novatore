from django.shortcuts import render
from .models import *

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    print(posts)

    categorias_con_posts = Categoria.objects.filter(post__isnull=False).distinct()

    categorias_usadas = []
    #for c in categorias_con_posts:
    #    categorias_usadas.append(c.nombre)

    return render(request, "Blog/blog.html", {"posts": posts, "categorias": categorias_con_posts})



def categoria(request, categoria_id):
    try:
        cat = Categoria.objects.get(id=categoria_id) 
        posts = Post.objects.filter(categoria=cat)

        return render(request, "Blog/categoria.html", {"categoria": cat, "posts": posts})
    except Categoria.DoesNotExist:
        pass
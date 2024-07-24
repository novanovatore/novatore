from django.shortcuts import render
from .models import *

# Create your views here.

def blog(request):
    
    posts = Post.objects.prefetch_related("categoria")
    print(posts)

    post_mas_categoria = []
    for p in posts:
        post_mas_categoria.append(
            {
                "post": p, 
                "categorias": p.categoria.all()
            }
        )
    


    # retorna todas las categoria que tengan post asociados.
    categorias_con_posts = Categoria.objects.filter(post__isnull=False).distinct()

    

    return render(request, "Blog/blog.html", {"posts": post_mas_categoria, "categorias": categorias_con_posts})



def categoria(request, categoria_id):
    try:
        cat = Categoria.objects.get(id=categoria_id) 
        posts = Post.objects.filter(categoria=cat)

        return render(request, "Blog/categoria.html", {"categoria": cat, "posts": posts})
    except Categoria.DoesNotExist:
        print("no hay posts para esa categoria")
        return render(request, "Blog/categoria.html", {"categoria": cat})
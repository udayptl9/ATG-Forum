from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article
from django.contrib.auth.models import User

@login_required
def home(request):
    other_articles = Article.objects.filter(privacy="Public")
    auther_articles = Article.objects.filter(auther = request.user).filter(privacy="Private")
    query = request.GET.get('query')
    if query:
        other_articles = other_articles.filter(title__icontains=query).distinct()
        auther_articles = auther_articles.filter(title__icontains=query).distinct()
    context = {
        'aut_art': auther_articles,
        'oth_art': other_articles,
    }
    return render(request, 'articles/home.html', context)

@login_required
def add(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        privacy = request.POST['privacy']
        newArticle = Article(auther=request.user, title=title, description=description, image=image, privacy=privacy)
        newArticle.save()
        messages.success(request, 'Article posted Successfully')
        return redirect('home')
    return render(request, 'articles/add.html')

@login_required
def articleView(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'articles/view.html', {'article': article})

@login_required
def articleDelete(request, id):
    if request.method == "POST":
        article = Article.objects.get(id=id)
        if article.auther == request.user:
            article.delete()
            messages.success(request, 'Article deleted Successfully')
            return redirect('home')
        else:
            return redirect('home')
    article = Article.objects.get(id=id)
    return render(request, 'articles/delete.html', {'article': article})

@login_required
def  articleUpdate(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        privacy = request.POST['privacy']
        image = request.FILES['image']
        article = Article.objects.get(id=id)
        if article.auther == request.user:
            article.title = title
            article.description = description
            article.privacy = privacy
            article.image = image
            article.save()
            messages.success(request, 'Article updated successfully')
            return redirect('home')
    return render(request, 'articles/update.html', {'article': article})

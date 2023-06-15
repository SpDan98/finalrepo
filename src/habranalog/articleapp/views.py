from django.shortcuts import render,get_object_or_404,redirect
from articleapp.models import *
from django.contrib.auth.decorators import login_required
from articleapp.forms import *

# Create your views here.

def home(request):
    data=Article.objects.filter(published=True)
    return render(request,'articleapp/home.html',{'articles':data})

def view_art(request,art_id):
    # if request.user.has_perm('articleapp.can_read_article'):
        viewscount=Views.objects.filter(article=art_id).count()
        data=get_object_or_404(Article,pk=art_id,published=True)
        try:
            v=Views.objects.create(user=request.user,article=data)
        except:
            pass
        blocks=ArticlesBlock.objects.filter(article=art_id)
        return render(request,'articleapp/view_art.html',{'article':data, 'blocks':blocks,'viewscount':viewscount})
    # else:
    #     return 

@login_required
def create_article(request):
    if request.method=='GET':
        return render(request,'articleapp/create_article.html',{'form':CreateArticleForm()})
    else:
        try:
            form=CreateArticleForm(request.POST,request.FILES)
            newart=form.save(commit=False)
            newart.author=request.user
            form.save()
            return redirect('articleapp:home')
        except:
            return render(request,'articleapp/create_article.html',{'form':CreateArticleForm(),'error':'некорректное значение'})

@login_required
def change_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='GET':
        return render(request,'articleapp/change_article.html',{'article':article})
    else:
        try:
            form=CreateArticleForm(request.POST,request.FILES,instance=article)
            form.save()
            return redirect('articleapp:home')
        except:
            return render(request,'articleapp/change_article.html',{'article':article,'error':'некорректное значение'})
        
@login_required
def view_article(request,art_id):
    article_=get_object_or_404(Article,pk=art_id,author=request.user)
    articleblocks=ArticlesBlock.objects.filter(article=art_id)
    return render(request,'articleapp/view_article.html',{'article':article_,'articleblocks':articleblocks})

@login_required
def delete_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='POST':
        article.delete()
        return redirect('articleapp:home')

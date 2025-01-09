from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.

def record(request):
    return render(request, 'index.html')

def timeline(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'timeline.html', {'posts': posts})

def todo(request):
    return render(request, 'todo.html')

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('timeline')
        else:
            print(form.errors)  # エラー内容を確認
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form, 'errors': form.errors})

# 削除確認ページ
def confirm_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 削除確認ページを表示
    return render(request, 'confirm_delete.html', {'post': post})

# 実際に投稿を削除
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        post.delete()  # 投稿を削除
        return redirect('timeline')  # 削除後にタイムラインにリダイレクト
    
    # GETメソッドでアクセスされた場合は、確認ページにリダイレクト
    return redirect('confirm_delete', post_id=post.id)

def home(request):
    return render(request, 'home.html')

# カウントダウンページビュー
def countdown(request):
    return render(request, 'countdown.html')
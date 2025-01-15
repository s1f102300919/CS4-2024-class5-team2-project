from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def view_profile(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    return render(request, 'profile/profile.html', {'user': user, 'profile': profile})

@login_required
def edit_profile(request):
    # ログインしているユーザーのプロフィールを取得
    user = request.user

    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None  # プロフィールがない場合

    if request.method == 'POST':
        # フォームが送信されたとき
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # フォームのデータを保存
            return redirect('view_profile')  # 保存後、プロフィールページにリダイレクト
    else:
        # GETリクエストの場合、フォームにユーザーのプロフィール情報を初期値として設定
        form = UserProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form})

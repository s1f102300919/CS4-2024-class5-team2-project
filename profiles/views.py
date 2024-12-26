from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    # ログインしているユーザーのプロファイルを取得
    user_profile = request.user.userprofile  # `userprofile` は `User` と `UserProfile` を関連付けたもの
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # プロフィールページにリダイレクト（必要に応じて変更）
    else:
        form = UserProfileForm(instance=user_profile)
    
    return render(request, 'edit_profile.html', {'form': form})

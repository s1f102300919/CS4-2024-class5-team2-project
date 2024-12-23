from django.shortcuts import render, redirect
from .models import Subject
from django.http import HttpResponse

# Create your views here.
def top(request):
    #  科目リストの取得
    subject_list = Subject.objects.values_list("name", flat=True)

    if request.method == "POST" and "new_subject" in request.POST:
        new_subject = request.POST.get("new_subject", "").strip()
        if new_subject and not Subject.objects.filter(name=new_subject).exists():
            Subject.objects.create(name=new_subject)
        return redirect("top")

    return render(request, "index.html", {"subject_list": subject_list})

# 科目削除
def delete_subject(request):
    if request.method == "POST":
        subject_name = request.POST.get("subject_name", "").strip()
        if subject_name:
            Subject.objects.filter(name=subject_name).delete()
    return redirect("top")

def form(request):
    data = {}
    if request.method == "POST":
        content = request.POST["content"]
        selected_subject = request.POST.get("selected_subject", "未選択")
        elapsed_time = request.POST.get("elapsed_time", "00:00:00")

        data = {
            "content": content,
            "selected_subject": selected_subject,
            "elapsed_time": elapsed_time,
        }

    return render(request, "record/form.html", data)
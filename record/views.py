from django.shortcuts import render, redirect
from .models import Subject, StudyRecord
from datetime import timedelta

def top(request):
    subject_list = Subject.objects.values_list("name", flat=True)
    if request.method == "POST" and "new_subject" in request.POST:
        new_subject = request.POST.get("new_subject", "").strip()
        if new_subject and not Subject.objects.filter(name=new_subject).exists():
            Subject.objects.create(name=new_subject)
        return redirect("top")
    return render(request, "index.html", {"subject_list": subject_list})

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
        elapsed_time_str = request.POST.get("elapsed_time", "00:00:00")

        # 時間の文字列を timedelta に変換
        hours, minutes, seconds = map(int, elapsed_time_str.split(':'))
        elapsed_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        # StudyRecord モデルに保存
        record = StudyRecord.objects.create(
            subject=selected_subject,
            comment=content,
            elapsed_time=elapsed_time
        )

        data = {
            "content": content,
            "selected_subject": selected_subject,
            "elapsed_time": elapsed_time_str,
        }

    return render(request, "record/form.html", {"records": StudyRecord.objects.all()})